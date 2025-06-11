#!/usr/bin/env python3
"""
Claude Code テストプロジェクト - 基本的な使用例
"""
import sys
import os

# srcディレクトリのパスを追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def main():
    """メイン実行関数"""
    print("🚀 Claude Code テストプロジェクト - 実行例")
    print("=" * 50)
    
    try:
        from test_project import hello_world, calculate_sum
        
        # 1. 基本的な挨拶
        print("\n1. 基本的な挨拶:")
        hello_world()
        
        # 2. 基本的な計算
        print("\n2. 基本的な計算:")
        examples = [
            (5, 3),
            (10, -2),
            (0, 100),
            (-5, -10)
        ]
        
        for a, b in examples:
            try:
                result = calculate_sum(a, b)
                print(f"  {a} + {b} = {result}")
            except Exception as e:
                print(f"  エラー: {a} + {b} -> {e}")
        
        print("\n" + "=" * 50)
        print("✅ 実行例完了")
        
    except ImportError as e:
        print(f"❌ インポートエラー: {e}")
        print("src/test_project.py が存在することを確認してください")

if __name__ == "__main__":
    main() 