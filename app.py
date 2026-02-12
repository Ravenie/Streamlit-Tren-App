import streamlit as st

st.sidebar.title("📊 Menu Aplikasi")
st.sidebar.markdown("---")

st.set_page_config(
    page_title="Analisis Tren TikTok",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

st.title("📊 Sistem Analisis Tren Pengguna TikTok")
st.markdown("---")

st.write("""
Aplikasi ini merupakan sistem berbasis web yang digunakan untuk menganalisis tren topik
pada pengguna TikTok menggunakan metode klasifikasi berbasis **BERT**.

### 🔎 Fitur Utama:
- Upload dataset TikTok (CSV/XLSX)
- Preprocessing teks otomatis
- Klasifikasi topik menggunakan BERT
- Analisis tren kategori
- Visualisasi grafik tren

### 📌 Alur Penggunaan:
1. Upload dataset
2. Lakukan preprocessing
3. Jalankan prediksi
4. Lihat hasil tren

Gunakan menu di sidebar untuk memulai atau tekan tombol untuk memulai
""")

if st.button("🚀 Start Analisis", use_container_width=True):
    st.switch_page("pages/1_Input_Data.py")
