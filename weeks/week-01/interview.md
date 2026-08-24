# Week 1 interview drill

每題限時 3 分鐘，結構使用：結論 → request/data path → evidence → trade-off。

1. Container 與 VM 的隔離模型有何差異？
2. 使用者看到 502，你會先做哪三個檢查？為什麼資訊量最高？
3. `localhost` 在 API container 內指向哪裡？API 如何找到 `postgres`？
4. Process 收到 SIGTERM 後應如何結束？PID 1 有何特殊性？
5. Healthcheck、readiness、liveness 的目的是否相同？
6. 為何 DB 不應 publish host port？開發時需要連 DB 怎麼辦？
7. Image tag、image digest 與 container ID 分別代表什麼？
8. Named volume 解決什麼問題？它不是 backup 的原因？
9. DNS 成功但 TCP timeout，可能在哪幾層？你會如何縮小範圍？
10. 請對本週 Dockerfile 與 Compose 做一次 production readiness review。

## Self-rating

| Dimension | 1–5 | Evidence / gap |
|---|---:|---|
| Correctness |  |  |
| Depth |  |  |
| Debug structure |  |  |
| Trade-off |  |  |
| Communication |  |  |

