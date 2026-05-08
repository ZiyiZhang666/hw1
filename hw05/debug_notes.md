# 任务一：CNN 代码调试记录
本次实验基于 PyTorch 实现 MNIST 手写数字识别 CNN，调试过程中遇到以下问题，均已定位并修复：

---

## 问题 1：依赖库缺失（`ModuleNotFoundError: No module named 'matplotlib'`）
### 现象
运行代码时，导入 `matplotlib` 模块报错，红色波浪线提示模块未找到，无法执行数据可视化部分。

### 原因分析
当前运行代码的 Python 环境中，仅安装了 PyTorch，未安装 `matplotlib` 和 `numpy` 依赖库，导致模块无法被识别。

### 修复方法
1.  在 PyCharm 终端中，直接使用目标环境的 `pip` 安装依赖：
    ```bash
    D:\python\envs\pytorch_env\Scripts\pip.exe install matplotlib numpy
安装完成后，重启 PyCharm 或刷新项目索引，红色报错消失，可视化功能正常运行。
## 问题 2：解释器切换失败（conda 命令无法识别）
### 现象
尝试用 conda activate pytorch_env 切换环境时，终端报错：无法将“conda”项识别为 cmdlet、函数、脚本文件或可运行程序的名称，无法激活虚拟环境。
### 原因分析
PowerShell 终端未将 Conda 添加到系统环境变量，导致无法识别 conda 命令，无法切换到创建好的 pytorch_env 环境。
### 修复方法
放弃终端激活方式，直接在 PyCharm 中手动切换解释器：
打开「设置」→「项目」→「Python 解释器」
选择「添加解释器」→「现有环境」，找到 D:\python\envs\pytorch_env\python.exe
切换成功后，右下角显示 pytorch_env，代码中的依赖库可被正常识别。
## 问题 3：准确率异常（初始准确率仅 5%）
### 现象
训练初期，模型测试准确率仅为 5%，接近随机猜测水平，损失下降缓慢。
### 原因分析
模型结构维度不匹配：卷积层输出特征图的尺寸计算错误，导致全连接层输入维度与实际数据不匹配，模型无法正常学习特征。
### 修复方法
修正全连接层的输入维度：
单卷积层 + 池化后，特征图尺寸从 28×28 变为 14×14，因此全连接层输入应为 16 * 14 * 14
修改 nn.Linear 的 in_features 参数，确保维度匹配
重新训练模型，准确率在第 1 轮训练后即可提升至 90% 以上，最终测试准确率稳定在 98% 左右。
## 问题 4：Matplotlib 中文乱码
### 现象
运行数据可视化代码时，生成的图片中中文标签显示为方框或乱码。
### 原因分析
Matplotlib 默认字体不支持中文，导致中文无法正常渲染。
### 修复方法
在代码开头添加字体配置，指定支持中文的字体：
```python
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'  # 使用黑体支持中文
```
添加后，重新运行代码，图片中的中文标签可正常显示。
## 问题 5：MNIST 数据集下载失败
### 现象
运行代码时，torchvision.datasets.MNIST 下载数据集失败，提示网络连接超时。
### 原因分析
国内网络环境限制，无法直接访问 PyTorch 官方数据集镜像，导致下载中断。
### 修复方法
手动下载 MNIST 数据集文件，放入 ./data/MNIST/raw/ 目录下
或修改代码中的 root 参数，指定本地数据集路径：
```python
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
```
若下载失败，可提前下载数据集并放入对应目录，避免自动下载。
## 调试总结
本次调试过程中，核心问题集中在环境配置和模型结构匹配上。通过直接使用目标环境的 pip 安装依赖、手动切换 PyCharm 解释器、修正模型维度等方法，成功解决了所有报错，最终模型可正常训练并输出 98% 以上的测试准确率。
plaintext

---

