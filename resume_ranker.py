import streamlit as st
import base64
import time
from PIL import Image
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fpdf import FPDF
import os

# ---------- Utility Functions ----------

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def calculate_similarity(resume_text, job_description):
    documents = [resume_text, job_description]
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity_score * 100, 2)

def extract_skills(text):
    skill_keywords = [
        'python', 'java', 'sql', 'excel', 'communication', 'teamwork', 'leadership',
        'data analysis', 'machine learning', 'deep learning', 'django', 'flask',
        'nlp', 'cloud', 'aws', 'azure', 'git', 'linux', 'html', 'css', 'javascript', 'react'
    ]
    found = [skill for skill in skill_keywords if skill in text.lower()]
    return found

def generate_pdf_report(name, score, missing_skills):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resume Analysis Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Candidate Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Match Score: {score}%", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt="Missing Skills:", ln=True)
    if missing_skills:
        for skill in missing_skills:
            pdf.cell(200, 10, txt=f"- {skill}", ln=True)
    else:
        pdf.cell(200, 10, txt="None", ln=True)

    report_path = f"./{name}_Resume_Report.pdf"
    pdf.output(report_path)
    return report_path

def get_download_link(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(file_path)}">📥 Download Resume Report</a>'

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# ---------- Streamlit App ----------

st.set_page_config(page_title="ResumeRanker", layout="centered")

# Display Logo
if os.path.exists('./Logo/logo2.png'):
    img = Image.open('./Logo/logo2.png')
    st.image(img, width=120)

st.title("📄 ResumeRanker - AI Resume Matching Tool")
st.markdown("Upload your resume and paste a job description to get a match score, missing skills, and a downloadable report.")

# Input Fields
name = st.text_input("👤 Your Name")
uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF)", type=['pdf'])
job_desc = st.text_area("📝 Paste Job Description")

# Create directory for resumes if it doesn't exist
os.makedirs("./Uploaded_Resumes", exist_ok=True)

if uploaded_file:
    save_path = f"./Uploaded_Resumes/{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.subheader("📄 PDF Resume Preview")
    show_pdf(save_path)

if uploaded_file and job_desc and name:
    with st.spinner("🔍 Analyzing resume..."):
        time.sleep(2)
        resume_text = extract_text_from_pdf(uploaded_file)

        # Show extracted text
        st.subheader("📃 Extracted Resume Text")
        st.text_area("Below is the extracted text from your uploaded resume:", resume_text, height=300)

        # Match score & skill comparison
        similarity = calculate_similarity(resume_text, job_desc)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_desc)
        missing_skills = list(set(jd_skills) - set(resume_skills))

        # Output results
        st.subheader("📊 Match Results")
        st.success(f"✅ Resume Match Score: **{similarity}%**")

        if missing_skills:
            st.warning("🚨 Missing Skills from Resume:")
            for skill in missing_skills:
                st.markdown(f"- {skill}")
        else:
            st.success("✅ All job-required skills are present in your resume!")

        # Report download
        st.subheader("📁 Report")
        report_path = generate_pdf_report(name, similarity, missing_skills)
        download_link = get_download_link(report_path)
        st.markdown(download_link, unsafe_allow_html=True)
else:
    st.info("📌 Please enter your name, upload a resume, and paste a job description.")
