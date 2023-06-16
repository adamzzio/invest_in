# IMPORT LIBRARY
import pandas as pd
import numpy as np
import scipy.stats as sci_stats
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import requests
from PIL import Image
import matplotlib.pyplot as plt

# SET PAGE
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

# IMPORT DATASET
df = pd.read_excel('DATA_DATMIN_KEL11_CREDIT SCORING.xlsx')

# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_ajzyv37m.json")

# HEADER
intro_column_left, intro_column_right = st.columns(2)
with st.container():
    with intro_column_left:
        # st.title(":bar_chart: Dashboard")
        st.markdown('<div style="text-align: justify; font-size:210%; line-height: 150%; margin-top: 10px;"> <b><br>Dashboard Profil Risiko Investasi Mahasiswa/i di Surabaya</b> </div>',
            unsafe_allow_html=True)
    with intro_column_right:
        st_lottie(lottie_coding, height=250, key="dashboard")

# st.markdown("##")
st.markdown('<hr>', unsafe_allow_html=True)

# TOP KPI's
est_interval_pendapatan = sci_stats.norm.interval(alpha=0.95,
                                                  loc=np.mean(df['Berapa jumlah pendapatan dalam sebulan?']),
                                                  scale=sci_stats.sem(df['Berapa jumlah pendapatan dalam sebulan?']))
est_interval_aset = sci_stats.norm.interval(alpha=0.95,
                                            loc=np.mean(df['Berapa aset yang anda miliki sekarang?']),
                                            scale=sci_stats.sem(df['Berapa aset yang anda miliki sekarang?']))
avg_lit_finance = round(df["Dari skala 1-10, sebutkan seberapa paham Anda akan literasi finansial?"].mean(), 1)
star_rating = ":star:" * int(round(avg_lit_finance, 0))

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Rata-rata Jumlah Pendapatan")
    st.write("Rp. ", np.round(est_interval_pendapatan[0],2), "- Rp. ", np.round(est_interval_pendapatan[1], 2))
with middle_column:
    st.subheader("Rata-rata Jumlah Aset Kekayaan")
    st.write("Rp. ", np.round(est_interval_aset[0],2), "- Rp. ", np.round(est_interval_aset[1], 2))
with right_column:
    st.subheader("Rata-rata Pemahaman Finansial")
    st.write(star_rating, "(", avg_lit_finance, ")")

st.markdown("""---""")

# GRAFIK BAR PLOT - RATA-RATA PENDAPATAN BERDASAR PROFIL RISIKO INVESTASI
avg_pendapatan_profil= df.groupby('Apa tingkat Profil Resiko investasi anda?')['Berapa jumlah pendapatan dalam sebulan?'].mean()
avg_pendapatan_profil = pd.DataFrame(avg_pendapatan_profil).sort_values(by='Berapa jumlah pendapatan dalam sebulan?',
                                                                        ascending=False)

fig_avg_profil_pendapatan = px.bar(avg_pendapatan_profil,
                                   x=avg_pendapatan_profil.index,
                                   y="Berapa jumlah pendapatan dalam sebulan?",
                                   title="<b>Rata-rata Pendapatan berdasarkan<br>Profil Risiko Investasi</b>",
                                   labels={"Apa tingkat Profil Resiko investasi anda?": "Profil Risiko",
                                           "Berapa jumlah pendapatan dalam sebulan?": "Rata-rata Pendapatan"},
                                   color_discrete_sequence=["#0083B8"] * len(avg_pendapatan_profil),
                                   template="plotly_white",
)
fig_avg_profil_pendapatan.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# # GRAFIK BAR PLOT - RATA-RATA ASET BERDASAR PROFIL RISIKO INVESTASI
avg_pendapatan_aset= df.groupby('Apa tingkat Profil Resiko investasi anda?')['Berapa aset yang anda miliki sekarang?'].mean()
avg_pendapatan_aset = pd.DataFrame(avg_pendapatan_aset).sort_values(by='Berapa aset yang anda miliki sekarang?',
                                                                        ascending=False)

fig_avg_profil_aset = px.bar(avg_pendapatan_aset,
                             x=avg_pendapatan_aset.index,
                             y="Berapa aset yang anda miliki sekarang?",
                             title="<b>Rata-rata Aset berdasarkan<br>Profil Risiko Investasi</b>",
                             labels={"Apa tingkat Profil Resiko investasi anda?": "Profil Risiko",
                                     "Berapa aset yang anda miliki sekarang?":"Rata-rata Aset"},
                             color_discrete_sequence=["#0083B8"] * len(avg_pendapatan_aset),
                             template="plotly_white",
)
fig_avg_profil_aset.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# GRAFIK PIE CHART - PROPORSI MAKSIMAL KEUNTUNGAN
prop_max_profit = df['Apakah anda memaksimalkan keuntungan dalam berinvestasi?'].value_counts()
prop_max_profit = pd.DataFrame(prop_max_profit)

fig_pie_max_profit = px.pie(prop_max_profit,
                            values="count",
                            names=prop_max_profit.index,
                            title="<b>Apakah anda memaksimalkan keuntungan<br>dalam berinvestasi?</b>")

fig_pie_max_profit.update_layout(
    plot_bgcolor="rgba(0,0,0,0)"
)

# GRAFIK PIE CHART - PROPORSI MINIMAL KERUGIAN
prop_min_loss = df['Apakah Anda meminimalkan kerugian dalam berinvestasi?'].value_counts()
prop_min_loss = pd.DataFrame(prop_min_loss)

fig_pie_min_loss = px.pie(prop_min_loss,
                            values="count",
                            names=prop_min_loss.index,
                            title="<b>Apakah Anda meminimalkan kerugian<br>dalam berinvestasi?</b>")

fig_pie_min_loss.update_layout(
    plot_bgcolor="rgba(0,0,0,0)"
)

# GRAFIK BAR PLOT - PROPORSI JUMLAH JENIS INVESTASI
prop_jenis_invest = df['Sebutkan jenis investasi yang Anda lakukan!'].value_counts()
prop_jenis_invest = pd.DataFrame(prop_jenis_invest).sort_values(by='Sebutkan jenis investasi yang Anda lakukan!',
                                                        ascending=False)

fig_prop_jenis_invest = px.bar(prop_jenis_invest,
                               x=prop_jenis_invest.index,
                               y=prop_jenis_invest['count'],
                               title="<b>Perbandingan Jumlah Jenis Investasi</b>",
                               labels={"index": "Jenis Investasi",
                                       "count":"Jumlah"},
                               color_discrete_sequence=["#0083B8"] * len(prop_jenis_invest),
                               template="plotly_white",
)
fig_prop_jenis_invest.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# # GRAFIK BAR PLOT - PROPORSI JUMLAH PROFIL RISIKO INVESTASI
# prop_jenis_profil = df['Apa tingkat Profil Resiko investasi anda?'].value_counts()
# prop_jenis_profil = pd.DataFrame(prop_jenis_profil).sort_values(by='Apa tingkat Profil Resiko investasi anda?',
#                                                         ascending=False)

# fig_prop_jenis_profil = px.bar(prop_jenis_profil,
#                                x=prop_jenis_profil.index,
#                                y="Apa tingkat Profil Resiko investasi anda?",
#                                title="<b>Perbandingan Jumlah Profil Risiko Investasi</b>",
#                                labels={"index": "Profil Risiko Investasi",
#                                        "Apa tingkat Profil Resiko investasi anda?":"Jumlah"},
#                                color_discrete_sequence=["#0083B8"] * len(prop_jenis_profil),
#                                template="plotly_white",
# )
# fig_prop_jenis_profil.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

# # GRAFIK BAR PLOT - PROPORSI PERILAKU INVESTOR SAAT HARGA TURUN
# prop_harga_turun = df['Apa yang Anda lakukan ketika harga turun?'].value_counts()
# prop_harga_turun = pd.DataFrame(prop_harga_turun).sort_values(by='Apa yang Anda lakukan ketika harga turun?',
#                                                         ascending=False)

# fig_prop_harga_turun = px.bar(prop_harga_turun,
#                               x=prop_harga_turun.index,
#                               y="Apa yang Anda lakukan ketika harga turun?",
#                               title="<b>Perbandingan Perilaku Investor<br>Saat Harga Turun</b>",
#                               labels={"index": "Jenis Perilaku",
#                                       "Apa yang Anda lakukan ketika harga turun?":"Jumlah"},
#                               color_discrete_sequence=["#0083B8"] * len(prop_harga_turun),
#                               template="plotly_white",
# )
# fig_prop_harga_turun.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

# # GRAFIK SCATTER PLOT - HUBUNGAN PENDAPATAN DENGAN ASET
# fig_scatter_pendapatan_aset = px.scatter(df,
#                                          x="Berapa jumlah pendapatan dalam sebulan?",
#                                          y="Berapa aset yang anda miliki sekarang?",
#                                          color="Apa tingkat Profil Resiko investasi anda?",
#                                          title="<b>Hubungan Pendapatan dengan Aset</b>",
#                                          labels={
#                                              "Berapa jumlah pendapatan dalam sebulan?": "Pendapatan",
#                                              "Berapa aset yang anda miliki sekarang?": "Aset",
#                                              "Apa tingkat Profil Resiko investasi anda?": "Profil Risiko Investasi"
#                                          },
#                                          template="plotly_dark"
#                                          )

# # DASHBOARD
left_column_chart_row1, right_column_chart_row1 = st.columns(2)
left_column_chart_row1.plotly_chart(fig_avg_profil_pendapatan, use_container_width=True)
right_column_chart_row1.plotly_chart(fig_avg_profil_aset, use_container_width=True)

left_column_chart_row2, right_column_chart_row2 = st.columns(2)
left_column_chart_row2.plotly_chart(fig_pie_max_profit, use_container_width=True)
right_column_chart_row2.plotly_chart(fig_pie_min_loss, use_container_width=True)

# left_column_chart_row3, mid_column_chart_row3, right_column_chart_row3 = st.columns(3)
# left_column_chart_row3.plotly_chart(fig_prop_jenis_invest, use_container_width=True)
# mid_column_chart_row3.plotly_chart(fig_prop_harga_turun, use_container_width=True)
# right_column_chart_row3.plotly_chart(fig_prop_jenis_profil, use_container_width=True)

# st.plotly_chart(fig_scatter_pendapatan_aset, use_container_width=True)

left_column_chart_row4, mid_column_chart_row4, right_column_chart_row4 = st.columns([1,6,1])
mid_column_chart_row4.image("wordcloud.png", use_column_width=True, caption="WordCloud Opini Investasi")
