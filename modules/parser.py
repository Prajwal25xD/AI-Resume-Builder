import fitz
import docx


def parse_pdf(file):

    text = ""

    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text



def parse_docx(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text



def parse_resume(file):

    if file.name.endswith(".pdf"):
        return parse_pdf(file)

    elif file.name.endswith(".docx"):
        return parse_docx(file)

    else:
        return "Unsupported file format"
