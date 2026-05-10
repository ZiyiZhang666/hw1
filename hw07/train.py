import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms
from sklearn.model_selection import train_test_split

# ====================== 超小设置 —— 速度极快 ======================
IMG_SIZE = (64, 64)
BATCH_SIZE = 16
EPOCHS = 5
DEVICE = torch.device("cpu")

# ====================== 数据预处理 ======================
transform = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# 加载数据
data_dir = "data"
train_data = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=transform)
test_data = datasets.ImageFolder(os.path.join(data_dir, "test"), transform=transform)

# 快速切分训练/验证集
train_idx, val_idx = train_test_split(list(range(len(train_data))), test_size=0.1, random_state=42)
train_loader = DataLoader(Subset(train_data, train_idx), batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(Subset(train_data, val_idx), batch_size=BATCH_SIZE, shuffle=False)
test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False)

# ====================== 超小CNN模型 —— 跑得飞快 ======================
class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.fc1 = nn.Linear(32 * 16 * 16, 64)
        self.fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = self.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# ====================== 训练 ======================
model = TinyCNN().to(DEVICE)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_losses = []
val_losses = []
train_accs = []
val_accs = []

print("开始极速训练...")
for epoch in range(EPOCHS):
    model.train()
    t_loss, t_correct = 0, 0
    for imgs, lbs in train_loader:
        imgs, lbs = imgs.to(DEVICE), lbs.to(DEVICE).float().unsqueeze(1)
        optimizer.zero_grad()
        out = model(imgs)
        loss = criterion(out, lbs)
        loss.backward()
        optimizer.step()
        t_loss += loss.item()
        t_correct += ((out > 0.5) == lbs).sum().item()

    model.eval()
    v_loss, v_correct = 0, 0
    with torch.no_grad():
        for imgs, lbs in val_loader:
            imgs, lbs = imgs.to(DEVICE), lbs.to(DEVICE).float().unsqueeze(1)
            out = model(imgs)
            v_loss += criterion(out, lbs).item()
            v_correct += ((out > 0.5) == lbs).sum().item()

    train_losses.append(t_loss / len(train_loader))
    val_losses.append(v_loss / len(val_loader))
    train_accs.append(t_correct / len(train_loader.dataset))
    val_accs.append(v_correct / len(val_loader.dataset))

    print(f"第 {epoch+1} 轮 | 训练准确率: {train_accs[-1]:.2f} | 验证准确率: {val_accs[-1]:.2f}")

# ====================== 测试集评估（作业必须要的4大指标） ======================
print("\n===== 测试集结果 =====")
all_pred = []
all_true = []
with torch.no_grad():
    for imgs, lbs in test_loader:
        imgs = imgs.to(DEVICE)
        out = model(imgs)
        pred = (out > 0.5).cpu().int().squeeze().numpy()
        all_pred.extend(pred)
        all_true.extend(lbs.numpy())

print(classification_report(all_true, all_pred, target_names=["NORMAL", "PNEUMONIA"]))

# ====================== 画图（作业必须要） ======================
plt.figure(figsize=(10,4))
plt.subplot(121)
plt.plot(train_losses, label="train loss")
plt.plot(val_losses, label="val loss")
plt.legend()

plt.subplot(122)
plt.plot(train_accs, label="train acc")
plt.plot(val_accs, label="val acc")
plt.legend()
plt.savefig("training_curves.png")
plt.close()

cm = confusion_matrix(all_true, all_pred)
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.close()

print("\n✅ 全部跑完！图表已保存！")