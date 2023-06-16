import streamlit as st
import pandas as pd
import pickle as pkl
from sklearn import preprocessing

# SET PAGE
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Model", page_icon=":crystal_ball:", layout="centered")

# SET TITLE
st.title('Model Prediksi Profil Risiko Investasi')

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%"> Model klasifikasi ini menggunakan algoritma Random Forest dan dibuat dengan bahasa pemrograman Python. </div>',
            unsafe_allow_html=True)
st.write('')

# Create input form
usia = st.number_input(label = 'Masukkan usia Anda : ', min_value=18, max_value=60, step=1, key='1')
jenis_kelamin = st.selectbox('Sebutkan jenis kelamin Anda', ('Laki-laki', 'Perempuan'))
pendapatan = st.number_input(label = 'Masukkan jumlah pendapatan Anda : ', min_value=0, step=100000, key='2')
aset = st.number_input(label = 'Masukkan jumlah aset Anda : ', min_value=0, step=100000, key='3')
max_profit = st.selectbox('Apakah Anda memaksimalkan keuntungan saat berinvestasi?', ('Ya', 'Tidak'))
min_loss = st.selectbox('Apakah Anda meminimalkan kerugian saat berinvestasi?', ('Ya', 'Tidak'))
harga_turun = st.selectbox('Apa yang Anda lakukan saat harga turun?', ('Simpan / Tahan', 'Jual Sebagian', 'Jual Semua', 'Beli Lagi'))
literasi_financial = st.number_input(label = 'Dari skala 1-10, seberapa paham Anda akan literasi finansial?', min_value=1, max_value=10, step=1, key='4')
jenis_investasi = st.selectbox('Sebutkan jenis investasi yang Anda lakukan?', ('Deposito', 'Reksadana', 'Saham', 'Crypto'))

# Store result to DataFrame
dt = pd.DataFrame({'Usia':[usia],
                   'Jenis Kelamin':[jenis_kelamin],
                   'Pendapatan':[pendapatan],
                   'Aset':[aset],
                   'Maksimal Keuntungan?':[max_profit],
                   'Minimal Kerugian?':[min_loss],
                   'Perilaku saat Harga Turun':[harga_turun],
                   'Literasi Finansial':[literasi_financial],
                   'Jenis Instrumen Investasi':[jenis_investasi]})

# Preprocessing
lst_encode = ['Jenis Kelamin',
              'Maksimal Keuntungan?',
              'Minimal Kerugian?',
              'Perilaku saat Harga Turun',
              'Jenis Instrumen Investasi']

le = preprocessing.LabelEncoder()

for i in lst_encode:
    dt[i] = le.fit_transform(dt[i])

# LOAD MODEL
filename = 'finalized_model_rf.sav'
loaded_model = pkl.load(open(filename, 'rb'))

# ADD SUBMIT BUTTON
submit = st.button("Submit")

# DO PREDICTION
result_pred = loaded_model.predict(dt.values)

# SHOW RESULT
if submit:
    text1 = "Tingkat Profil Risiko Anda : "
    result_profil = text1 + result_pred[0]
    if result_pred[0] == "Konservatif":
        st.info(result_profil)
        st.markdown(
            '<div style="text-align: justify; font-size:100%"> Berdasarkan profil risiko Anda, maka berikut beberapa saran yang bisa kami berikan :<br><br> </div>',
            unsafe_allow_html=True)
        st.success("- Mengambil jenis instrumen investasi yang stabil, berisiko rendah atau bahkan tidak ada risiko sama sekali. ")
        st.success("- Contoh instrumen investasi yang bisa diambil yaitu Reksadana Pasar Uang, Deposito, dan lain sebagainya.")
    elif result_pred[0] == "Moderat":
        st.warning(result_profil)
        st.markdown(
            '<div style="text-align: justify; font-size:100%"> Berdasarkan profil risiko Anda, maka berikut beberapa saran yang bisa kami berikan :<br><br> </div>',
            unsafe_allow_html=True)
        st.success("- Mengambil jenis instrumen investasi yang memiliki fluktuasi sedang dan memiliki risiko tingkat menengah.")
        st.success("- Contoh instrumen investasi yang bisa diambil yaitu Reksadana Pendapatan Tetap, Reksadana Obligasi, dan Reksadana Campuran.")
    else:
        st.error(result_profil)
        st.markdown(
            '<div style="text-align: justify; font-size:100%"> Berdasarkan profil risiko Anda, maka berikut beberapa saran yang bisa kami berikan :<br><br> </div>',
            unsafe_allow_html=True)
        st.success("- Mengambil jenis instrumen investasi yang memiliki fluktuasi dan risiko yang cukup tinggi.")
        st.success("- Contoh instrumen investasi yang bisa diambil yaitu Reksadana Campuran, Saham, atau bahkan Crypto.")