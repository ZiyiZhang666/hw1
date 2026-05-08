# 深度学习作业：MNIST 手写数字识别（CNN + LeNet-5）

## 一、项目简介
本项目基于 PyTorch 深度学习框架，完成 MNIST 手写数字识别任务，包含**基础卷积神经网络**与**经典 LeNet-5 网络**的实现、训练、测试与调试。

项目包含：
- 任务一：简单卷积神经网络（Simple CNN）
- 任务二：LeNet-5 经典卷积神经网络
- 完整调试记录
- 模型训练与测试结果

---

## 二、运行环境
- Python 3.9
- PyTorch（CPU 版本）
- Matplotlib
- NumPy

---

## 三、文件结构
hw05/ ├── task1_2_simple_cnn.py # 任务一：简单 CNN 实现├── task1_3_lenet5.py # 任务二：LeNet-5 实现├── debug_notes.md # 代码调试与问题解决记录├── report.md # 实验报告（结构、结果、分析）├── requirements.txt # 项目依赖库├── lenet5_mnist.pth # LeNet-5 训练好的模型└── simple_cnn_mnist.pth # 简单 CNN 训练好的模型
plaintext

---

## 四、依赖安装
在终端执行以下命令安装所有依赖：
```bash
pip install -r requirements.txt
```
## 运行方法
1. 运行任务一（简单 CNN）
```
python task1_2_simple_cnn.py
```
2. 运行任务二（LeNet-5）
``` 
python task1_3_lenet5.py
```
## 六、数据集说明
程序运行时会自动下载 MNIST 数据集到 ./data 目录，无需手动下载与处理。
## 七、模型说明
### 任务一：简单 CNN
- 1 个卷积层
- 1 个池化层
- 1 个全连接层
- 测试集准确率：约 98%+
###任务二：LeNet-5
- 2 个卷积层
- 2 个平均池化层
- 3 个全连接层
- Sigmoid 激活函数
- 测试集准确率：约 98.5%~99%
## 八、输出结果
运行代码后会输出：
- 每轮训练损失
- 测试集准确率
- 训练好的模型文件（.pth）
- 数据可视化图片（样本、预测、损失曲线）

## 九、调试说明
所有运行过程中遇到的环境问题、依赖问题、模型错误及解决方案，均记录在 debug_notes.md 中。
