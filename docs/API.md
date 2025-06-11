# Claude Code テストプロジェクト API ドキュメント

## 概要
Claude Codeのテスト用Python プロジェクトのAPI仕様書です。

## モジュール: test_project.py

### 関数一覧

#### `hello_world()`
- **説明**: 簡単な挨拶メッセージを出力する関数
- **引数**: なし
- **戻り値**: なし
- **例**:
  ```python
  hello_world()
  # 出力: "Hello, Claude Code!"
  #       "GitHubテスト用プロジェクト"
  ```

#### `calculate_sum(a: int, b: int) -> int`
- **説明**: 二つの数値を足し算する関数（型チェック付き）
- **引数**:
  - `a` (int|float): 最初の数値
  - `b` (int|float): 二番目の数値
- **戻り値**: int|float - 合計値
- **例外**:
  - `TypeError`: 引数が数値でない場合
- **例**:
  ```python
  result = calculate_sum(5, 3)
  print(result)  # 8
  ```

## 使用例

```python
#!/usr/bin/env python3
from src.test_project import hello_world, calculate_sum

# 挨拶
hello_world()

# 計算
result = calculate_sum(10, 20)
print(f"10 + 20 = {result}")
```

## テスト実行

```bash
# 特定のテストファイル実行
python3 tests/test_project.py

# カバレッジ付きテスト実行  
python3 -m pytest tests/ --cov=src
``` 