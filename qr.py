import streamlit as st
import qrcode as qr

def generate_qr_code(url, filename):
    img = qr.make(url)
    img.save(filename)

st.title('QR Code Generator')
website_url = st.text_input("Enter the URL of the website:")
filename = st.text_input("Enter the name of the generated image:")

if st.button("Generate QR Code"):
    generate_qr_code(website_url, filename + '.png')
    st.success('QR code generated successfully')
    st.image(filename + '.png')
