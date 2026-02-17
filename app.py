import streamlit as st

st.set_page_config(page_title="AI Resume Builder", layout="wide")

st.title("AI Resume Builder & ATS Optimizer")

st.write("App loaded successfully")

try:
    from modules.parser import parse_resume
    from modules.ats_model import predict_score
    from modules.enhancer_openai import enhance_resume
    from modules.generator import generate_docx

    st.success("All modules imported successfully")

except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()


uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

if uploaded_file is not None:

    try:

        text = parse_resume(uploaded_file)

        st.subheader("Original Resume")
        st.write(text)

        score = predict_score(5,2,3)

        st.subheader("ATS Score")
        st.write(score)

        if st.button("Enhance Resume"):

            enhanced = enhance_resume(text)

            st.subheader("Enhanced Resume")
            st.write(enhanced)

            path = generate_docx(enhanced)

            with open(path,"rb") as f:
                st.download_button(
                    "Download Resume",
                    f,
                    file_name="enhanced_resume.docx"
                )

    except Exception as e:

        st.error(f"Error: {e}")

else:

    st.warning("Please upload a resume file.")
