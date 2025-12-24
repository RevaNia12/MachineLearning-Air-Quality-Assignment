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
st.markdown("Dashboard kualitas udara berbasis data **AirQualityUCI**")

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
col2.metric("🌡️ Avg Temperature", f"{df['T'].mean():.2f} °C")
col3.metric("💨 Avg CO", f"{df['CO(GT)'].mean():.2f}")
col4.metric("🧪 Avg NO2", f"{df['NO2(GT)'].mean():.2f}")

st.markdown("---")

# ======================
# CHART SECTION
# ======================
left, right = st.columns(2)

# LINE CHART
with left:
    st.subheader("📈 Temperature Trend")
    fig, ax = plt.subplots()
    ax.plot(df["Datetime"], df["T"])
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    st.pyplot(fig)

# BAR CHART
with right:
    st.subheader("📊 Average Pollutant Levels")
    avg_pollution = df[["CO(GT)", "NO2(GT)", "NOx(GT)"]].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=avg_pollution.index, y=avg_pollution.values, ax=ax)
    ax.set_ylabel("Average Value")
    st.pyplot(fig)

st.markdown("---")

# ======================
# PIE CHART
# ======================
st.subheader("Pollution Composition")
pollution_cols = ["CO(GT)", "NO2(GT)", "NOx(GT)"]

pie_data = df[pollution_cols].replace(-200, pd.NA)

pie_data = pie_data.mean().dropna()

fig, ax = plt.subplots(figsize=(2, 2))
ax.pie(
    pie_data,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=90,
    radius=0.5,
    textprops={"fontsize": 7},                    
    wedgeprops={"edgecolor": "white"}
)
ax.axis("equal")

st.pyplot(fig)


# ======================
# DATA TABLE
# ======================
st.subheader("📄 Raw Data Preview")
st.dataframe(df.head(50))
