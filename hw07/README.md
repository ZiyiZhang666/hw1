# HW07：胸部X光肺炎二分类

## 项目简介
基于PyTorch实现的胸部X光肺炎二分类模型，可识别正常和肺炎患者的X光图像，完整实现了数据加载、模型训练、评估与结果可视化流程。

## 环境依赖
- Python 3.9
- PyTorch 1.10+
- 依赖安装命令：
  ```bash
  pip install -r requirements.txt
## 运行方式
```
python train.py
```
## 数据集说明
数据集结构：
plaintext
data/
├── train/
│   ├── NORMAL/
│   └── PNEUMONIA/
├── test/
│   ├── NORMAL/
│   └── PNEUMONIA/
└── val/
    ├── NORMAL/
    └── PNEUMONIA/
程序会自动从 train 集按 8:2 划分训练 / 验证集，解决原 val 集数据过少的问题。
## 输出结果
训练好的模型：chest_xray_cnn.pth
训练曲线与混淆矩阵：figures/ 目录
终端输出：训练日志、测试集四项评估指标