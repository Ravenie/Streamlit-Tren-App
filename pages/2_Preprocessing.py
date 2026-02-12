import streamlit as st
import pandas as pd
import re

st.sidebar.title("📊 Menu Aplikasi")
st.sidebar.markdown("---")

st.title("Preprocessing Data")

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

# ========================
# CEK DATA SESSION
# ========================
if "data" not in st.session_state:
    st.warning("Silakan upload data terlebih dahulu di halaman Input Data")
    st.stop()

df = st.session_state["data"]
text_col = st.session_state["text_column"]

st.subheader("Preview Data Awal")
st.dataframe(df.head())

# ========================
# CASE FOLDING
# ========================
st.subheader("1️⃣ Case Folding")

df["case_folding"] = df[text_col].astype(str).str.lower()

before_after_cf = pd.DataFrame({
    "Before": df[text_col].head(5),
    "After": df["case_folding"].head(5)
})

st.dataframe(before_after_cf)

# ========================
# TEXT CLEANSING
# ========================
st.subheader("2️⃣ Text Cleansing")

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["cleaning"] = df["case_folding"].apply(clean_text)

before_after_clean = pd.DataFrame({
    "Before": df["case_folding"].head(5),
    "After": df["cleaning"].head(5)
})

st.dataframe(before_after_clean)

# ========================
# NORMALIZATION (contoh sederhana)
# ========================
st.subheader("3️⃣ Normalization")

kamus_normalisasi = {
    "yg": "yang",
    "gk": "tidak",
    "ga": "tidak",
    "tdk": "tidak",
    "dr": "dari"
}

def normalize(text):
    words = text.split()
    normalized = [kamus_normalisasi.get(w, w) for w in words]
    return " ".join(normalized)

df["normalized"] = df["cleaning"].apply(normalize)

before_after_norm = pd.DataFrame({
    "Before": df["cleaning"].head(5),
    "After": df["normalized"].head(5)
})

st.dataframe(before_after_norm)

# ========================
# TOKENIZATION
# ========================
st.subheader("4️⃣ Tokenization")

df["tokens"] = df["normalized"].apply(lambda x: x.split())

before_after_token = pd.DataFrame({
    "Before": df["normalized"].head(5),
    "After": df["tokens"].head(5)
})

st.dataframe(before_after_token)

# ========================
# HASIL FINAL CLEAN TEXT
# ========================
st.subheader("✅ Hasil Clean Text Final")

df["clean_text"] = df["normalized"]

st.dataframe(df[["clean_text"]].head(10))

# Simpan ke session untuk prediksi
st.session_state["processed_data"] = df

st.markdown("---")

if st.button("🔎 Lihat Hasil Prediksi", use_container_width=True):
    st.switch_page("pages/3_Prediksi.py")
