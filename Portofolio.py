import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Dewangga Megananda", page_icon="📂", layout="wide")

# Header
st.title("👋 Hello, i'm Dewangga Megananda")
st.subheader("Informatics Student | Cybersecurity Enthusiast | Data Analyst Enthusiast")

# Informasi Kontak
st.write("""
📍 **Address:** Tebet, South Jakarta  
📧 **Email:** dewangga.megananda13@gmail.com  
🔗 **LinkedIn:** [Dewangga Megananda](https://linkedin.com)
🔗 **YouTube:** [Dewangga Megananda](https://www.youtube.com/@DewanggaMegananda)
""")

# Foto Profil
image = Image.open("profile.jpg")  # Ganti dengan foto Anda
st.image(image, width=200)

# Tentang Saya
st.header("📝 SUMMARY")
st.write("""
An Informatics student with a strong passion for cybersecurity and a relentless drive to explore advancements in digital security. Equipped with sharp analytical skills, creative problem-solving abilities, and a keen eye for detail, I excel at identifying potential security risks effectively. My intuitive, authentic, and empathetic personality adds value in understanding user behavior and predicting potential vulnerabilities.
""")

# Pendidikan
st.header("🎓 EDUCATION")
st.write("""
**University of Gunadarma**  
Informatics Engineering | GPA 3.63
""")

# Pengalaman
st.header("💼 EXPERIENCE")
st.write("""
**Cyber Academy Indonesia – Student Course** (September 2022 – Present)  
📌 **Elastic Stack as SIEM**
- Conducted log analysis to investigate security incidents and improve system resilience against cyberattacks.

**Coding Studio – Student Course**  
📌 **WEB Penetration Testing with DVWA**
- Performed various attacks, including SQL Injection, Cross-Site Scripting (XSS), Command Injection, and CSRF, to understand common web security flaws.
""")

# Sertifikasi
st.header("📜 CERTIFICATIONS")
st.write("""
✅ **Pre-security Course**, Cyber Academy, No. PREC01103240669, 2024 
✅ **SOC Analyst Course**, Cyber Academy, No. CSOC01112244535, 2024  
✅ **Structured Query Language (SQL)**, Dicoding, No. MRZMN67WRPYQ, 2025  
✅ **Fundamental Cyber Security**, Coding Studio, No. UA3EKURADH, 2025  
✅ **Fundamental Penetration Testing**, Coding Studio, No. EAJX3YZFUI, 2025  
✅ **Fundamental Network Computer**, Coding Studio, No. EFXUS4C1EO, 2025  
""")

# Galeri Sertifikat
st.subheader("📜 Certificate Gallery")
cert_images = ["presec.jpg", "soc.jpg", "funcysec.jpg", "funnet.jpg", "funpen.jpg", "funsql.jpg"]
cert_captions = [
    "Pre-security Course - Cyber Academy",
    "SOC Analyst Course - Cyber Academy",
    "Fundamental Cyber Security - Coding Studio",
    "Fundamental Network Computer - Coding Studio",
    "Fundamental Penetration Testing - Coding Studio",
    "Structured Query Language (SQL) - Dicoding"
]

if 'cert_index' not in st.session_state:
    st.session_state.cert_index = 0

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️"):
        st.session_state.cert_index = (st.session_state.cert_index - 1) % len(cert_images)

with col3:
    if st.button("➡️"):
        st.session_state.cert_index = (st.session_state.cert_index + 1) % len(cert_images)

with col2:
    st.image(cert_images[st.session_state.cert_index], caption=cert_captions[st.session_state.cert_index], width=600)

# Kemampuan Tambahan
st.header("⚙️ ADDITIONAL SKILLS")
st.write("""
🔹 **Technical Skills:** Penetration Testing, Vulnerability Assessment & Management, Incident Response & Handling, SIEM Tools, Digital Forensics, Threat Intelligence, Malware Analysis, Operating Systems Security (Linux, Windows), DBMS, Data Analyst.  
🔹 **Personal Skills:** Critical Thinking, Analytical Thinking, Communication Skills, Continuous Learning, Time Management.  
🔹 **Tools:** Vscode, Elastic, VMWare, Oracle, Cisco.  
🔹 **Programming Languages:** Python, Php, C++, C, Java.  
🔹 **Languages:** Bahasa Indonesia, English.  
""")

# Proyek
st.header("📂 PROJECTS")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Analisis Data Kualitas Udara")
    st.write("Menganalisis tren polusi udara menggunakan teknik visualisasi dan Machine Learning.")
    st.image("analisis.jpg", use_column_width=True)
    st.markdown("[Lihat di GitHub](https://github.com/nanda910/Analisis-Data-Kualitas-Udara)")
    st.markdown("[Lihat di Streamlit](https://dewanggamegananda.streamlit.app/)")

with col2:
    st.subheader("🤖 Antrian Puskesmas")
    st.write("Sistem Antrian Puskesmas berbasis WEB.")
    st.image("antrian.jpg", use_column_width=True)
    st.markdown("[Lihat di GitHub](https://github.com/nanda910/Antrian_Puskesmas)")

# Kontak
st.header("📬 CONTACT ME")
contact_form = """
<form action="https://formsubmit.co/dewangga.megananda13@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Nama Anda" required>
    <input type="email" name="email" placeholder="Email Anda" required>
    <textarea name="message" placeholder="Pesan Anda" required></textarea>
    <button type="submit">Kirim</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Tambahkan CSS untuk styling
st.markdown("""
<style>
    input, textarea { width: 100%; padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc; }
    button { background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; }
    button:hover { background-color: #45a049; }
</style>
""", unsafe_allow_html=True)
