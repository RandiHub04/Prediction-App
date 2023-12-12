#Load libraries needed
import streamlit as st

#Set page configuration
st.set_page_config(
    page_title= "Selamat Datang di Aplikasi Time Series",
    page_icon="🙌",
    layout="wide"
)

# Add content your Streamlit app
st.markdown("# 🎉Selamat Datang di Aplikasi Prediksi Penjualan Produk di seluruh toko")

# Display the waving GIF
st.image("https://www.animatedimages.org/data/media/707/animated-welcome-image-0058.gif")

# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
            0%{
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .slide-in-animation {
            animation: slide-in 1.5s ease-in-out;
        }

    <style>

""",unsafe_allow_html=True)


# Text with animation
st.write('<div class= "slide-in-animation"> Aplikasi ini dirancang sedemikian rupa agar bisa memprediksi penjualan produk diseluruh toko </div>', unsafe_allow_html=True)

# add a sidebar to select pages
st.sidebar.success("Pilih halaman di atas.")


# Create a Streamlit container for the subheader
subheader_container = st.container()


#Define the subheader content
subheader_content = """
<div class= "slide-in-animation">
<h3> Hal yang Dapat Anda Lakukan Di Aplikasi Ini:</h3>
<ul>
  <li>Perkiraan penjualan pada Tanggal Tertentu untuk Toko Favorite</li>
  <li>Lihat kumpulan data dan berinteraksi dengan visual yang menunjukkan penjualan harian di seluruh toko</li>
  <li>Kenali lebih banyak tentang tim</li>
</ul>
</div>
"""


# Apply Css animation using HTML/CSS
subheader_container.markdown(subheader_content, unsafe_allow_html=True)

# Add CSS Animation
st.write("""
    <style>
        @keyframes slide-in {
            0%{
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .slide-in-animation {
            animation: slide-in 1.5s ease-in-out;
        }

    <style>

""",unsafe_allow_html=True)
