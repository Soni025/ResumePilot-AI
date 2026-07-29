import streamlit as st
from dotenv import load_dotenv
import os
import PyPDF2
import io
import openai  # Using correct OpenAI SDK

# Load environment variables
load_dotenv()

# Set Streamlit config
st.set_page_config(page_title="AI Resume Critiquer", page_icon=":guardsman:", layout="centered")
st.title("📝 AI Resume Critiquer")
st.markdown("Upload your resume and get **AI-powered feedback** tailored to your needs!")

# Get API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

# Optional job role input
job_role = st.text_input("Enter the job role you are applying for (optional)")

# Analyze button
analyze = st.button("Analyze Resume")

# PDF text extraction function
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

# General file text extractor
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    elif uploaded_file.type == "text/plain":
        return uploaded_file.getvalue().decode("utf-8")
    else:
        st.error("Unsupported file type.")
        return ""

# Main analysis logic
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            st.error("The uploaded file appears to be empty or unreadable.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
Focus on the following aspects:
1. Content clarity and impact
2. Skills presentation
3. Experience descriptions
4. Specific improvements for {job_role if job_role else 'general job applications'}

Resume content:
{file_content}

Please provide your analysis in a clear, structured format with specific recommendations.
"""

        with st.spinner("Analyzing your resume..."):
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Correct model name
                messages=[
                    {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )

        st.markdown("### 📊 Analysis Results")
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
