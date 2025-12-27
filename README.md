# Air Quality Data Analysis for Decision Making

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data secara end-to-end menggunakan **Air Quality Dataset**.
Analisis dilakukan mulai dari data preparation, exploratory data analysis (EDA), dan penyampaian insight
melalui visualisasi data. Proyek ini dibuat untuk memenuhi tugas submission **Machine Learning Assignment** oleh GDGoC.

## Dataset
Dataset yang digunakan adalah **Air Quality Dataset**, yang berisi informasi mengenai:
- Konsentrasi polutan udara (CO, NO2, NOx, dll)
- Data sensor kualitas udara
- Variabel cuaca seperti suhu, kelembapan absolut, dan kelembapan relatif

## Tools & Library
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit 

## Struktur Folder
   - data
     * AirQualityUCI.xlsx
   - Notebook.ipynb
   - dashboard.py
   - requirements.txt
   - README.md

 ## Cara Menjalankan Proyek
 ### 1. Install dependency
Pastikan Python sudah terpasang, lalu jalankan:
pip install -r requirements.txt
### 2. Menjalankan Notebook
Buka file Notebook.ipynb menggunakan jupyter notebook untuk melihat proses analisis dan eksplorasi data.
### 3. Menjalankan Dashboard Streamlit
streamlit run dashboard.py
Dashboard akan terbuka di browser lokal dan menampilkan visualisasi dari dataset.

## Insight Utama

- Suhu udara memiliki korelasi positif dengan beberapa polutan seperti CO dan NO2.
- Kelembapan relatif (RH) memiliki korelasi negatif yang kuat terhadap suhu.
- Faktor cuaca berperan penting dalam dinamika kualitas udara.

## Kesimpulan

Proyek ini menunjukkan proses end-to-end data analysis, mulai dari data mentah hingga penyampaian
insight melalui dashboard. Visualisasi data dan EDA membantu memahami pola serta hubungan antar variabel
untuk mendukung pengambilan keputusan berbasis data.

## Dokumentasi Dashboard
<img width="1878" height="864" alt="Screenshot 2025-12-27 163821" src="https://github.com/user-attachments/assets/50758f0c-1500-4b80-afbd-cde84cdf72d7" />




