import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("📊 Menu Aplikasi")
st.sidebar.markdown("---")

st.title("📊 Analisis Tren")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #429E9D;  /* ganti warna sesuai selera */
}

[data-testid="stSidebar"] * {
    color: white;  /* warna teks sidebar */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(45deg, #3B82F6, #10B981);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(45deg, #2563EB, #059669);
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* background utama */
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #d1fae5);
}

/* optional: card container terasa mengambang */
.block-container {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* background seluruh app */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #ccfbf1);
}

/* container utama konten */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

/* area konten */
.block-container {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)

if "data_prediksi" not in st.session_state:
    st.warning("Lakukan prediksi terlebih dahulu!")
    st.stop()

df = st.session_state["data_prediksi"]

trend_counts = df["kategori"].value_counts()

col1, col2, col3 = st.columns(3)

col1.metric("Total Data", len(df))
col2.metric("Kategori Dominan", trend_counts.idxmax())
col3.metric("Jumlah Kategori", trend_counts.size)


st.subheader("Data Hasil Prediksi")
st.dataframe(df[["clean_text", "kategori"]])

# ===== Hitung tren =====
trend = df["kategori"].value_counts().reset_index()
trend.columns = ["Kategori", "Jumlah"]

trend["Persentase"] = (trend["Jumlah"] / trend["Jumlah"].sum()) * 100
trend["Persentase"] = trend["Persentase"].round(2).astype(str) + " %"


col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Tabel Tren")
    st.dataframe(trend, use_container_width=True)

with col2:
    st.subheader("📊 Grafik Tren")

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(trend["Kategori"], trend["Jumlah"])
    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Kategori")

    st.pyplot(fig)


st.info(
    f"Kategori paling dominan adalah **{trend_counts.idxmax()}** "
    f"dengan total {trend_counts.max()} data."
)

selected = st.selectbox(
    "🔍 Lihat detail kategori:",
    df["kategori"].unique()
)

filtered = df[df["kategori"] == selected]

display_cols = ["clean_text", "prediksi", "kategori", "confidence"]

st.dataframe(
    filtered[display_cols].head(20),
    column_config={
        "confidence": st.column_config.ProgressColumn(
            "Confidence",
            min_value=0,
            max_value=1,
        )
    },
    use_container_width=True
)



st.pyplot(fig, use_container_width=False)



