import streamlit as st
from utils import get_pdf_url, kalenderwoche

kalenderwoche = kalenderwoche()
kursliste = get_pdf_url()
selection = st.selectbox("Wähle deine Umschulung aus:", list(get_pdf_url().keys()))
st.write(f"{selection}")

with open(f"KW{kalenderwoche}/{selection}-Berichtsheft_KW{kalenderwoche}.xlsx", "rb") as file:
    st.download_button(
        label="Download Berichtsheft",
        data=file,
        file_name=f"Berichtsheft-KW{kalenderwoche}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )