import streamlit as st
from PIL import Image


# apply photo
image = Image.open(r"C:\group11\asset\banner.jpg", "r")
st.image(image)

st.title("CYBERCRIME")

st.markdown(
    """### Apa Itu Cybercrime? :right_anger_bubble:

**PENGERTIAN**

Cyber crime adalah kejahatan dunia maya yang dilakukan individu atau sekelompok orang yang menyerang sistem keamanan komputer atau data-data yang ada di dalam komputer. Kejahatan tersebut dilakukan dengan beragam motif, mulai dari kepuasan diri hingga kejahatan yang dapat merugikan ekonomi atau politik.
    
""",
    unsafe_allow_html=True,
)
st.write(
    "sumber : https://www.merdeka.com/jateng/cyber-crime-adalah-kejahatan-dunia-maya-ketahui-jenis-dan-cara-mencegahnya-kln.html"
)
st.write(
    """Untuk lebih jelas lagi mengenai cybersecurity, kalian juga dapat
simak penjelasannya di video berikut ya..."""
)

# apply video
video_file = open("C:\group11\cybercrime.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
st.caption("Created by Group 11")

# topic about the type of cybercrime
st.markdown(
    """### Jenis Cybercrime yang sering terjadi di Indonesia
    
""",
    unsafe_allow_html=True,
)
st.write(
    """Penipuan online atau penipuan digital yang saat ini makin banyak modusnya. 
Di antaranya adalah modus penipuan berkedok foto selfie dengan KTP atau identitas diri. 
Foto selfie bersama KTP biasanya menjadi salah satu syarat registrasi online akun keuangan, 
seperti dompet digital, paylater, pinjaman online, sampai daftar rekening bank online. 
Bisa saja kamu terjebak aplikasi pinjaman online palsu yang dibuat sedemikian rupa. 
Kemudian oleh pelaku, data kamu dipakai untuk pencucian uang, dijual di pasar gelap, 
atau digunakan sesuka hati untuk pinjaman online ilegal."""
)
# if st.button('Next Page'):
#    st.write('move to page 4')
# else:
#    st.write('Stay in page_3')
