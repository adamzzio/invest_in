import streamlit as st

# SET PAGE
st.set_page_config(page_title="Invest-in Web App", page_icon=":money_with_wings:", layout="centered")

# SET TITLE AND LOGO IMAGE
intro_col_left, intro_col_right = st.columns(2)
intro_col_left.image('logo_investin.png')
intro_col_right.markdown('<div style="text-align: justify; font-size:210%"> <b>Web App Analisis Profil Risiko Investasi</b> </div>',
            unsafe_allow_html=True)

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%"> Web App ini merupakan suatu aplikasi di mana kita bisa memprediksi suatu profil risiko investasi seseorang berdasarkan beberapa variabel seperti jenis investasi, jumlah pendapatan dan aset, dan lain sebagainya. </div>',
            unsafe_allow_html=True)

# ANGGOTA TIM
st.write('## Anggota Tim :')

col1, col2, col3 = st.columns(3)

# For columns 1 : Introduce Adam Maurizio Winata
col1.write('### Adam Maurizio Winata')
col1.image('foto_adam.jpg', caption = 162012133045)

# For columns 2 : Introduce Annaura Nabilla Masduki
col2.write('### Annaura Nabilla Masduki')
col2.image('foto_annaura.jpeg', caption = 162012133021)

# For columns 3 : Introduce Cindi Nirmala Nadia
col3.write('### Cindi Nirmala Nadia')
col3.image('foto_cindi.jpeg', caption = 162012133018)

# KETERANGAN AKHIR
st.markdown('<div style="text-align: justify; font-size:160%"> Web App ini dibuat untuk memenuhi tugas akhir / UAS pada mata kuliah Data Mining SD-A1 Prodi Teknologi Sains Data Universitas Airlangga. </div>',
            unsafe_allow_html=True)
