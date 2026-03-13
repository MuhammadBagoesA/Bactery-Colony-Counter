# Bactery Colony Counter

**Bactery Colony Counter** adalah aplikasi web sederhana yang menggunakan **YOLOv26** untuk mendeteksi dan menghitung koloni bakteri pada gambar.  

---

## Fitur Utama

- **Upload Gambar atau Gunakan Contoh**  
  Pengguna dapat mengunggah gambar koloni bakteri sendiri atau memilih contoh gambar yang tersedia.

- **Deteksi Otomatis dengan YOLOv8**  
  Model YOLO yang telah dilatih mampu mendeteksi 5 jenis bakteri:
  - B-subtilis
  - C-albicans
  - E-coli
  - P-aeruginosa
  - S-aureus

- **Visualisasi Hasil Deteksi**  
  Gambar hasil deteksi ditampilkan dengan bounding box di sekitar setiap koloni.

- **Colony Count & Statistik**  
  Menampilkan:
  - Total koloni yang terdeteksi
  - Jumlah dan persentase masing-masing jenis bakteri

- **Pengaturan Confidence Threshold**  
  Slider untuk menyesuaikan ambang deteksi (default 0.02), memberikan fleksibilitas dalam menyesuaikan sensitivitas deteksi.

- **Tampilan Interaktif & Dashboard**  
  Layout rapi menggunakan placeholder untuk hasil deteksi dan statistik, memudahkan analisis visual.

---

## Teknologi yang Digunakan

- **Python 3.14**  
- **Streamlit** – Membuat antarmuka web interaktif  
- **Ultralytics YOLOv26** – Deteksi objek koloni bakteri  
- **OpenCV & NumPy** – Manipulasi gambar dan array  
- **Pillow (PIL)** – Proses file gambar  

---

## Manfaat

- Mempercepat analisis koloni bakteri di laboratorium  
- Mengurangi kesalahan manual dalam menghitung koloni  
- Memberikan statistik lengkap untuk setiap jenis bakteri  
- Mudah digunakan oleh pengguna non-teknis  

---
