# IMPORT LIBRARY
import streamlit as st

# SET PAGE
st.set_page_config(page_title="News Article", page_icon=":newspaper:", layout="centered")

# ---- SIDEBAR ----
st.sidebar.header("Financial News Article")

jenis_berita = st.sidebar.selectbox(
    'Pilih berita di sini',
    ('Jenis Profil Risiko Investasi',
     'Jenis Instrumen Investasi',
     'Coming Soon'))

# MENAMPILKAN BERITA
if jenis_berita == 'Jenis Profil Risiko Investasi':
    st.header('Sebelum Berinvestasi, Yuk Kenali Dulu Jenis Profil Risiko Investasi!')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write("### Profil Risiko : Konservatif")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Sesuai namanya, tipe ini cenderung menghindari risiko. Profil risiko konservatif cocok untuk reksadana pasar uang yang dikenal minim risiko. Jadi, sebelum memulai investasi reksadana, kenali dulu profil risiko kamu, ya. Selain cocok untuk reksadana pasar uang, tipe konservatif juga dapat memilih reksadana obligasi. Sebab, baik reksadana pasar uang maupun obligasi, berpotensi menghasilkan return lebih tinggi, dengan risiko yang relatif rendah. </div>',
        unsafe_allow_html=True)

    st.write("### Profil Risiko : Moderat")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Karakter ini siap menerima fluktuasi jangka pendek. Artinya, tidak terlalu kaget dengan penurunan nilai reksadana, walau tidak begitu siap juga kalau instrumen investasinya tiba-tiba kebakaran. Tipe reksadana yang cocok untuk profil moderat adalah reksa dana campuran yang risikonya masih relatif rendah, dibandingkan reksa dana saham. Namun, jika pun kamu yang berprofil moderat ingin memilih reksadana saham, tidak ada salahnya. Asalkan, sedikit demi sedikit kamu mulai belajar menghadapi goncangan nilai di reksadana tersebut. </div>',
        unsafe_allow_html=True)

    st.write("### Profil Risiko : Agresif")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Bisa dikatakan, profil ini siap banget buat kaya sekaligus siap juga jatuh miskin. Secara sederhana, tipe agresif adalah risk taker yang siap berinvestasi di seluruh instrumen keuangan seperti reksa dana saham. Tidak hanya itu, kalau kamu berisiko agresif, kamu pun biasanya berani investasi saham secara langsung. Tipe ini agresif biasanya diisi oleh para investor tingkat lanjut (bukan pemula) yang sudah mampu menganalisis pasar. </div>',
        unsafe_allow_html=True)

    st.write("#### Source : [Link](https://artikel.bibit.id/investasi1/sebelum-investasi-reksadana-kenali-dulu-profil-risiko-kamu-yuk)")

elif jenis_berita == 'Jenis Instrumen Investasi':
    st.header('Sebelum Berinvestasi, Yuk Kenali Dulu Jenis Instrumen Investasi!')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write("### Deposito")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Instrumen investasi deposito merupakan salah satu jenis instrumen yang sangat sering digunakan oleh banyak orang. Prinsip melakukan investasi pada instrumen ini mirip seperti menabung, namun kamu dapat mendapatkan keuntungan yang lebih besar dari deposito. Dalam investasi deposito, kamu harus menyimpan sejumlah uang dalam batas waktu yang telah ditentukan. Batas waktu tersebut dapat selama beberapa bulan atau hingga beberapa tahun. Hal yang perlu kamu ingat adalah kamu tidak dapat mengambil uang yang telah kamu masukkan ke dalam deposito hingga batas waktu yang telah ditentukan. Selama waktu tersebut, Kamu akan mendapatkan return sesuai dengan perhitungan yang telah ditentukan sejak awal. Jika kamu mengambil uang dari deposito sebelum batas waktu yang ditentukan, kamu dapat terkena denda. </div>',
        unsafe_allow_html=True)

    st.write("### Reksadana")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Kamu baru mulai mencoba untuk melakukan investasi? Reksa dana mungkin menjadi pilihan instrumen investasi yang tepat bagi kamu. Portofolio investasi pada instrumen ini telah dikelola oleh manajer investasi yang berpengalaman sehingga kamu tidak perlu repot seperti pada instrumen saham. Jumlah keuntungan yang kamu peroleh juga dapat lebih besar apabila dibandingkan dengan keuntungan deposito. Jika ingin melakukan investasi di reksa dana, kamu sekarang dapat melakukannya di berbagai aplikasi atau platform online yang telah banyak tersedia seperti <b>Bibit</b> dan <b>Bareksa</b>. </div>',
        unsafe_allow_html=True)

    st.write("### Saham")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Saham merupakan suatu instrumen investasi yang berupa bukti kepemilikan nilai terhadap sebuah perusahaan atau bukti penyertaan modal. Jika kamu merupakan pemegang saham, kamu akan memiliki hak untuk mendapatkan dividen sesuai dengan perhitungan jumlah saham yang kamu miliki. Kenaikan dan penurunan nilai saham dapat dipengaruhi oleh berbagai faktor. Instrumen investasi saham dapat memberikan nilai keuntungan atau imbal balik yang tinggi, namun hal ini juga menyebabkan saham memiliki resiko yang lebih tinggi dibandingkan dengan instrumen investasi lainnya. Selain itu, membeli saham juga sangat mudah karena bisa dilakukan melalui aplikasi seperti <b>Stockbit</b>. </div>',
        unsafe_allow_html=True)

    st.write("### Crypto")
    st.markdown(
        '<div style="text-align: justify; font-size:100%"> Investasi crypto atau cryptocurrency adalah jenis investasi yang menawarkan return tinggi/high return. Cryptocurrency sendiri adalah mata uang digital yang hanya ada dan bisa digunakan di dunia maya. Cryptocurrency sendiri digunakan untuk berbagai transaksi, seperti pembelian jasa game dan aksesorisnya sampai berbelanja hal lain seperti barang untuk dipakai. Dari situ, jual beli bitcoin makin marak dan populer hingga muncul uang kripto lainnya. Selain bitcoin yang sangat populer, contoh mata uang kripto lainnya adalah Ethereum, Ripple, Litecoin, Mana, SandBox, dan sebagainya. Cara membeliny juga cukup gampang di mana kita bisa membeli koin crypto melalui aplikasi seperti <b>TokoCrypto</b> dan <b>Binance</b>. </div>',
        unsafe_allow_html=True)

    st.write(
        "#### Source 1 : [Link](https://www.generali.co.id/id/healthyliving/detail/607/menarik-inilah-5-jenis-instrumen-investasi-yang-bisa-kamu-pilih)")
    st.write(
        "#### Source 2 : [Link](https://www.cermati.com/artikel/investasi-crypto-jenis-manfaat-dan-risiko-yang-perlu-diketahui)")

elif jenis_berita == 'Coming Soon':
    st.header('Coming Soon!')
    st.markdown('<hr>', unsafe_allow_html=True)