import streamlit as st
import requests

# the simple logic of website

st.title("LLM for PDF")

st.write("This is a demo for the LLM for PDF project.")

st.write("There is two way to handle the PDF file: 1. Upload the PDF file 2. Input the PDF files' uel.")



upload_pdf = st.file_uploader("Upload some PDFs", type=["pdf"], accept_multiple_files = True)








if st.button("Submit"):
    if upload_pdf:
        print(upload_pdf)
        st.success("Successfully submitted!!!")
            
    else:
        st.error("Please upload at least one PDF file.")



if 'urls' not in st.session_state:
    st.session_state.urls = []

per_url = st.text_input("Enter the URL of the PDF file", key="url_input")

col1, col2 = st.columns([1, 6])
with col1:
    add_clicked = st.button("Add URL")
with col2:
    finish_clicked = st.button("Finish")

if add_clicked:
    if per_url:
        if not (per_url.startswith('http://') or per_url.startswith('https://')):
            st.error("Please enter a valid URL starting with http:// or https://")
        else:
            st.session_state.urls.append(per_url)
            st.session_state.url_input = ""
            st.rerun()
    else:
        st.error("URL cannot be empty.")

if st.session_state.urls:
    st.subheader("Added URLs:")
    for idx, url in enumerate(st.session_state.urls, 1):
        st.write(f"{idx}. {url}")

if finish_clicked:
    if not st.session_state.urls:
        st.error("Please add at least one URL before finishing.")
    else:
        st.success("Successfully submitted following URLs:")
        for url in st.session_state.urls:
            st.write(f"• {url}")



