import streamlit as st
from urllib.parse import unquote

def edit_url(url):
    # Extract the base URL before the first occurrence of "/assets/pdfjs/web/viewer.html"
    base_url_end_index = url.find("/assets/pdfjs/web/viewer.html")
    base_url = url[:base_url_end_index]
    
    # Extract the encoded path after "file="
    start_index = url.find("file=") + len("file=")
    encoded_path = url[start_index:]
    
    # Decode the encoded file path
    decoded_path = unquote(encoded_path)
    
    # Construct the final URL
    final_url = f"{base_url}{decoded_path}"
    
    return final_url

# Streamlit app UI
st.title("URL Editor")

# Input field for the user to paste the URL
input_url = st.text_input("Paste the URL here:")

# Button to edit the URL
if st.button("Generate Edited URL"):
    if input_url:
        edited_url = edit_url(input_url)
        st.success("Here is your edited URL:")
        st.write(edited_url)
        
        # Button to go to the edited URL
        st.markdown(f"[Go to Edited URL]({edited_url})", unsafe_allow_html=True)
