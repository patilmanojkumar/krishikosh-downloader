import streamlit as st
from urllib.parse import unquote

def edit_url(url):
    # Extract the encoded path after "file="
    start_index = url.find("file=") + len("file=")
    encoded_path = url[start_index:]
    
    # Decode the encoded file path
    decoded_path = unquote(encoded_path)
    
    # The decoded path already contains the base URL, so no need to add it again
    return decoded_path

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
