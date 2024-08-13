import streamlit as st
from urllib.parse import unquote

def edit_url(url):
    try:
        # Extract the encoded path after "file="
        start_index = url.find("file=") + len("file=")
        encoded_path = url[start_index:]
        
        # Decode the encoded file path
        decoded_path = unquote(encoded_path)
        
        # The decoded path already contains the base URL, so no need to add it again
        return decoded_path
    except Exception:
        return None

# Streamlit app UI
st.title("Krishikosh Downloader")
st.markdown("**Easily download files from Krishikosh.**")

# Input field for the user to paste the URL
input_url = st.text_input("Paste the full-length Krishikosh URL here:")

# Instructions for the user
st.markdown("""
Please ensure that the URL you input follows the correct format:
- Example of correct URL: `https://krishikosh.egranth.ac.in/assets/pdfjs/web/viewer.html?file=https%3A%2F%2Fkrishikosh.egranth.ac.in%2Fserver%2Fapi%2Fcore%2Fbitstreams%2Fb8a091b0-6e12-43c1-8c29-63ba25519a43%2Fcontent`
- Incorrect URLs may not work as expected.
""")

# Single button to edit the URL and follow the link
if st.button("Download"):
    if input_url:
        edited_url = edit_url(input_url)
        if edited_url:
            # Provide a link to the edited URL that the user can click
            st.success("URL edited successfully! Click the link below to download the file.")
            st.markdown(f"[Download File]({edited_url})", unsafe_allow_html=True)
        else:
            st.error("The URL you provided does not appear to be in the correct format. Please try again.")
    else:
        st.warning("Please enter a URL to proceed.")
