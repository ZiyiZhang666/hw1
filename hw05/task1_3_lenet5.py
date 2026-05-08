import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# ====================== 1. 定义 LeNet-5 模型 ======================
class LeNet5(nn.Module):
    """
    经典 LeNet-5 结构适配 MNIST 手写数字识别
    输入：单通道 28x28 灰度图
    输出：10 个类别
    """
    def __init__(self):
        super(LeNet5, self).__init__()
        # 卷积层 1: 输入 1 通道，输出 6 通道，5x5 卷积核
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)
        self.pool1 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.sigmoid1 = nn.Sigmoid()

        # 卷积层 2: 输入 6 通道，输出 16 通道，5x5 卷积核
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
        self.pool2 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.sigmoid2 = nn.Sigmoid()

        # 全连接层 1: 16*5*5 -> 120
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.sigmoid3 = nn.Sigmoid()

        # 全连接层 2: 120 -> 84
        self.fc2 = nn.Linear(120, 84)
        self.sigmoid4 = nn.Sigmoid()

        # 输出层: 84 -> 10
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 第一层
        x = self.pool1(self.sigmoid1(self.conv1(x)))
        # 第二层
        x = self.pool2(self.sigmoid2(self.conv2(x)))
        # 展平
        x = x.view(-1, 16 * 5 * 5)
        # 全连接层
        x = self.sigmoid3(self.fc1(x))
        x = self.sigmoid4(self.fc2(x))
        x = self.fc3(x)
        return x

# ====================== 2. 数据加载 ======================
def load_data(batch_size=64):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = torchvision.datasets.MNIST(
        root='./data', train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=transform
    )

    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True
    )
    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False
    )
    return train_loader, test_loader

# ====================== 3. 训练函数 ======================
def train(model, train_loader, criterion, optimizer, device, epochs=10):
    model.train()
    train_losses = []
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        epoch_loss = running_loss / len(train_loader)
        train_losses.append(epoch_loss)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
    return train_losses

# ====================== 4. 测试函数 ======================
def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    test_loss /= len(test_loader)
    accuracy = 100 * correct / total
    print(f"Test Loss: {test_loss:.4f}, Accuracy: {accuracy:.2f}%")
    return test_loss, accuracy

# ====================== 5. 主函数 ======================
def main():
    # 超参数设置
    batch_size = 64
    epochs = 10
    lr = 0.001

    # 设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    # 数据
    train_loader, test_loader = load_data(batch_size)

    # 模型
    model = LeNet5().to(device)
    print(model)

    # 损失函数与优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # 训练
    print("开始训练 LeNet-5...")
    train_losses = train(model, train_loader, criterion, optimizer, device, epochs)

    # 测试
    print("开始测试...")
    test_loss, test_acc = test(model, test_loader, criterion, device)

    # 保存模型
    torch.save(model.state_dict(), 'lenet5_mnist.pth')
    print("模型已保存为 lenet5_mnist.pth")

if __name__ == "__main__":
    main()