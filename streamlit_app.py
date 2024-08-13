import streamlit as st
from urllib.parse import unquote

def edit_url(url):
    try:
        # Ensure that the URL contains the necessary parts
        if "file=" not in url or "content" not in url:
            raise ValueError("The URL is not in the expected format.")
        
        # Extract the encoded path after "file="
        start_index = url.find("file=") + len("file=")
        
        # Find the position where 'content' starts
        end_index = url.find("content") + len("content")
        
        # Ensure that the positions make sense
        if start_index >= end_index:
            raise ValueError("The URL is not in the expected format.")
        
        # Extract the encoded file path from start_index to end_index
        encoded_path = url[start_index:end_index]
        
        # Decode the encoded file path
        decoded_path = unquote(encoded_path)
        
        # The decoded path already contains the base URL, so no need to add it again
        return decoded_path
    except ValueError as ve:
        st.error(f"Error: {ve}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

# Streamlit app UI
st.markdown(
    "<h1 style='text-align: center; font-size: 32px;'>Krishikosh Downloader by <a href='https://github.com/patilmanojkumar'>Manojkumar Patil</a></h1>",
    unsafe_allow_html=True
)

# Displaying the dynamic SVG banner
st.markdown(
    """
    <p align="center">
      <a href="https://github.com/DenverCoder1/readme-typing-svg">
        <img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=yellow&size=30&center=true&vCenter=true&width=600&height=100&lines=Download+Thesis+From+Krishikosh!;" alt="Typing SVG">
      </a>
    </p>
    """,
    unsafe_allow_html=True
)

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
            st.success("Link Generated successfully! Click the link below to download the file.")
            st.markdown(f"[Download File]({edited_url})", unsafe_allow_html=True)
        else:
            st.error("The URL you provided does not appear to be in the correct format. Please try again.")
    else:
        st.warning("Please enter a URL to proceed.")
