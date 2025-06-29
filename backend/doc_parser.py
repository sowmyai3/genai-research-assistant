from io import BytesIO
from pdfminer.high_level import extract_text

def parse(uploaded_file) -> str:
    """Return full text from a PDF or TXT Streamlit UploadedFile."""
    if uploaded_file.type == "application/pdf":
        return extract_text(BytesIO(uploaded_file.read()))
    # plain-text path
    return uploaded_file.read().decode(errors="ignore")
