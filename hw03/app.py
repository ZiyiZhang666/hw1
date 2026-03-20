import streamlit as st
import cv2
import numpy as np
from PIL import Image
from src.face_utils import detect_faces, draw_boxes

st.title("hw03 人脸识别作业")
uploaded_file = st.file_uploader("上传图片", type=["jpg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_np = np.array(img)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    faces = detect_faces(img_bgr)
    st.write(f"检测到 {len(faces)} 张人脸")

    result_img = draw_boxes(img_bgr, faces)
    result_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

    st.image(result_rgb, caption="检测结果")