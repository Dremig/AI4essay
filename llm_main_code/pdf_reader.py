import pdfplumber
from pathlib import Path
import requests
from io import BytesIO
from urllib.parse import urlparse

def extract_pdf_content(pdf_path: str) -> str:
    # file exists?
    if not Path(pdf_path).exists():
        raise FileNotFoundError(f"PDF file not exist: {pdf_path}")
    
    # file type
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError("the type of the file should be PDF")

    full_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:  
                    full_text.append(page_text.strip())
    
    except Exception as e:
        raise RuntimeError(f"Fail to read file: {str(e)}") from e
    
    return "\n\n".join(full_text)



def extract_online_pdf(url: str, timeout: int = 10) -> str:
    parsed = urlparse(url)
    if not parsed.scheme in ("http", "https"):
        raise ValueError("only http or https is supported")

    try:
        # download pdf stream
        with requests.get(url, stream=True, timeout=timeout) as response:
            response.raise_for_status()
            
            content_type = response.headers.get('Content-Type', '')
            if 'application/pdf' not in content_type:
                raise ValueError("the url dos not return any pdf file")

            with BytesIO(response.content) as pdf_buffer:
                full_text = []
                with pdfplumber.open(pdf_buffer) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            full_text.append(text.strip())
                return "\n\n".join(full_text)
                
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Internet error: {str(e)}") from e

