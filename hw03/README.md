# hw03 人脸识别作业

## 一、项目结构
hw03/
├── src/                  # 工具模块目录
│   └── face_utils.py     # 人脸检测核心工具
├── app.py                # Streamlit Web 应用入口
├── requirements.txt      # Python 依赖清单
└── README.md             # 项目说明文档

## 二、功能说明
### 1. 核心功能
本项目实现**人脸检测功能**：
- 支持上传 JPG/PNG 格式图片
- 自动检测图片中的所有人脸位置
- 用绿色矩形框标注出所有检测到的人脸
- 实时显示检测到的人脸数量

### 2. 检测流程
1.  **图片读取**：通过 Streamlit 上传组件获取用户上传的图片
2.  **格式转换**：将 PIL 图片转换为 OpenCV 可处理的 BGR 格式
3.  **灰度处理**：将彩色图转为灰度图，提升检测效率
4.  **人脸检测**：调用 OpenCV 自带的 Haar 级联分类器 `haarcascade_frontalface_default.xml` 检测人脸
5.  **结果可视化**：在原图上绘制绿色矩形框标注人脸，并在页面展示结果

## 三、依赖与运行说明
### 1. Python 依赖
所有依赖已记录在 `requirements.txt` 中，可通过以下命令一键安装：
pip install -r requirements.txt
#### 核心依赖包括：
- streamlit：Web 应用框架，用于构建可视化界面
- opencv-python：计算机视觉库，用于人脸检测与图像处理
- pillow：图片处理库，用于读取上传的图片文件
- 其他辅助库（如 numpy、pandas 等）
### 2. 系统依赖
本项目采用 OpenCV 自带的 Haar 特征分类器，无需安装 dlib 或 face_recognition，避免了复杂的编译环境配置，可在 Windows/macOS/Linux 系统直接运行。
### 3. 运行命令
在项目根目录下打开终端，执行：
streamlit run app.py
### 4. 访问方式
运行成功后，浏览器会自动打开本地访问地址：http://localhost:8501

## 四、使用说明
- 启动服务后，在页面点击「Browse files」上传一张包含人脸的图片
- 等待系统自动检测，页面会显示检测到的人脸数量
- 查看标注了绿色人脸框的结果图片
- 可上传新图片重新检测
## 五、备注
本项目为人脸检测版本，未实现人脸识别功能，因此无需准备人脸库
若后续需扩展人脸识别功能，可引入 face_recognition 库并添加人脸特征编码与比对逻辑