# Claude Code テストプロジェクト Makefile

.PHONY: help test lint format install clean run example

# デフォルトターゲット
help:
	@echo "Claude Code テストプロジェクト"
	@echo ""
	@echo "利用可能なコマンド:"
	@echo "  install    - 依存関係をインストール"
	@echo "  test       - テストを実行"
	@echo "  lint       - コード品質チェック"
	@echo "  format     - コードフォーマット"
	@echo "  run        - メインプログラム実行"
	@echo "  example    - 使用例を実行"
	@echo "  clean      - 一時ファイルを削除"

# 依存関係インストール
install:
	pip install -r requirements.txt

# テスト実行
test:
	python -m pytest tests/ -v
	@echo "✅ テスト完了"

# テストカバレッジ付き
test-cov:
	python -m pytest tests/ --cov=src --cov-report=html
	@echo "📊 カバレッジレポート: htmlcov/index.html"

# コード品質チェック
lint:
	flake8 src tests examples
	mypy src tests examples
	@echo "🔍 Lint チェック完了"

# コードフォーマット
format:
	black src tests examples
	@echo "✨ コードフォーマット完了"

# メインプログラム実行
run:
	python src/test_project.py

# 使用例実行
example:
	python examples/basic_usage.py

# クリーンアップ
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	@echo "🗑️  クリーンアップ完了" 