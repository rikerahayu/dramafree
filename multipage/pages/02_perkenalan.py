import streamlit as st
from PIL import Image

# apply photo
image = Image.open(r"C:\group11\asset\banner.jpg", "r")
st.image(image)

st.title("Welcome To Our Tim!")

image = Image.open(r"C:\group11\asset\tim.png", "r")
st.image(image, caption="Women In Tech - Group 11")

# with st.expander("Data Tim Kami"):
#    data1, data2, data3 = st.columns(3)
#    data1.metric("Ayu Perwita Sari", "Ayu", "Mahasiswa")
#    data2.metric("Iva Kurnia", "Iva", "PNS")
#    data3.metric("Rike Rahayu", "Rike", "Pengajar")


# st.markdown(
#    """**Nama Lengkap  :bar_chart:**"""
# )

# st.write("Iva Kurnia")
# st.write("Ayu Perwita Sari")
# st.write("Rike Rahayu")#
