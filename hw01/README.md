# 八皇后问题求解器
## 项目简介
本项目基于 Python 实现**回溯算法**求解 n 皇后问题，核心目标是找到所有合法的皇后放置方案，确保任意两个皇后不在同一行、同一列或同一对角线上。项目包含源码实现、单元测试、运行说明，适配 Windows 系统 + PyCharm 开发环境。
## 实现思路
n 皇后问题的核心解法为回溯算法，具体步骤如下：1. **逐行放置**：按行遍历棋盘，每行仅放置一个皇后（避免同行冲突）；2. **合法性检查**：放置前验证当前列、左上对角线、右上对角线是否已有皇后；3. **回溯递归**：若当前行无合法列可放置，则回溯到上一行，移除上一行的皇后并尝试下一列；4. **结果收集**：当所有行都放置完皇后时，记录当前棋盘布局为一个有效解。
核心函数说明：- `is_safe(board, row, col, n)`：检查 (row, col) 位置是否可放置皇后；- `backtrack(row, n, board, result)`：递归回溯放置皇后，收集所有有效解；- `solve_n_queens(n)`：入口函数，返回 n 皇后的所有解；- `print_solution(result)`：格式化打印所有解的棋盘布局。
## 项目结构
hw01/├── src/ # 源码目录│ └── queens.py # 八皇后求解核心代码├── tests/ # 测试目录│ └── test_queens.py # 单元测试文件（验证解的数量）├── README.md # 项目说明文档└── prompt_log.md # AI 交互日志
## 运行与测试指南
### 前置条件
1. 已安装 Python 3.7+（推荐 3.9+），并勾选「Add Python to PATH」；2. 已将项目导入 PyCharm，且 `src` 目录标记为「源代码根目录」，`tests` 目录标记为「测试源代码根目录」。
### 1. 运行求解器
#### 方式1：PyCharm 直接运行
- 打开 `src/queens.py` 文件；- 点击文件右上角「运行」按钮（绿色三角），或右键 →「运行 'queens'」；- 运行结果会显示在 PyCharm 底部「Run」面板，包含 4/8 皇后的所有解及解的数量。
#### 方式2：终端运行
1. 打开 PyCharm 终端（底部「终端」标签）；2. 切换到 `hw01` 目录：
   ```bash
   cd hw01
执行求解器：
bash
运行
python src/queens.py
3.运行单元测试
步骤 1：安装 pytest（首次运行需执行）
bash
运行
pip install pytest
步骤 2：执行测试用例
在 PyCharm 终端（已切换到 hw01 目录）执行：
bash
运行
pytest tests/test_queens.py -v
测试结果说明
1 皇后问题：预期解数量 → 1；- 4 皇后问题：预期解数量 → 2；- 8 皇后问题：预期解数量 → 92；- 测试通过时终端显示「3 passed」，代表所有用例验证成功。
常见问题解决
问题 1：运行 queens.py 双击后闪退
原因：Python 脚本运行完自动关闭窗口；- 解决：在 queens.py 末尾添加 input("按回车键退出...")，或使用终端 / PyCharm 运行。
问题 2：pytest 提示「找不到 src 模块」
原因：src 未标记为源代码根目录；- 解决：1. PyCharm 右键 src →「将目录标记为」→「源代码根目录」；2. 或终端临时配置路径：
bash
运行
set PYTHONPATH=%cd%\src && pytest tests/test_queens.py -v
问题 3：pytest 未被识别为命令
原因：pytest 未安装或未加入环境变量；- 解决：使用 python -m pytest 替代直接执行 pytest：
bash
运行
python -m pytest tests/test_queens.py -v
预期输出示例
4 皇后问题输出
plaintext
4皇后问题的解：
解法 1：
. Q . . 
. . . Q 
Q . . . 
. . Q . 

解法 2：
. . Q . 
Q . . . 
. . . Q 
. Q . . 

4皇后共有2个解
8 皇后问题输出（节选）
plaintext
8皇后问题的解：
解法 1：
Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . Q . 
. Q . . . . . . 
. . . Q . . . . 

...（共92个解）
8皇后共有92个解