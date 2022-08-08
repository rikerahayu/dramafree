def main_page():    
    st.markdown("#Main Page")
    st.sidebar.markdown("Main page")

def page_2():
    st.markdown("#Page 2")
    st.sidebar.markdown("Page 2")

def page_3():
    st.markdown("# Page 3")
    st.sidebar.markdown("Page 3")

def page_4():
    st.markdown("# Page 4")
    st.sidebar.markdown("Page 4")

def page_5():
    st.markdown("Page 5")
    st.sidebar("Page 5")

#apply photo
image = Image.open(r"group11/asset/banner.jpg", "r")
st.image(image)

st.title('Women In Tech - Group 11')
st.markdown(
   """### Haii teman-teman, selamat datang di dunia keamanan digital:wave:

**:right_anger_bubble: Tahukah kalian berapa jumlah pengguna internet di seluruh dunia dan berapa rata-rata waktu yang dihabiskan untuk mengakses internet? :right_anger_bubble:** 
 
""",
        unsafe_allow_html=True,
)

with st.expander("Data Pengguna Internet"):
    st.markdown(
        """**Data Pengguna Internet :bar_chart:**"""
    )
    
    data1, data2, data3, data4, data5 = st.columns(5)
    data1.metric("2018", "132, 7 Jt", "")
    data2.metric("2019", "150 Jt", "17, 3")
    data3.metric("2020", "175, 4 Jt", "25, 4")
    data4.metric("2021", "202, 6 Jt", "27,2")
    data5.metric("2022", "204, 7 Jt", "2, 1")

    st.write("sumber : https://databoks.katadata.co.id/datapublish/2022/03/23/ada-2047-juta-pengguna-internet-di-indonesia-awal-2022")

    st.markdown(
        """**Dapat dilihat dari data diatas bahwa setiap tahun ada peningkatan pengguna internet :arrow_up:	:arrow_up:	:arrow_up:**"""
    )

st.write("""Dengan makin banyaknya penggunaan komputer seperti desktop, laptop, smartphone, server, dan perangkat IoT (internet of things) serta penggunaan jaringan komputer seperti internet dalam kehidupan umat manusia sehari-hari. 
Hal ini memungkinkan bahwa akan semakin meningkat pula ancaman serangan oleh orang-orang yang tidak bertanggung jawab. 
Kerugian yang ditimbulkan oleh serangan tersebut juga akan menjadi besar apabila kita tidak mengetahui bahwa kita sedang dalam penyerangan orang-orang yang tidak bertanggung jawab.
Untuk itu, kami akan membantu kalian untuk mengenal apa itu kejahatan teknologi informasi (cybercrime), jenis-jenis cybercrime, serta cara menghindarinya.""")
