import streamlit as st
from utils import get_pdf_url

kursliste = get_pdf_url()
selection = st.selectbox("Wähle deine Umschulung aus:", list(get_pdf_url().keys()))
st.write(f"{kursliste[selection]}")

