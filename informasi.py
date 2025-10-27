import streamlit as st
import plotly.graph_objects as go

st.title("Informasi Pajak")
tabs = st.tabs(["Dasar Pajak", "Alur Penagihan Pajak", "Panduan & Referensi"])

# TAB 1 – Dasar Pajak
with tabs[0]:
    st.markdown("<h3 style='text-align: center; font-size: 35px; margin-top:10px; margin-bottom: 10px'>Definisi</h3>", unsafe_allow_html=True)

    # Definisi Pajak & WP 
    st.markdown(
        """
        <style>
        .equal-col {
            display: flex;
            flex-direction: row;
            gap: 20px;
        }
        .equal-box {
            flex: 1;
            background-color: #F0F4FF;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="equal-col">
            <div class="equal-box">
                <h3 style="font-size: 20px">Pajak</h3>
                <p>Berdasarkan UU No. 28 Tahun 2007, Pajak adalah kontribusi wajib kepada negara yang terutang oleh orang pribadi atau badan,
                yang bersifat memaksa berdasarkan undang-undang, tanpa mendapatkan imbalan secara langsung,
                dan digunakan untuk keperluan negara bagi sebesar-besarnya kemakmuran rakyat.</p>
            </div>
            <div class="equal-box">
                <h3 style="font-size: 20px">Wajib Pajak (WP)</h3>
                <p>Berdasarkan Undang-Undang Nomor 28 Tahun 2007, Wajib Pajak adalah orang pribadi atau badan, meliputi pembayar pajak, pemotong pajak,
                dan pemungut pajak, yang mempunyai hak dan kewajiban perpajakan sesuai dengan
                ketentuan peraturan perundang-undangan.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Kategori Utama Pajak 
    st.markdown("<h3 style='text-align: center; font-size: 35px; margin-top:20px; margin-bottom: 20px'>Kategori Utama Pajak</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .kategori-col {
            display: flex;
            flex-direction: row;
            gap: 15px;
        }
        .kategori-box {
            flex: 1;
            background-color:#F0F4FF;
            padding:15px;
            border-radius:10px;
            margin-bottom:15px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="kategori-col">
            <div class="kategori-box">
                <b>Pajak Pusat</b><br>
                Dipungut pemerintah pusat, misalnya PPh dan PPN.
            </div>
            <div class="kategori-box">
                <b>Pajak Daerah</b><br>
                Dipungut pemerintah daerah, misalnya Pajak Kendaraan, Hotel, Restoran.
            </div>
            <div class="kategori-box">
                <b>Bea dan Cukai</b><br>
                Pungutan atas kegiatan impor/ekspor serta barang tertentu (rokok, alkohol).
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Jenis Pajak Pusat
    st.markdown("<h3 style='text-align:center; font-size:30px; margin-top:20px; margin-bottom: 20px'>Jenis Pajak Pusat</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .equal-col-jenis{
            display:flex;
            gap:20px;
            align-items:stretch;
            flex-wrap:nowrap;
        }
        .equal-box-jenis{
            flex:1;
            display:flex;
            flex-direction:column;
            gap:20px;
        }
        .jenis-item{
            background-color:#F0F4FF;
            padding:16px 18px;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.06);
            line-height:1.5;
            height:auto;           
            min-height:120px;         
            word-break:break-word;   
            overflow-wrap:anywhere;  
        }
        .jenis-item b{
            display:block;
            margin-bottom:6px;
        }
        @media (max-width: 900px){
            .equal-col-jenis{flex-wrap:wrap;}
        }
        </style>

        <div class="equal-col-jenis">
            <div class="equal-box-jenis">
                <div class="jenis-item">
                    <b>Pajak Pertambahan Nilai (PPN)</b>
                    Berdasarkan Undang-Undang Nomor 8 Tahun 1998, Pajak Pertambahan Nilai adalah pajak
                    yang dikenakan atas konsumsi Barang Kena Pajak (BKP) dan Jasa Kena Pajak (JKP)
                    di dalam Daerah Pabean yang dilakukan oleh Pengusaha Kena Pajak (PKP).
                </div>
                <div class="jenis-item">
                    <b>Pajak Penghasilan (PPh) Pasal 21</b>
                    PPh Pasal 21 adalah pemotongan pajak atas penghasilan sehubungan dengan pekerjaan,
                    jasa, atau kegiatan yang diterima Wajib Pajak orang pribadi dalam negeri. Pemotongan
                    dilakukan oleh pemberi kerja, bendahara pemerintah, dana pensiun, badan, perusahaan,
                    atau penyelenggara kegiatan.
                </div>
            </div>
            <div class="equal-box-jenis">
                <div class="jenis-item">
                    <b>Pajak Penghasilan (PPh) Pasal 22</b>
                    Berdasarkan Pasal 22 Undang-Undang Nomor 36 Tahun 2008, PPh Pasal 22 adalah pajak
                    yang dikenakan pada transaksi tertentu dan dipungut oleh bendahara pemerintah,
                    badan usaha tertentu, atau Wajib Pajak badan tertentu dalam kegiatan impor,
                    penyerahan barang, serta penjualan barang mewah.
                </div>
                <div class="jenis-item">
                    <b>Pajak Penghasilan (PPh) Pasal 23</b>
                    PPh Pasal 23 adalah pemotongan atas penghasilan berupa hadiah, bunga, dividen,
                    sewa, royalti, dan jasa-jasa lainnya selain objek PPh Pasal 21. Pemotongan dilakukan
                    pada saat pembayaran, disediakan untuk dibayar, atau saat jatuh tempo pembayaran.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# TAB 2 – Alur Penagihan Pajak
# TAB 2 – Alur Penagihan Pajak
with tabs[1]:
    stages = [
        "Utang Pajak", "Jatuh Tempo Pembayaran", "Surat Teguran", "Surat Paksa",
        "Penyitaan", "Pengumuman Lelang", "Pelaksanaan Lelang"
    ]
    durations = ["1 bulan", "7 hari", "21 hari", "2x24 jam", "14 hari", "14 hari", " "]

    x = list(range(len(stages)))
    y = [0] * len(stages)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="lines",
        line=dict(color="lightgrey", width=3),
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers+text",
        marker=dict(size=20, color="skyblue", line=dict(width=2, color="blue")),
        text=[f"{s}<br><sup>{d}</sup>" for s, d in zip(stages, durations)],
        textposition="top center",
        textfont=dict(size=15),
        showlegend=False
    ))

    fig.update_layout(
        title="Timeline Penagihan Pajak (PMK 189/PMK.03/2020)",
        xaxis=dict(visible=False), 
        yaxis=dict(visible=False),
        plot_bgcolor="white",
        margin=dict(l=50, r=50, t=60, b=60)  
    )

    st.plotly_chart(fig, use_container_width=True)

    # Tambahkan deskripsi resmi
    st.markdown("""
    Proses penagihan dimulai dari adanya dasar penagihan yang terdiri dari:  
    - Surat Tagihan Pajak (STP)  
    - Surat Ketetapan Pajak Kurang Bayar (SKPKB)  
    - Surat Ketetapan Pajak Tambahan (SKPKBT)  
    - Surat Keputusan Pembetulan (SK Pembetulan)  
    - Surat Keputusan Keberatan (SK Keberatan)  
    - Putusan Banding  
    - Putusan Peninjauan Kembali  
    - Dasar penagihan tidak disengketakan oleh Anda. 

    Timeline Penagihan Pajak:
    1. Jatuh tempo dasar penagihan adalah 1 (satu) bulan sejak terbit.  
    2. Apabila dalam jangka waktu tersebut Penanggung Pajak tidak mengajukan permohonan angsuran/penundaan dan tidak melunasi hingga jatuh tempo, maka setelah lewat waktu 7 hari sejak jatuh tempo akan dikeluarkan Surat Teguran.  
    3. Akan dikeluarkan Surat Paksa (SP) setelah lewat waktu 21 hari sejak diterbitkannya Surat Teguran oleh Jurusita secara langsung apabila Penanggung Pajak belum melunasi utang pajaknya.  
    4. Jurusita dapat melakukan pengumuman di media massa, pemblokiran, pencegahan, dan penyanderaan terhadap penanggung pajak yang belum melunasi utang pajak dan biaya penagihan tanpa menunggu jatuh tempo.    
    5. Apabila sampai batas waktu Surat Paksa (SP) Penanggung Pajak belum melunasi utang pajaknya, maka setelah lewat waktu 2 x 24 jam akan diterbitkan Surat Perintah Melaksanakan Penyitaan (SPMP).  
    6. Surat Pencabutan Sita diterbitkan oleh Jurusita apabila Penanggung Pajak telah melunasi utang pajak dan biaya penagihan atau berdasarkan keputusan pengadilan.  
    7. Pejabat lelang akan melakukan pengumuman lelang apabila setelah lewat waktu 14 hari sejak tanggal penyitaan, Penanggung Pajak belum juga melunasi utang pajak dan biaya penagihannya.  
    8. Pelaksanaan lelang dilaksanakan setelah lewat waktu 14 hari sejak pengumuman lelang apabila Penanggung Pajak tidak membayar utang pajak dan biaya penagihannya.  
                
    Keterangan Tambahan:
    1. Apabila Penanggung Pajak mempunyai utang pajak sekurang-kurangnya Rp100 juta dan diragukan itikad baiknya dalam melunasi utang pajak, dapat dilakukan pencegahan dan penyanderaan.  
    2. Jangka waktu penyanderaan adalah 6 bulan dan dapat diperpanjang maksimal 6 bulan. Penyanderaan tidak menghapus utang pajak dan penagihan tetap dilaksanakan.  

    Lebih lanjut di: [pajak.go.id - Penagihan](https://www.pajak.go.id/id/penagihan)
    """)

# TAB 3 – Panduan & Referensi
with tabs[2]:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.video("https://www.youtube.com/watch?v=UQiJq0szNNw&list=PLDDScx7l7xS2fT-w5yIhbd6aT0xg4g62O&index=22&pp=iAQB")
    with col2:
        st.video("https://www.youtube.com/watch?v=zn00tvtRRdY&list=PLDDScx7l7xS2fT-w5yIhbd6aT0xg4g62O&index=27&pp=iAQB")
    with col3:
        st.video("https://www.youtube.com/watch?v=Of14NW7FmQg&list=PLDDScx7l7xS3Kv-FFv8EKw8NBJ6WA9dbx&index=1&pp=iAQB")
    with col4:
        st.video("https://www.youtube.com/watch?v=UJ7TW_soGqM&list=PLDDScx7l7xS3Kv-FFv8EKw8NBJ6WA9dbx&index=3&pp=iAQB")

