# Week 1 — Docker, Linux & Networking

目標不是背 Docker 指令，而是能回答並證明：一個 HTTP request 如何經 DNS/TCP、reverse proxy、API、PostgreSQL 與 Redis，且故障時能以 evidence 找到 root cause。

預計 14 小時。完成標準以 [checklist](./checklist.md) 為準。

## Mental model

```text
Browser :8080
    │ HTTP
    ▼
Nginx reverse proxy
    ├── /      → frontend:8080
    └── /api/* → api:8000
                    ├── TCP/DNS → postgres:5432
                    └── TCP/DNS → redis:6379
```

Container 不是輕量 VM。Linux namespace 隔離 process/network/mount 等資源視圖；cgroup 管理與計量 CPU、memory 等資源。Image 是不可變 build artifact，container 是 image 的執行個體，volume 才承載需要跨 container replacement 保留的狀態。

## Seven-day schedule

| Day | Type | Time | Work | Evidence |
|---|---|---:|---|---|
| 1 | Theory | 2h | namespaces/cgroups、process/signal、DNS→TCP→HTTP mental model | `notes/day-01.md` + 手繪 request path |
| 2 | Build | 2.5h | 讀懂 Dockerfile、build context、layer/cache、non-root | image history + `docker inspect` 摘要 |
| 3 | Build | 2.5h | 啟動五服務 stack；驗證 network、health、persistence | `verify.ps1` output + screenshot |
| 4 | Debug | 2.5h | 完成三個故障注入，不先看解答 | [incident lab](./incident-lab.md) |
| 5 | Review | 1.5h | 改善 healthcheck、graceful shutdown、安全與 README | PR + self-review |
| 6 | Interview | 1.5h | 回答 [interview questions](./interview.md)，錄 5 分鐘 demo | 回答筆記或錄影連結 |
| 7 | Review | 1h | retrospective、更新 issue/README、排 Week 2 | [retrospective](./retrospective.md) |

## Core commands to understand

不要只複製；每個命令先寫下你預期看到什麼。

```powershell
docker compose config
docker compose build
docker compose up -d
docker compose ps
docker compose logs --tail 100 api
docker compose exec api id
docker compose exec api cat /proc/1/status
docker compose exec api cat /proc/1/cgroup
docker compose exec api getent hosts postgres
docker compose exec api getent hosts redis
docker inspect devops-api
docker stats --no-stream
docker compose down
```

## What to explain by Friday

1. `EXPOSE`、Compose `ports`、container port 的差異。
2. 為何 `depends_on` 的啟動順序不等於 dependency ready，以及 healthcheck 如何補足。
3. 為何 API 不能使用 `localhost` 連 PostgreSQL。
4. PID 1、SIGTERM 與 graceful shutdown 的關係。
5. bind mount、named volume、container writable layer 的生命週期差異。
6. 為何 production image 應用 non-root user，以及這仍不是完整安全邊界。
7. 502、connection refused、timeout、DNS resolution failure 各自暗示哪一層問題。

## Deliverable

建立 `week-01/docker-compose-foundation` Pull Request，附：

- 完整 `docker compose ps` 與 smoke-test evidence。
- 一張 request path 圖。
- 三個 incident 的 hypothesis/evidence/root cause/prevention。
- 一段「如果進 production，我還會改什麼」的風險說明。

