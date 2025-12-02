import streamlit as st

# KONFIGURASI DASHBOARD
st.set_page_config(
    page_title="Dashboard Analisis Data",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #183B4E;
    }
    [data-testid="stSidebar"] * {
        color: white;
    }
    [data-testid="stHeader"] {
        background-color: #FFD54F; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HALAMAN UTAMA
home = st.Page("home.py", title="Beranda", icon=":material/home:")
informasi = st.Page("informasi.py", title="Informasi Pajak", icon=":material/info:")
analisis_visual = st.Page("visualisasi.py", title="Visualisasi Data", icon=":material/monitoring:")
profil = st.Page("profil.py", title="Profil Pencipta", icon=":material/account_circle:")

# Navigasi utama
pg = st.navigation([home, informasi, analisis_visual, profil])
pg.run()

