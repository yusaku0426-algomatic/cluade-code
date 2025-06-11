#!/usr/bin/env python3
"""
Claude Code テストプロジェクト
基本的なPython関数のサンプル
"""

def hello_world():
    """簡単な挨拶関数"""
    print("Hello, Claude Code!")
    print("このプロジェクトはClaude Codeのテスト用です")

def calculate_sum(a: int, b: int) -> int:
    """
    二つの数値を足し算する関数
    
    Args:
        a (int): 最初の数値
        b (int): 二番目の数値
    
    Returns:
        int: 合計値
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("引数は数値である必要があります")
    
    return a + b

def calculate_factorial(n: int) -> int:
    """
    階乗を計算する関数
    
    Args:
        n (int): 階乗を計算する数値
        
    Returns:
        int: n の階乗
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("引数は0以上の整数である必要があります")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("Claude Code テストプロジェクト実行中")
    print("=" * 50)
    
    # 挨拶
    hello_world()
    print()
    
    # 足し算テスト
    try:
        result = calculate_sum(5, 3)
        print(f"5 + 3 = {result}")
        
        result = calculate_sum(10, -2)
        print(f"10 + (-2) = {result}")
    except (TypeError, ValueError) as e:
        print(f"エラー: {e}")
    
    print()
    
    # 階乗テスト
    try:
        for i in [0, 1, 5, 10]:
            result = calculate_factorial(i)
            print(f"{i}! = {result}")
    except (TypeError, ValueError) as e:
        print(f"エラー: {e}")
    
    print("\n" + "=" * 50)
    print("テスト完了")
    print("=" * 50) 