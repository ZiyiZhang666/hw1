def is_safe(board, row, col, n):
    """
    检查(row, col)位置是否可以放置皇后（修复后：完整检查所有冲突）
    """
    # 检查同一列是否有皇后
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 修复：恢复左上到右下对角线检查
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 检查右上到左下对角线是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def backtrack(row, n, board, result):
    """
    回溯算法核心：逐行放置皇后，收集所有有效解
    """
    # 所有行都放置完皇后，记录当前解
    if row == n:
        # 转换棋盘格式（1→Q，0→.）
        solution = []
        for i in range(n):
            row_str = ""
            for j in range(n):
                row_str += "Q" if board[i][j] == 1 else "."
            solution.append(row_str)
        result.append(solution)
        return

    # 遍历当前行的每一列，尝试放置皇后
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # 放置皇后
            backtrack(row + 1, n, board, result)  # 递归处理下一行
            board[row][col] = 0  # 回溯：移除皇后


def solve_n_queens(n):
    """
    入口函数：求解n皇后问题，返回所有解
    """
    # 初始化棋盘（n×n，0表示空，1表示皇后）
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    backtrack(0, n, board, result)
    return result


def print_solution(result):
    """
    格式化打印所有解
    """
    n = len(result[0]) if result else 0
    print(f"{n}皇后问题的解：")
    for idx, solution in enumerate(result, 1):
        print(f"解法 {idx}：")
        for row in solution:
            print(row)
        print()
    print(f"{n}皇后共有{len(result)}个解")


# 主程序：测试4皇后和8皇后
if __name__ == "__main__":
    # 测试4皇后（修复后输出2个解）
    res_4 = solve_n_queens(4)
    print_solution(res_4)

    # 测试8皇后（修复后输出92个解）
    res_8 = solve_n_queens(8)
    print_solution(res_8)

    # 防止运行后闪退
    input("\n按回车键退出...")