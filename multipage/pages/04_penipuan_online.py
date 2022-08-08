import streamlit as st
from PIL import Image

# apply photo
image = Image.open(r"C:\group11\asset\banner.jpg", "r")
st.image(image)

st.title("PENIPUAN ONLINE")
st.markdown(
    """### Apa Itu Penipuan Online? :right_anger_bubble:
            
**PENGERTIAN**

Penipuan online : Penggunaan layanan internet atau software dengan akses internet untuk menipu atau mengambil keuntungan dari korban, misalnya dengan mencuri informasi personal yang dapat memicu pencurian identitas.
    
""",
    unsafe_allow_html=True,
)
st.markdown(
    """### Data Penipuan Online
        
""",
    unsafe_allow_html=True,
)

# Picture about online scam files
image = Image.open(r"C:\group11\asset\penipuan.png", "r")
st.image(image, caption="created by group 11")

# Point about example of online scam
st.markdown(
    """### Kasus-kasus Penipuan Online
    
""",
    unsafe_allow_html=True,
)
with st.expander("Kasus-kasus Penipuan Online"):
    st.write(
        """
**:anger: Case 1 :anger:**

Anita senang berbelanja di marketplace. Suatu hari saat ingin berbelanja, si penjual mengajak bertransaksi di luar markerplace tersebut dan meminta Anita untuk langsung mentransfer uang ke rekeningnya. Anita kemudian mentransfer sejumlah uang kepada penjual namun barang yang dipesan tidak pernah dikirimkan.

**:anger: Case 2 :anger:**

Suatu hari, Wina mendapat telepon dari nomor tidak dikenal yang mengaku sebagai petugas rumah sakit. Dia mengabarkan bahwa salah satu anaknya masuk IGD dan harus segera mendapat perawatan. Agar dapat segera dirawat, Wina diminta untuk mentransfer sejumlah uang kepadanya terlebih dahulu. Karena panik, Wina menuruti permintaan tersebut. Namun setelah mentransfer uang, Wina baru sadar ternyata anaknya baik-baik saja.

**:anger: Case 3 :anger:**

Suatu hari, Yeni mendapat telepon yang mengaku sebagai CS bank tempatnya menyimpan uang. CS tersebut mengabarkan bahwa Yeni memperoleh hadiah undian dan diminta untuk menyebutkan data-data pribadinya, serta menyebutkan nomor OTP yang dikirim ke nomor hpnya. Beberapa saat kemudian, uang di rekeningnya habis tak bersisa.

**:anger: Case 4 :anger:**

Sinta mmenerima email dari bank yang memintanya untuk mengupdate data dan mengirimkan tautan. Di dalam tautan tersebut terdapat form yang harus diisi dengan username dan password m-bankingnya. Sinta merasa curiga dan menghubungi pihak bank. Ternyata, pihak bank tidak pernah mengirimkan email tersebut.
     """
    )

st.markdown(
    """### Apakah kamu merasa familiar dengan kasus-kasus tersebut atau pernah mengalaminya?
yuk, kenali lebih jauh tentang penipuan online!
    
""",
    unsafe_allow_html=True,
)

st.markdown(
    """### Modus Penipuan Online

Berbagai aktifitas kini dapat dilakukan secara online, tetapi di baliknya terdapat berbagai ancaman penipuan untuk memperoleh keuntungan dari para pengguna layanan online, seperti e-commerce, internet banking, investasi online, media sosial, dan lain sebagainya. Untuk itu, kita perlu mengetahui modus-modus yang digunakan dalam penipuan online dan bagaimana cara menghindarinya.
    
""",
    unsafe_allow_html=True,
)

# Point about the type of online scam
st.markdown(
    """### Jenis-jenis Penipuan Online
        
""",
    unsafe_allow_html=True,
)
with st.expander("Jenis-Jenis Penipuan Online"):
    st.write(
        """
         **:money_with_wings: SNIFFING :money_with_wings:**
         Sniffing menggunakan jaringan publik untuk mengambil data atau informasi sensitif secara ilegal. Ketika kita menggunakan jaringan publik seperti WIFI, maka terdapat celah bagi penipu untuk 
         
         **EMAIL PHISING**
         Dalam jenis penipuan ini, pelaku mengelabui korban dengan mengirimkan tautan ke email/media sosial yang akan mengarahkannya ke situs palsu. Korban kemudian diminta untuk memberikan informasi pribadi seperti username dan password yang kemudian disalahgunakan oleh pelaku.
         
         **PERETASAN**
         Aktivitas yang berupaya mengakses secara ilegal perangkat digital, seperti komputer, ponsel cerdas, tablet, akun media sosial, dan bahkan seluruh jaringan.
         
         **CYBER BULLYING**
         Penyalahgunaan internet untuk melecehkan, mengancam, mempermalukan, dan mengejek orang lain. Korban cyberbullying dapat mengalami kerugian secara fisik maupun mental.
         
         **CARDING**
         Modus tindakan kejahatan dalam transaksi menggunakan kartu kredit sesorang. Setelah mengetahui nomor kartu kredit calon korban, kemudian pelaku dapat berbelanja online melalui kartu kredit curian tersebut.
         
         **SPAMMING**
         Spamming adalah kegiatan mengirim email palsu dengan memanfaatkan server email yang memiliki ‘smtp open relay‘ atau spamming bisa juga diartikan dengan pengiriman informasi atau iklan suatu produk yang tidak pada tempatnya.
         
         **SKIMMING**
         Tindakan kejahatan pencurian data pengguna ATM untuk membobol rekening menggunakan alat khusus bernama scammer yang bentuknya mirip dengan mulut slot kartu ATM.
         
         **PENIPUAN ONLINE**
         Penggunaan layanan internet atau software dengan akses internet untuk menipu atau mengambil keuntungan dari korban, misalnya dengan mencuri informasi personal yang dapat memicu pencurian identitas.
         """
    )
