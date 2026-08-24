import os
import socket

import asyncpg
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Week 1 DevOps API")
pool: asyncpg.Pool | None = None
cache: redis.Redis | None = None


@app.on_event("startup")
async def startup() -> None:
    global pool, cache
    pool = await asyncpg.create_pool(
        host=os.environ["POSTGRES_HOST"],
        database=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        min_size=1,
        max_size=5,
    )
    cache = redis.Redis(host=os.environ["REDIS_HOST"], decode_responses=True)
    async with pool.acquire() as connection:
        await connection.execute(
            "CREATE TABLE IF NOT EXISTS visits (id integer PRIMARY KEY, count integer NOT NULL)"
        )
        await connection.execute(
            "INSERT INTO visits (id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING"
        )


@app.on_event("shutdown")
async def shutdown() -> None:
    if cache:
        await cache.aclose()
    if pool:
        await pool.close()


@app.get("/healthz")
async def healthz() -> dict:
    try:
        assert pool is not None and cache is not None
        await pool.fetchval("SELECT 1")
        await cache.ping()
        return {"status": "ok"}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="dependency unavailable") from exc


@app.get("/info")
async def info() -> dict:
    assert pool is not None and cache is not None
    async with pool.acquire() as connection:
        visits = await connection.fetchval(
            "UPDATE visits SET count = count + 1 WHERE id = 1 RETURNING count"
        )
    redis_visits = await cache.incr("visits")
    return {
        "message": "Week 1 stack is running",
        "hostname": socket.gethostname(),
        "postgres_visits": visits,
        "redis_visits": redis_visits,
    }

