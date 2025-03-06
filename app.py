import streamlit as st
from utils import get_pdf_url

kursliste = get_pdf_url()
selection = st.selectbox("Wähle deine Umschulung aus:", list(get_pdf_url().keys()))
st.write(f"{kursliste[selection]}")

with open(f"KW10/{selection}-Berichtsheft-KW10.xlsx", "rb") as file:
    st.download_button(
        label="Download Berichtsheft",
        data=file,
        file_name=f"{selection}-Berichtsheft-KW10.xlsx",
        mime="application/pdf"
    )