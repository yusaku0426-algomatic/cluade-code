# Claude Code テストプロジェクト

Claude Codeの動作テスト用Pythonプロジェクトです。

## 📁 プロジェクト構造

```
claude-projects/
├── src/                    # ソースコード
│   ├── test_project.py     # メインプログラム
│   └── hello.py           # 追加のサンプルコード
├── tests/                  # テストファイル
│   ├── __init__.py
│   └── test_project.py    # ユニットテスト
├── .gitignore             # Git除外設定
└── README.md              # このファイル
```

## 🚀 クイックスタート

### プログラム実行
```bash
# メインプログラム実行
python3 src/test_project.py

# hello.py実行
python3 src/hello.py
```

### テスト実行
```bash
# ユニットテスト実行
python3 tests/test_project.py
```

## 🧪 機能

### 基本機能
- **hello_world()**: 挨拶メッセージの出力
- **calculate_sum()**: 数値の足し算（型チェック付き）

### 特徴
- ✅ 型ヒント対応
- ✅ エラーハンドリング
- ✅ ユニットテスト
- ✅ 標準的なPythonプロジェクト構造

## 🤖 Claude Code 連携

このプロジェクトはClaude Codeでのテストを想定しています：

```bash
# Claude Codeでプロジェクト分析
claude "このプロジェクトを分析して改善提案をして"

# Claude Codeで新機能追加
claude "新しい数学関数を追加してテストも含めて実装して"

# Claude Codeでコード品質向上
claude "コードの品質を向上させて、ドキュメントも更新して"
```

## 📈 開発履歴

- **2025年6月11日**: プロジェクト構造を整理（src/、tests/に分離）
- **2025年6月1日**: プロジェクト作成、Git練習開始

## 📝 目的

- Git の基本操作を学ぶ
- Claude Code の使い方を習得する
- マージとコンフリクト解決をマスターする  
- Pythonプログラミングスキルを向上させる

## 🔗 リンク

- **GitHub**: https://github.com/yusaku0426-algomatic/cluade-code.git
- **Claude Code**: https://docs.anthropic.com/claude-code/

## 📝 TODO

- [ ] 追加の数学関数実装
- [ ] CI/CDパイプライン設定
- [ ] ドキュメント追加
- [ ] Docker対応
