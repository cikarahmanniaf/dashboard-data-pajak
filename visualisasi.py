import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

EXCEL_PATH = "https://docs.google.com/spreadsheets/d/1I0UOQbYxk9MMDVx8HVrQSxoPkiEhf7JS/export?format=xlsx"

@st.cache_data
def load_sheet(path, sheet_name):
    return pd.read_excel(path, sheet_name=sheet_name)

# Load data
ppn = load_sheet(EXCEL_PATH, "PPN")
pph21 = load_sheet(EXCEL_PATH, "PPh 21")
pph22 = load_sheet(EXCEL_PATH, "PPh 22")
pph23 = load_sheet(EXCEL_PATH, "PPh 23")
pph21_sektor = load_sheet(EXCEL_PATH, "PPh 21 Sektor")
wp = load_sheet(EXCEL_PATH, "Data Wajib Pajak")

st.title("Visualisasi Data Pajak")
st.write("Isi filter data di bawah untuk melihat grafik penerimaan pajak:")

col1, col2, col3 = st.columns(3)

with col1:
    tahun_list = ["2020","2021","2022","2023","2024"]
    tahun = st.multiselect("Pilih Tahun", ["Semua"] + tahun_list, default=["Semua"])
    if "Semua" in tahun:
        tahun = tahun_list

with col2:
    bulan_list = list(range(1, 13))
    bulan = st.multiselect("Pilih Bulan", ["Semua"] + bulan_list, default=["Semua"])
    if "Semua" in bulan:
        bulan = bulan_list

with col3:
    jenis_list = ["PPN","PPh 21","PPh 22","PPh 23"]
    jenis_pajak = st.multiselect("Pilih Jenis Pajak", ["Semua"] + jenis_list, default=["Semua"])
    if "Semua" in jenis_pajak:
        jenis_pajak = jenis_list


# Konversi ke format datetime agar bisa diplot
df_tren = pd.DataFrame()
for pajak, df in [("PPN", ppn), ("PPh 21", pph21), ("PPh 22", pph22), ("PPh 23", pph23)]:
    if pajak in jenis_pajak:
        for th in tahun:
            tmp = df[["Bulan", th]].copy()
            tmp = tmp[tmp["Bulan"].isin(bulan)]
            tmp.rename(columns={th: "Nilai"}, inplace=True)

            # Kolom tambahan
            tmp["Tahun"] = int(th)
            tmp["Jenis Pajak"] = pajak
            
            bulan_map = {
                "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
                "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12,
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
            }

            tmp["Bulan_num"] = tmp["Bulan"].map(bulan_map).fillna(tmp["Bulan"])
            tmp["Periode"] = pd.to_datetime(dict(year=tmp["Tahun"], month=tmp["Bulan_num"].astype(int), day=1))

            df_tren = pd.concat([df_tren, tmp])        

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background-color:#fff7e6; padding:5px; border-radius:10px; margin-bottom:10px;">
        <h4 style="text-align:center;">Penerimaan Pajak Bulanan</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    if not df_tren.empty:
        # Memastikan kolom Nilai numerik
        df_tren["Nilai"] = (
            df_tren["Nilai"].astype(str).str.replace(",", ".").astype(float)
        )

        fig_tren = px.line(
            df_tren, 
            x="Periode", 
            y="Nilai", 
            color="Jenis Pajak", 
            markers=True,
            labels={"Nilai": "Nilai (Rp Miliar)"},
            color_discrete_map={
                "PPN": "#183B4E",
                "PPh 21": "#27548A",
                "PPh 22": "#80A1BA",
                "PPh 23": "#87CEEB"
            }
        )

        # skala Y
        fig_tren.update_yaxes(range=[0, 130])  

        st.plotly_chart(fig_tren, use_container_width=True)
    else:
        st.warning("Tidak ada data untuk filter ini.")

with col2:
    st.markdown(
        """
        <div style="background-color:#fff7e6; padding:5px; border-radius:10px; margin-bottom:10px;">
        <h4 style="text-align:center;">Penerimaan Pajak Tahunan</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    if not df_tren.empty:
        df_tahunan = df_tren.groupby(["Tahun","Jenis Pajak"])["Nilai"].sum().reset_index()
        fig_tahunan = px.bar(
            df_tahunan, 
            x="Tahun", 
            y="Nilai", 
            color="Jenis Pajak", 
            barmode="group",
            labels={"Nilai": "Nilai (Rp Miliar)"},
            color_discrete_map={
                "PPN": "#183B4E",
                "PPh 21": "#27548A",
                "PPh 22": "#80A1BA",
                "PPh 23": "#87CEEB"
            }
        )
        # skala Y
        fig_tahunan.update_yaxes(range=[0, 500])  
        
        st.plotly_chart(fig_tahunan, use_container_width=True)
    else:
        st.warning("Tidak ada data untuk filter ini.")

st.markdown(
    """
    <div style="background-color:#fff7e6; padding:5px; border-radius:10px; margin-bottom:10px;">
    <h4 style="text-align:center;">Penerimaan Pajak Penghasilan (PPh) Pasal 21 per Jenis Sektor</h4>
    </div>
    """,
    unsafe_allow_html=True
)

pph21_sektor = pph21_sektor.reset_index()
sektor_col = pph21_sektor.columns[1]

# Reshape dari wide ke long
df_pph21_stack = pph21_sektor.melt(
    id_vars=[sektor_col],
    var_name="Tahun",
    value_name="Nilai"
)

# Hitung persentase kontribusi per tahun
df_pph21_stack["Persen"] = df_pph21_stack.groupby("Tahun")["Nilai"].transform(lambda x: x / x.sum() * 100)

# Pilihan tahun
tahun_list = ["2020", "2021", "2022", "2023", "2024"]
tahun_sektor = st.selectbox("Pilih Tahun", tahun_list)

# Filter sesuai tahun
df_tahun = df_pph21_stack[df_pph21_stack["Tahun"] == tahun_sektor].copy()
df_tahun["Kode Sektor"] = df_tahun[sektor_col].str.split("-").str[0].str.strip()
df_tahun["Nama Sektor"] = df_tahun[sektor_col].str.split("-", n=1).str[1].str.strip()

# Buat bar chart
fig_pph21_bar = px.bar(
    df_tahun,
    x="Kode Sektor",
    y="Nilai",
    color="Kode Sektor",
    hover_data={
        "Nilai": ":,.2f",
        "Persen": ":.2f",
        "Tahun": True,
        "Nama Sektor": True
    },
    color_discrete_sequence=["#183B4E"],
    labels={"Nilai": "Nilai (Rp Miliar)"}
)
fig_pph21_bar.update_yaxes(range=[0, 80])

fig_pph21_bar.update_layout(
    yaxis=dict(title="Penerimaan Pajak (Rp Miliar)"),
    xaxis=dict(title="Kode Sektor"),
    showlegend=False
)

st.plotly_chart(fig_pph21_bar, use_container_width=True)

# Transformasi data
df_melt = wp.melt(id_vars="Jenis WP", var_name="Kecamatan_Jenis", value_name="Jumlah")
df_melt.rename(columns={"Jenis WP": "Tahun"}, inplace=True)

# Split "Kecamatan Jenis" jadi 2 kolom
df_melt[["Kecamatan", "Jenis"]] = df_melt["Kecamatan_Jenis"].str.rsplit(" ", n=1, expand=True)
df_melt["Kecamatan"] = df_melt["Kecamatan"].str.replace("Kec ", "")

# Line Chart per Jenis WP
fig_line = px.line(
    df_melt,
    x="Tahun", 
    y="Jumlah",
    facet_col="Jenis",       
    markers=True,
    color="Kecamatan",
    color_discrete_sequence=["#27548A","#80A1BA", "#87CEEB"]    

)

fig_line.update_layout(
    height=380,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.6,
        xanchor="center",
        x=0.5
    ),
    legend_title_text="Kecamatan"
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background-color:#fff7e6; padding:5px; border-radius:10px; margin-bottom:10px;">
        <h4 style="text-align:center;">Tren Wajib Pajak per Jenis WP</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.markdown(
        """
        <div style="background-color:#fff7e6; padding:5px; border-radius:10px; margin-bottom:10px;">
        <h4 style="text-align:center;">Komposisi Jenis Wajib Pajak</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Filter Tahun untuk Pie Chart
    tahun_pilih = st.selectbox("Pilih Tahun untuk Pie Chart:", sorted(df_melt["Tahun"].unique()))
    df_pie = df_melt[df_melt["Tahun"] == tahun_pilih]

    # Pie Chart
    fig_pie = px.pie(
        df_pie,
        names="Jenis",
        values="Jumlah",
        facet_col="Kecamatan",
        color="Jenis",
        color_discrete_map={
            "Badan": "#80A1BA",           
            "OP": "#27548A",   
            "Pemungut/Bendahara": "#87CEEB"  
        }
    )
    fig_pie.update_layout(
        height=300,
        margin=dict(t=40, b=80), 
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5,
            font=dict(size=11),
            bgcolor="rgba(0,0,0,0)"
        )
    )

    st.plotly_chart(fig_pie, use_container_width=True)

