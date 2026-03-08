import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from queens import solve_n_queens


class TestNQueens(unittest.TestCase):
    """八皇后问题单元测试类"""

    def test_4_queens(self):
        """测试4皇后（已知应有2个解）"""
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)  # 断言解的数量为2

    def test_8_queens(self):
        """测试8皇后（已知应有92个解）"""
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92)  # 断言解的数量为92

    def test_1_queen(self):
        """边界测试：1皇后（应有1个解）"""
        solutions = solve_n_queens(1)
        self.assertEqual(len(solutions), 1)


# 运行测试
if __name__ == "__main__":
    unittest.main()