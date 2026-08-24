# Week 1 Day 1 — Linux isolation and request path

> 建議紀錄時間：開始前 3 分鐘、學習中隨手記 evidence、結束後 10 分鐘。

## 1. Session metadata

| Field | Value |
|---|---|
| Date | 2026-08-25 |
| Type | Theory |
| Planned time | 2h |
| Actual time |  |
| Energy before / after | / 5 · / 5 |
| Related Issue / PR |  |
| Status | Not Started |

## 2. One outcome for today

> 我能畫出 browser → Nginx → API → PostgreSQL/Redis 的 request path，並用自己的話解釋 namespace 與 cgroup 在 container 中的不同責任。

### Acceptance criteria

- [ ] 我能解釋 PID、network、mount namespace 分別隔離什麼。
- [ ] 我能解釋 cgroup 如何限制與計量 CPU、memory。
- [ ] 我能依序說明 DNS → TCP → HTTP → reverse proxy。
- [ ] 我完成一張 request path 圖與三題 retrieval questions。

## 3. Before learning

### My current mental model

在查資料前先寫 3–5 句，允許寫錯：

- Namespace:
- Cgroup:
- Container image vs container:
- DNS → TCP → HTTP:

### Questions I want to answer

1. 為什麼 container 內的 PID 1 與 host 看到的 PID 不同？
2. Container 的 memory limit 是由 namespace 還是 cgroup 實作？
3. API container 為什麼不能用 `localhost` 找 PostgreSQL？

## 4. What I learned

| Concept | My explanation | Production relevance |
|---|---|---|
| PID namespace |  |  |
| Network namespace |  |  |
| Mount namespace |  |  |
| Cgroup |  |  |
| DNS / TCP / HTTP |  |  |

### Request path

```text
Browser :8080
    │
    ▼
Nginx reverse proxy
    ├── /      → frontend
    └── /api/* → API
                    ├── PostgreSQL
                    └── Redis
```

在每一條箭頭旁補上 hostname、port、protocol，以及失敗時可能看到的症狀。

## 5. Evidence

### Commands and key output

```text
開始 Docker lab 後，記錄 ps、id、/proc/1/status、/proc/1/cgroup 與 DNS 查詢的關鍵輸出。
不要貼完整 log、密碼、Token 或 .env。
```

- Diagram:
- Commit:
- Screenshot:
- Conclusion:

## 6. Explain-back

1. Namespace 與 cgroup 最大的差異？
2. `curl http://localhost:8080/api/info` 背後依序發生什麼？
3. DNS 成功但 TCP timeout，下一步要收集什麼 evidence？
4. PID 1 收到 SIGTERM 時，應用程式應如何反應？

## 7. AI collaboration record

- AI role used:
- Prompt summary:
- Suggestion I verified:
- What I can now explain without AI:

## 8. End-of-day checkpoint

### Three-line summary

1. Learned:
2. Proved:
3. Still unclear:

### Retrieval questions

1. Q: Container isolation 主要依靠哪兩類 Linux 機制？
   A:
2. Q: 為什麼 API 使用 `postgres:5432` 而非 `localhost:5432`？
   A:
3. Q: Connection refused 與 timeout 通常分別暗示什麼？
   A:

### Next smallest action

> Day 2 開始後 15 分鐘內：讀 Dockerfile，先預測每一層的 cache 行為與執行使用者。

### Final status

- [ ] Acceptance criteria completed
- [ ] Evidence committed or linked
- [ ] Blocker converted into an Issue
- [ ] Sensitive information checked
