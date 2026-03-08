# AI 交互日志
## 一、AI工具说明
本项目使用 **豆包（Doubao）** 作为AI编程辅助工具，以下为开发全流程的核心交互过程。

## 二、核心需求
基于 Python 实现八皇后问题的回溯算法求解，并完成单元测试；要求故意引入Bug、记录错误日志、引导AI修复Bug，适配 PyCharm 开发环境，编写规范的 README.md 和交互日志。

## 三、关键问题与解决过程
### 1. 环境配置类问题
#### 问题1：Windows 系统找不到「查看」选项卡，无法显示文件扩展名
- 提问：找不到「查看」选项卡，无法创建 .py/.md 文件
- AI 解答：
  - 方法1：Win+R 输入 `control folders` 打开文件夹选项，切换到「查看」标签页，取消勾选「隐藏已知文件类型的扩展名」；
  - 方法2：Win11 点击文件夹右上角「三个点」→「选项」，Win10 按 Alt 键调出菜单栏→「查看」→「选项」。
- 解决效果：成功显示文件扩展名，可创建 queens.py、prompt_log.md、README.md 文件。

#### 问题2：确认 Python 是否安装完成
- 提问：如何确认 python 是否下载完成
- AI 解答：
  - 核心方法：Win+R 输入 cmd，执行 `python --version`，显示版本号即安装成功；
  - 辅助方法：开始菜单搜索 Python、查看安装目录是否有 python.exe。
- 解决效果：验证 Python 3.9.9 安装成功，环境变量配置正常。

#### 问题3：Python 安装时「Disable path length limit」选项的含义
- 提问：「Disable path length limit」什么意思
- AI 解答：禁用 Windows 260 字符路径长度限制，避免项目目录过深时 Python 工具报错，建议安装时勾选。
- 解决效果：理解选项作用，确认安装时已勾选，规避后续路径问题。

### 2. 文件操作类问题
#### 问题1：prompt_log.md 和 README.md 是否为文件夹
- 提问：prompt_log.md 和 README.md 是文件夹吗
- AI 解答：不是文件夹，是 Markdown 格式纯文本文件，创建方法与 queens.py 一致（新建文本文档→重命名为 .md 后缀）。
- 解决效果：成功在 hw01 目录下创建两个 .md 文件。

#### 问题2：queens.py 文件双击后一闪而过
- 提问：闪了一下页面就退出了怎么解决
- AI 解答：
  - 临时方案：Shift+右键打开终端，执行 `python queens.py`；
  - 永久方案：在代码末尾添加 `input("按回车键退出...")`；
  - 专业方案：PyCharm 终端运行，保留输出结果。
- 解决效果：可正常查看 queens.py 运行结果，无闪退问题。

#### 问题3：README.md 文件的格式与打开方式
- 提问：README.md 文件是什么格式，怎么打开
- AI 解答：Markdown 格式纯文本文件，可通过记事本（基础）、VS Code（推荐，支持预览）、Typora（专业）打开，核心标记包含标题（#）、列表（-）、加粗（** **）等。
- 解决效果：能编辑并预览 README.md 内容，掌握基础排版语法。

### 3. PyCharm 适配类问题
#### 问题1：PyCharm 环境下代码是否需要修改
- 提问：使用 PyCharm 环境，是否上述代码需要进行修改
- AI 解答：核心代码无需修改，仅需将 src 标记为「源代码根目录」、tests 标记为「测试源代码根目录」，配置 Python 解释器。
- 解决效果：PyCharm 无导入警告，代码可正常运行。

#### 问题2：PyCharm 中运行单元测试的详细步骤
- 提问：详细描述如何在 PyCharm 中完成运行单元测试
- AI 解答：
  - 前提：标记 src/tests 目录、配置 Python 解释器；
  - 方式1：右键 test_queens.py →「Run 'Unittests in test_queens'」；
  - 方式2：Terminal 切换到 hw01 目录，执行 `pytest tests/test_queens.py -v`（需先安装 pytest）。
- 解决效果：掌握两种测试运行方式，可验证代码正确性。

#### 问题3：PyCharm 中导入文件夹并切换到 hw01 目录
- 提问：怎么将电脑文件夹中的文件导入到 PyCharm 中，用于切换到 hw01 目录
- AI 解答：
  - 导入：PyCharm →「文件」→「打开」，选择仓库根目录（包含 hw01）；
  - 切换目录：Terminal 中执行 `cd hw01`，提示符显示 hw01 即成功。
- 解决效果：成功导入项目，Terminal 可切换到目标目录。

### 4. 测试运行报错类问题
#### 问题1：pytest 未被识别为命令
- 报错：「无法将“pytest”项识别为 cmdlet、函数、脚本文件或可运行程序的名称」
- AI 解答：
  - 原因：pytest 未安装或未加入环境变量；
  - 解决：执行 `python -m pip install pytest`，或用 `python -m pytest tests/test_queens.py -v` 运行。
- 解决效果：pytest 命令可正常识别。

#### 问题2：pytest 找不到 tests/test_queens.py 文件
- 报错：「file or directory not found: tests/test_queens.py」
- AI 解答：原因是 Terminal 路径或文件目录结构错误，核对 hw01 目录下是否有 tests 文件夹及 test_queens.py 文件。
- 解决效果：定位到文件路径问题，修正后可找到测试文件。

#### 问题3：ModuleNotFoundError: No module named 'src'
- 报错：导入 src.queens 模块失败
- AI 解答：
  - 方案1：PyCharm 右键 src →「将目录标记为」→「源代码根目录」；
  - 方案2：Terminal 执行 `set PYTHONPATH=%cd%\src && pytest tests/test_queens.py -v`；
  - 方案3：修改 test_queens.py 导入语句，手动添加 src 路径。
- 解决效果：成功导入 src 模块，单元测试可正常运行。

### 5. 故意引入Bug并引导AI修复（核心作业要求）
#### 步骤1：故意引入Bug
- 操作：打开 `src/queens.py`，注释掉 `is_safe` 函数中「检查左上到右下对角线」的代码段：
  ```python
  # 注释前的正确代码：
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
      if board[i][j] == 1:
          return False
  # 注释后的Bug代码：
  # for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
  #     if board[i][j] == 1:
  #         return False
  目的：制造对角线检查缺失的 Bug，导致 4 皇后解数量错误。
#### 步骤 2：运行测试，记录错误日志
- 执行命令：pytest tests/test_queens.py -v
- 错误日志核心内容：
- ```python
  # tests/test_queens.py::TestNQueens::test_4_queens FAILED
  # AssertionError: 6 != 2
- 说明：4 皇后预期解数量为 2，实际输出 6，测试失败。
#### 步骤 3：引导 AI 修复 Bug
- 向 AI 提交的 Prompt：
「我在八皇后问题的 is_safe 函数中注释掉了检查左上到右下对角线的代码，运行 pytest 测试时，test_4_queens 失败，报错 AssertionError: 6 != 2，请帮我定位问题并修复代码」
- AI 解答：
问题根源是缺少左上到右下对角线的合法性检查，导致皇后可以在该对角线上共存，解的数量异常；修复方案是取消该段代码的注释，恢复对角线检查逻辑。
#### 步骤 4：验证修复结果
- 操作：取消 queens.py 中被注释的对角线检查代码，保存文件；
- 重新执行测试命令：pytest tests/test_queens.py -v；
- 结果：终端显示「3 passed」，test_4_queens 验证通过，4 皇后解数量恢复为 2，Bug 修复完成。
## 四、最终成果
- 1.完成 queens.py 代码编写，实现 n 皇后问题回溯算法求解；
- 2.完成「故意引入 Bug→测试报错→引导 AI 修复→验证通过」的全流程，记录完整错误日志和 AI 交互内容；
- 3.完成 test_queens.py 单元测试，验证 1/4/8 皇后解的数量正确性；
- 4.编写完整的 README.md，包含实现思路、运行 / 测试步骤；
整理本次开发全流程的 AI 交互日志，覆盖环境配置、文件操作、PyCharm 适配、Bug 处理等所有环节。