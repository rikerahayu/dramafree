import streamlit as st
from PIL import Image

# apply photo
image = Image.open(r"C:\group11\asset\banner.jpg", "r")
st.image(image)

st.title("PERAN PENDIDIKAN")
st.markdown(
    """### Mengapa pendidikan itu penting dalam menekan angka kejahatan cybersecurity? 	:thinking_face:
    
"""
)

st.write(
    "Pendidikan merupakan senjata paling tajam di dunia karena dengan pendidikan anda dapat mengubah dunia. - Nelson Mandela"
)
st.write("Peran 1")
st.write("Penjelasan")

st.write("Peran 2")
st.write("Penjelasan")

st.write("Peran 3")
st.write("Penjelasan")

st.write("Peran 4")
st.write("Penjelasan")
