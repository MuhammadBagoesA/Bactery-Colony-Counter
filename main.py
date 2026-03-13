import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import os

#model
MODEL_WEIGHTS = "weight/best1.pt"
model = YOLO(MODEL_WEIGHTS)

SAMPLE_DIR = r"sample images"

#nama kelas
class_names = ["B-subtilis", "C-albicans", "E-coli", "P-aeruginosa", "S-aureus"]
nc = len(class_names)

#sidebar
st.sidebar.header("Pengaturan Deteksi")

conf_threshold = st.sidebar.slider(
    "Confidence Threshold",
    0.0,
    1.0,
    0.02,   # default
    0.01
)

#title
st.title("Bactery Colony Counter")
st.write("by : Muhammad Bagoes Anargiansyah")
st.write("Upload gambar atau gunakan contoh gambar untuk menghitung koloni bakteri.")

#display
st.divider()

col1, col2 = st.columns([3,1])

with col1:
    image_placeholder = st.empty()

with col2:
    count_placeholder = st.empty()
    stats_placeholder = st.empty()

image_placeholder.info("Belum ada gambar yang dianalisis")
count_placeholder.metric("Total Colony", 0)
stats_placeholder.write("Statistik bakteri akan muncul di sini...")

st.divider()

#fungsi menampilkan deteksi
def run_detection(img):

    results = model(img, conf=conf_threshold)

    annotated_frame = results[0].plot()
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    boxes = results[0].boxes
    colony_count = len(boxes)

    #update gambar hasil deteksi
    image_placeholder.image(
        annotated_frame,
        caption="Hasil Deteksi Koloni",
        width="stretch"
    )

    #update total colony
    count_placeholder.metric("Total Colony", colony_count)

    #update statistik per kelas
    stats_placeholder.empty()

    if colony_count > 0:
        classes = boxes.cls.cpu().numpy()
        unique_classes, counts = np.unique(classes, return_counts=True)

        stats_md = ""
        for cls, count in zip(unique_classes, counts):
            percentage = (count / colony_count) * 100
            name = class_names[int(cls)] if int(cls) < nc else f"Class {int(cls)}"
            stats_md += f"**{name}**\n\n"
            stats_md += f"- Jumlah : {count}\n"
            stats_md += f"- Persentase : {percentage:.2f}%\n\n---\n\n"

        stats_placeholder.markdown(stats_md)
    else:
        stats_placeholder.write("Tidak ada bakteri yang terdeteksi.")

#upload gambar
st.subheader("Upload Gambar")

uploaded_file = st.file_uploader(
    "Upload gambar...",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    run_detection(img)


#sample
st.subheader("Contoh Gambar")

sample_images = []

if os.path.exists(SAMPLE_DIR):
    for file in os.listdir(SAMPLE_DIR):
        if file.endswith(("jpg","jpeg","png")):
            sample_images.append(os.path.join(SAMPLE_DIR, file))

cols = st.columns(3)

for i, img_path in enumerate(sample_images):

    with cols[i % 3]:

        image = Image.open(img_path)

        st.image(
            image,
            caption=os.path.basename(img_path),
            width="stretch"
        )

        if st.button("Gunakan gambar ini", key=img_path):

            img = np.array(image)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            run_detection(img)