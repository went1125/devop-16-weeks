# Week 1 incident lab

每題使用相同流程：**impact → hypothesis → highest-information check → evidence → mitigation → root cause → prevention**。不要同時改三個設定，否則無法知道哪個變更有效。

## Incident A — 502 Bad Gateway

在 `project/nginx/default.conf` 中把 API upstream port 由 `8000` 改成 `8001`，重建 gateway。

- Symptom:
- User impact:
- Hypothesis:
- Evidence:
- Commands:
- Mitigation:
- Root cause:
- Prevention:

提示：比較 Nginx error log、API listen port、container DNS resolution 與 TCP connection。

## Incident B — API cannot resolve database

在 `.env` 中把 `POSTGRES_HOST` 改為不存在的 hostname，重建 API。

- Symptom:
- User impact:
- Hypothesis:
- Evidence:
- Commands:
- Mitigation:
- Root cause:
- Prevention:

提示：先區分 name resolution failure、refused 與 timeout。

## Incident C — Persistent data disappears

先建立一筆 hit counter evidence，再比較 `docker compose down` 與 `docker compose down -v` 的結果。

> `down -v` 會刪除此 lab 的 named volume。只可在確認 lab 資料可丟棄後執行。

- Expected lifecycle:
- Actual evidence:
- Root cause of data loss:
- Production prevention:

## Optional pressure lab

把 API memory limit 調到不合理的小值並製造流量，觀察 exit code、OOMKilled/inspect、logs 與 restart behavior。不要在重要環境執行。

