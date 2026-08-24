# ADR-0001: Use one evolving SaaS project

- Status: Accepted
- Date: 2026-08-25

## Context

此課程要證明的是從 commit 到 production 的交付與維運能力，而非累積彼此無關的小範例。

## Decision

16 週只維護同一套 Cloud Native SaaS。Week 1 由 Docker Compose 起步，之後逐步加入 CI/CD、AWS、IaC、Kubernetes、GitOps、observability、SRE、安全、platform 與 AI inference。

## Consequences

- 優點：每個技術選擇都有真實上下文，能展示演進、故障與 trade-off。
- 代價：需要維護 backward compatibility，並主動控制應用功能範圍。
- Guardrail：應用只維持足以驗證平台能力的最小功能，不把課程變成產品開發。

