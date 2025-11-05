import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Beranda")
st.write("Selamat datang di dashboard KPP Pratama Surabaya Rungkut!")

st.markdown(
    """
    <div style="
        background-color:#183B4E;
        padding:15px;
        color:white;
        border-radius:10px;
        margin-bottom:20px;
    ">
    Dashboard ini merupakan hasil kerja praktik tim 2025_02_014 sebagai bagian dari tujuan khusus kegiatan, 
    yaitu merancang dashboard interaktif yang berisi informasi umum, data pajak, analisis data, 
    dan profil yang disajikan secara ringkas untuk umum.
    </div>
    """, 
    unsafe_allow_html=True
)

# Tentang KPP
st.markdown(
    """
    <style>
        .about-container {
            background-color: #e0e0e0;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }
        .about-container h3 {
            color: black;
            margin-bottom: px;
            text-align: center;
        }
        .about-container img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .about-container p {
            font-size: 15px;
            color: black;
            line-height: 1.6;
            text-align: justify;
        }
    </style>

    <div class="about-container">
        <h3>Tentang KPP Pratama Surabaya Rungkut</h3>
        <figure>
            <img src="https://www.pajak.go.id/sites/default/files/styles/large/public/2022-07/Alamat-%26-Nomor-Telepon-Kantor-Pajak-Kota-Surabaya.jpg?itok=ZUhDwT_G" width="400">
            <figcaption style="font-size:12px; color: black; text-align:center;">
                Kantor Pelayanan Pajak Pratama Surabaya Rungkut
            </figcaption>
        </figure>
        <p>
            Kantor Pelayanan Pajak (KPP) Pratama Surabaya Rungkut merupakan unit vertikal Direktorat Jenderal Pajak 
            di bawah Kementerian Keuangan. KPP ini melaksanakan fungsi penyuluhan, pelayanan, dan pengawasan perpajakan
            untuk beberapa wilayah administrasi di Surabaya. KPP Pratama Surabaya Rungkut memiliki fokus wilayah administrasi dalam kerjanya, 
            antara lain: Kecamatan Rungkut, Gunung Anyar, Tenggilis Mejoyo. 
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Peta
st.markdown(
    "<h3 style='text-align: center;'>Peta Kecamatan Surabaya</h3>",
    unsafe_allow_html=True
)

kelurahan_coords = {
    "Rungkut": {
        "Kali Rungkut": [-7.3189, 112.7850],
        "Kedung Baruk": [-7.3197, 112.7643],
        "Medokan Ayu": [-7.3322, 112.7990],
        "Penjaringan Sari": [-7.3280, 112.7790],
        "Rungkut Kidul": [-7.3285, 112.7889],
        "Wonorejo": [-7.3433, 112.8140],
    },
    "Tenggilis Mejoyo": {
        "Kendangsari": [-7.3258, 112.7587],
        "Kutisari": [-7.3225, 112.7462],
        "Panjang Jiwo": [-7.3195, 112.7764],
        "Tenggilis Mejoyo": [-7.3178, 112.7640],
    },
    "Gunung Anyar": {
        "Gunung Anyar": [-7.3458, 112.7986],
        "Gunung Anyar Tambak": [-7.3550, 112.8175],
        "Rungkut Menanggal": [-7.3279, 112.7405],
        "Rungkut Tengah": [-7.3256, 112.7700],
    }
}

# Membuat peta
m = folium.Map(location=[-7.3213, 112.7870], zoom_start=13)

# Marker untuk tiap kelurahan
colors = {"Rungkut": "blue", "Tenggilis Mejoyo": "green", "Gunung Anyar": "red"}

for kecamatan, data_kel in kelurahan_coords.items():
    for kel, coord in data_kel.items():
        folium.Marker(
            location=coord,
            popup=f"{kel} ({kecamatan})",
            icon=folium.Icon(color=colors[kecamatan], icon="info-sign"),
        ).add_to(m)

# Layout 
col1, col2, col3 = st.columns([1, 3, 1])  

with col2:
    st_folium(m, width=800, height=400)

# Informasi Penerimaan Pajak
st.markdown(
    """
    <div style="
        background-color:#eaeaea;
        padding:20px;
        font-size:15px;
        border-radius:10px;
        margin-bottom:20px;
        text-align: justify;
    ">
    Berikut adalah informasi mengenai penerimaan pajak yang dikelola oleh KPP Pratama Surabaya Rungkut,
    yang mencakup PPN, PPh, dan jumlah tindakan penagihan. Data ini diambil secara resmi dari permohonan ke seksi terkait.
    Informasi di bawah mencakup data dari tahun 2018 hingga 2024.   
    </div>
    """, 
    unsafe_allow_html=True
)

# Data pajak
ppn_df = pd.read_csv(
    "https://drive.google.com/uc?id=1aNDOgTKy6DSBl0nQzll2HVdVsXsn3rcu",
    sep=",",
    encoding="utf-8",
    engine="python"
)

pph21_df = pd.read_csv(
    "https://drive.google.com/uc?id=1hyx1nKPJyz1RrGbVS_O_FnVYE6anu-G1",
    sep=",",
    encoding="utf-8",
    engine="python"
)

pph22_df = pd.read_csv(
    "https://drive.google.com/uc?id=1_hAv0Qu5dLDOPVYLiKaeihSMZdtccbsH",
    sep=",",
    encoding="utf-8",
    engine="python"
)

pph23_df = pd.read_csv(
    "https://drive.google.com/uc?id=1riuGy70Ak4jgH4b5pbL_Im_VWYzC04df",
    sep=",",
    encoding="utf-8",
    engine="python"
)

df = pd.DataFrame({
    "tahun": ppn_df["Tahun"],
    "bulan": ppn_df["Bulan"],
    "ppn": ppn_df["PPN"],
    "pph21": pph21_df["PPh21"],
    "pph22": pph22_df["PPh22"],
    "pph23": pph23_df["PPh23"]
})

# Filter Pilihan Tahun & Bulan 
th, bln = st.columns(2)

with th:
    tahun = st.selectbox("Pilih Tahun", sorted(df["tahun"].unique()))

with bln:
    bulan = st.selectbox("Pilih Bulan", sorted(df[df["tahun"] == tahun]["bulan"].unique()))

# Ambil data current & previous 
current = df[(df["tahun"] == tahun) & (df["bulan"] == bulan)].iloc[0]

prev_index = df.index[(df["tahun"] == tahun) & (df["bulan"] == bulan)].tolist()[0] - 1
if prev_index >= 0:
    prev = df.iloc[prev_index]
else:
    prev = None

# Fungsi Growth
def growth(curr, prev):
    if prev is None or prev == 0:
        return 0
    return ((curr - prev) / prev) * 100

ppn_growth = growth(current["ppn"], prev["ppn"] if prev is not None else None)
pph21_growth = growth(current["pph21"], prev["pph21"] if prev is not None else None)
pph22_growth = growth(current["pph22"], prev["pph22"] if prev is not None else None)
pph23_growth = growth(current["pph23"], prev["pph23"] if prev is not None else None)

# Fungsi format rupiah
def format_rupiah_singkat(nilai):
    if nilai >= 1_000_000_000_000:
        return f"Rp {nilai/1_000_000_000_000:.2f} T"
    elif nilai >= 1_000_000_000:
        return f"Rp {nilai/1_000_000_000:.2f} M"
    elif nilai >= 1_000_000:
        return f"Rp {nilai/1_000_000:.2f} Jt"
    else:
        return f"Rp {nilai:,.0f}".replace(",", ".")

# Tampilan
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div style="background-color: #eaeaea; padding:5px; border-radius:10px; text-align:center; box-shadow:7px 5px 8px rgba(255, 255, 224, 0.6);">
            <h4>Penerimaan PPN</h4>
            <h3 style="color:#183B4E; margin:5px 0; font-size:20px;">{format_rupiah_singkat(current['ppn'])}</h3>
            <p style="margin:0; font-size:12px; color:#555;">Growth Rate (Bulan)</p>
            <p style="color:{'green' if ppn_growth>=0 else 'red'}; margin:0; font-weight:bold;">
                {'⬆' if ppn_growth>=0 else '⬇'} {ppn_growth:.1f}%
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color:#eaeaea; padding:5px; border-radius:10px; text-align:center; box-shadow:7px 5px 8px rgba(0,0,0,0.1);">
            <h4>Penerimaan PPh 21</h4>
            <h3 style="color:#183B4E; margin:5px 0; font-size:20px;">{format_rupiah_singkat(current['pph21'])}</h3>
            <p style="margin:0; font-size:12px; color:#555;">Growth Rate (Bulan)</p>
            <p style="color:{'green' if pph21_growth>=0 else 'red'}; margin:0;">
                {'⬆' if pph21_growth>=0 else '⬇'} {pph21_growth:.1f}%
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="background-color:#eaeaea; padding:5px; border-radius:10px; text-align:center; box-shadow:7px 5px 8px rgba(0,0,0,0.1);">
            <h4>Penerimaan PPh 22</h4>
            <h3 style="color:#183B4E; margin:5px 0; font-size:20px;">{format_rupiah_singkat(current['pph22'])}</h3>
            <p style="margin:0; font-size:12px; color:#555;">Growth Rate (Bulan)</p>
            <p style="color:{'green' if pph22_growth>=0 else 'red'}; margin:0;">
                {'⬆' if pph22_growth>=0 else '⬇'} {pph22_growth:.1f}%
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div style="background-color:#eaeaea; padding:5px; border-radius:10px; text-align:center; box-shadow:7px 5px 8px rgba(0,0,0,0.1);">
            <h4>Penerimaan PPh 23</h4>
            <h3 style="color:#183B4E; margin:5px 0; font-size:20px;">{format_rupiah_singkat(current['pph23'])}</h3>
            <p style="margin:0; font-size:12px; color:#555;">Growth Rate (Bulan)</p>
            <p style="color:{'green' if pph23_growth>=0 else 'red'}; margin:0;">
                {'⬆' if pph23_growth>=0 else '⬇'} {pph23_growth:.1f}%
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Informasi KPP di bawah
st.markdown(
    """
    <style>
        .footer-container {
            display: flex;
            justify-content: space-between; 
            align-items: center;      
            background-color: #eaeaea;
            border-top: 3px solid #ddd;  
            padding: 20px 20px;
            border-radius: 10px;
            margin-top: 50px;
            box-shadow: 0px -2px 10px rgba(0,0,0,0.1);
        }
        .footer-right {
            font-size: 13px;
            color: black;
            text-align: right;
        }
        .social-icons {
            margin-top: 10px;
            text-align: right;
        }
        .social-icons a {
            margin: 0 5px;
            text-decoration: none;
        }
        .social-icons img {
            width: 16px;
            height: 16px;
            transition: transform 0.2s;
        }
        .social-icons img:hover {
            transform: scale(1.2);
        }
    </style>

    <div class="footer-container">
        <div class="footer-left">
            <img src="https://static.pajak.go.id/assets/media/logos/Logo%20DJP.png" width="300" style="margin-bottom:10px;">
        </div>
        <div class="footer-right">
            Jl Jagir Wonokromo No. 104, Surabaya, Indonesia <br>
            Kantor Pelayanan Pajak Pratama Surabaya Rungkut <br>
            Phone: 031-8483198, 8483196 <br>
            E-mail: kpp.615@pajak.go.id <br>
            Fax: 031-8483197
            <div class="social-icons">
                <p style="margin-top:30px; margin-bottom:2px; font-size:15px; font-weight:bold;">Follow Us:</p>
                <a href="https://www.instagram.com/pajaksbyrungkut" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png">
                </a>
                <a href="https://twitter.com/pajaksbyrungkut" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png">
                </a>
                <a href="https://wa.me/6289622615615" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png">
                </a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

