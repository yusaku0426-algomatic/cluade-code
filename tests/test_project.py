#!/usr/bin/env python3
"""
Claude Code テストプロジェクト用のユニットテスト
"""
import unittest
import sys
import os

# srcディレクトリのパスを追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from test_project import calculate_sum, hello_world

class TestProjectFunctions(unittest.TestCase):
    """テストプロジェクトの関数をテストするクラス"""
    
    def test_calculate_sum_positive_numbers(self):
        """正の数の足し算テスト"""
        result = calculate_sum(5, 3)
        self.assertEqual(result, 8)
    
    def test_calculate_sum_negative_numbers(self):
        """負の数を含む足し算テスト"""
        result = calculate_sum(10, -2)
        self.assertEqual(result, 8)
    
    def test_calculate_sum_zero(self):
        """ゼロを含む足し算テスト"""
        result = calculate_sum(0, 5)
        self.assertEqual(result, 5)
    
    def test_calculate_sum_both_zero(self):
        """両方ゼロの足し算テスト"""
        result = calculate_sum(0, 0)
        self.assertEqual(result, 0)
    
    def test_calculate_sum_float_numbers(self):
        """浮動小数点数の足し算テスト"""
        result = calculate_sum(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2, places=1)
    
    def test_calculate_sum_invalid_input(self):
        """無効な入力のテスト"""
        with self.assertRaises(TypeError):
            calculate_sum("5", 3)
        
        with self.assertRaises(TypeError):
            calculate_sum(5, "3")
        
        with self.assertRaises(TypeError):
            calculate_sum(None, 5)

if __name__ == '__main__':
    # テスト実行
    unittest.main(verbosity=2) 