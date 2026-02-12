import streamlit as st
import pandas as pd
import random

st.sidebar.title("📊 Menu Aplikasi")
st.sidebar.markdown("---")

st.title("🤖 Prediksi Topik")

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

if "processed_data" not in st.session_state:
    st.warning("Lakukan preprocessing terlebih dahulu!")
    st.stop()

df = st.session_state["processed_data"].copy()

label_map = {
    0: "Lifestyle",
    1: "Skincare",
    2: "Entertainment",
    3: "Gaming",
    4: "Education"
}

if st.button("Proses Prediksi"):

    import numpy as np

    pred_labels = []
    confidences = []

    for _ in range(len(df)):

        # probabilitas acak
        probs = np.random.dirichlet(np.ones(5))

        label = np.argmax(probs)
        confidence = probs[label]

        pred_labels.append(label)
        confidences.append(confidence)

    df["prediksi"] = pred_labels
    df["kategori"] = df["prediksi"].map(label_map)
    df["confidence"] = confidences  # simpan float untuk progress bar

    st.session_state["data_prediksi"] = df

    st.success("Prediksi selesai!")

    st.dataframe(
        df[["clean_text", "prediksi", "kategori", "confidence"]]
        .head(20),
        column_config={
            "confidence": st.column_config.ProgressColumn(
                "Confidence",
                min_value=0,
                max_value=1,
            )
        }
    )

st.markdown("---")

if st.button("📊 Lihat Analisis Tren", use_container_width=True):
    st.switch_page("pages/4_Analisis_Tren.py")






