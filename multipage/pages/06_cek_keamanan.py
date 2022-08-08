import streamlit as st
from PIL import Image

# apply photo
image = Image.open(r"C:\group11\asset\banner.jpg", "r")
st.image(image)


st.title("Cek Yuk :memo:")
st.markdown(
    """### Mari kita cek apakah anda aman

**Pilihlah pilihan di bawah ini yang mencerminkan kondisi dan keadaan anda** 
 
""",
    unsafe_allow_html=True,
)
first = st.checkbox(
    "Saya selalu waspada jika ada telepon dari nomor yang tidak dikenal dan mengecek melalui aplikasi cek nomor telepon (misal: get contact)"
)
second = st.checkbox(
    "Saya sangat berhati-hati jika diminta melakukan transaksi di luar marketplace dan mengecek rekening yang diberikan apakah sudah pernah dilaporkan atas penipuan"
)

third = st.checkbox(
    "Saya tidak serta merta mempercayai informasi yang disampaikan melalui telepon dan mengecek terlebih dahulu kebenarannya"
)

four = st.checkbox(
    "Saya tidak akan memberikan informasi pribadi dalam bentuk apapun termasuk username, password, dan kode OTP kepada orang lain "
)

five = st.checkbox(
    "Saya tidak mau membuka tautan yang dikirim oleh orang yang tidak dikenal melalui email atau yang mencoba meniru organisasi resmi"
)

six = st.checkbox(
    "Saya tidak mudah tergiur iming-iming berupa hadiah dan melakukan transfer uang yang diminta untuk mendapat hadiah tersebut"
)

seven = st.checkbox(
    "Tidak menggunakan jaringan umum seperti WIFI di tempat umum untuk melakukan transaksi online."
)

known_variables = first + second + third + four + five + six
if known_variables == 1:
    st.error("Saya rentan sehingga mudah terkena penipuan online")
elif known_variables == 2:
    st.error("Saya rentan sehingga mudah terkena penipuan online")
elif known_variables == 3:
    st.warning("Saya mungkin dapat dengan mudah terkena penipuan online")
elif known_variables == 4:
    st.warning("Saya mungkin dapat dengan mudah terkena penipuan online")
elif known_variables == 5:
    st.success("Saya aman dari penipuan online")
elif known_variables == 6:
    st.success("Saya aman dari penipuan online")
elif known_variables == 7:
    st.success("Saya aman dari penipuan online")
