import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Air Quality Dashboard",
    layout="wide"
)

st.title("🌍 Air Quality Dashboard")
st.markdown("Dashboard kualitas udara berbasis data **AirQualityUCI** pada tahun 2004-2005")

# ======================
# LOAD DATA
# ======================
df = pd.read_excel("data/AirQualityUCI.xlsx")


df["Datetime"] = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str))
df = df.dropna()

# ======================
# KPI SECTION
# ======================
col1, col2, col3, col4 = st.columns(4)

col1.metric("📊 Total Data", len(df))
col2.metric("🌡️ Rata-rata Suhu", f"{df['T'].mean():.2f} °C")
col3.metric("💨 Rata-rata CO", f"{df['CO(GT)'].mean():.2f}")
col4.metric("🧪 Rata-rata NO2", f"{df['NO2(GT)'].mean():.2f}")

st.markdown("---")

# ======================
# CHART SECTION
# ======================
left, right = st.columns(2)

# Diagram Garis
with left:
    st.subheader("📈 Pola Perubahan Suhu")
    fig, ax = plt.subplots()
    ax.plot(df["Datetime"], df["T"])
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    st.pyplot(fig)
    st.caption(
        "Keterangan: Terlihat adanya fluktuasi suhu sepanjang waktu, "
        "yang mengindikasikan pola harian dan perubahan kondisi lingkungan."
    )

# Diagram Batang
with right:
    st.subheader("📊 Rata-rata Tingkat Polutan")
    avg_pollution = df[["CO(GT)", "NO2(GT)", "NOx(GT)"]].mean()
    avg_pollution.index.name = "Pollutant"
    fig, ax = plt.subplots()
    sns.barplot(x=avg_pollution.index, y=avg_pollution.values, ax=ax)
    ax.set_ylabel("Rata-rata")
    st.pyplot(fig)
    dominant_pollutant = avg_pollution.idxmax()
    st.caption(
        "Keterangan: NOx(GT) memiliki nilai rata-rata tertinggi, "
        "sehingga menjadi kontributor utama terhadap penurunan kualitas udara."
    )


# ======================
# PIE CHART
# ======================
st.subheader("Komposisi Polutan")
pollution_cols = ["CO(GT)", "NO2(GT)", "NOx(GT)"]

pie_data = df[pollution_cols].replace(-200, pd.NA)

pie_data = pie_data.mean().dropna()

fig, ax = plt.subplots(figsize=(2, 2))
ax.pie(
    pie_data,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=90,
    radius=0.7,      
    textprops={"fontsize": 7},  
    labeldistance=1.05,             
    pctdistance=0.65, 
    wedgeprops={"edgecolor": "white"}
)
ax.axis("equal")

st.pyplot(fig)
st.markdown(
    """
    **Keterangan:**  
    Komposisi polutan menunjukkan bahwa beberapa gas memiliki kontribusi lebih dominan, sehingga perlu menjadi fokus utama dalam upaya pengendalian kualitas udara.
    """
)



# ======================
# DATA TABLE
# ======================
st.subheader("Tampilan Awal Data Mentah")
st.dataframe(df.head(50))

# ======================
# INSIGHT SECTION
# ======================
st.subheader("Kesimpulan")

avg_temp = df["T"].mean()
avg_co = df["CO(GT)"].mean()
avg_no2 = df["NO2(GT)"].mean()

st.info(
    f"""
    🔹 **Suhu rata-rata** selama periode pengamatan adalah **{avg_temp:.2f} °C**.  
    🔹 **Kadar CO rata-rata** berada di angka **{avg_co:.2f}**, menunjukkan tingkat polusi gas karbon monoksida yang cukup konsisten.  
    🔹 **NO₂ rata-rata** sebesar **{avg_no2:.2f}**, yang berpotensi berdampak pada kualitas udara dan kesehatan.
    """
)








