# Week 1 checklist

## Theory

- [ ] 我能區分 process、image、container、service。
- [ ] 我能說明 PID/network/mount namespace 與 cgroup 的責任。
- [ ] 我能畫出 browser → Nginx → API → PostgreSQL/Redis 的 request path。
- [ ] 我能區分 DNS failure、connection refused、timeout、HTTP 5xx。

## Build

- [ ] `docker compose config` 成功，且我已檢查 resolved configuration。
- [ ] `docker compose up --build -d` 後所有服務 healthy/running。
- [ ] `./scripts/verify.ps1` 通過。
- [ ] API container 以 non-root user 執行。
- [ ] PostgreSQL 未 publish 到 host。
- [ ] 重建 API container 後資料仍存在。

## Debug

- [ ] 我在不知道答案的情況下完成三個 incident。
- [ ] 每題都有 hypothesis、evidence、commands、root cause、prevention。
- [ ] 我能解釋為何「先重啟」會破壞部分 evidence。

## Review and interview

- [ ] 我完成 5 分鐘 demo。
- [ ] 我回答所有 interview questions 並標示薄弱題。
- [ ] 我完成 retrospective 與下一週 Top 3。
- [ ] PR 有驗收證據、風險與 rollback。

