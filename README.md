# 16-Week DevOps Learning Journey

這個 repository 是一份以實作證據為核心的 DevOps / SRE / Platform Engineering 學習紀錄。

## Current status

| Week | Topic | Status | Evidence |
|---|---|---|---|
| 1 | Docker, Linux & Networking | In progress | [Week 1](./weeks/week-01/README.md) |
| 2–16 | See the Excel roadmap | Planned | To be added week by week |

## Repository map

```text
weeks/week-01/          教材、每日任務、incident lab、retrospective
project/                16 週持續演進的 Cloud Native SaaS
docs/adr/               架構決策紀錄
.github/                Issue / Pull Request templates
```

## Learning contract

- 以可重現的 evidence 判定完成，不用「看完影片」判定完成。
- 每個功能使用短分支與 Pull Request，`main` 必須可運行。
- 每週至少一次故障注入、一次 retrospective、一次 5 分鐘口述 demo。
- 不提交 `.env`、密碼、Token、憑證、私鑰或雲端 access key。
- AI 可以解釋與 review；診斷時先收集 evidence，再讓 AI 更新 hypothesis。

## Week 1 quick start

需求：Docker Desktop（含 Compose v2）、Git、PowerShell 7；Windows 建議使用 WSL2 backend。

```powershell
Copy-Item project/.env.example project/.env
Set-Location project
docker compose config
docker compose up --build -d
./scripts/verify.ps1
docker compose ps
```

完成後開啟 `http://localhost:8080`。清理環境：

```powershell
docker compose down
```

若要連資料 volume 一起刪除，先確認資料不需要，再執行 `docker compose down -v`。

## Official references

- Docker Compose specification: https://docs.docker.com/reference/compose-file/
- Compose startup order and health checks: https://docs.docker.com/compose/how-tos/startup-order/
- Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- Linux namespaces overview: https://man7.org/linux/man-pages/man7/namespaces.7.html
- GitHub repository practices: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories

