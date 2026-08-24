# Working agreement

## Branch and pull request flow

1. 從最新的 `main` 建立短分支：`week-01/<type>-<topic>`。
2. 一個 Pull Request 只處理一個可驗收目標。
3. PR 必須包含：Why、What、How to verify、Evidence、Risk、Rollback。
4. 合併前自行 review diff，確認沒有秘密資料與非必要產物。
5. 優先 squash merge，讓 `main` 的歷史對學習作品集保持清楚。

建議 commit 格式：

```text
feat(api): add dependency health endpoint
fix(compose): wait for postgres readiness
docs(week-01): record DNS incident evidence
test(smoke): verify reverse-proxy route
```

## Definition of done

- 驗收指令由乾淨環境可重現。
- 文件說明「為什麼」，設定檔呈現「怎麼做」。
- 新的 failure mode 有對應檢查方式或 runbook。
- PR 附終端輸出、截圖或 dashboard URL；不得只寫「works on my machine」。

