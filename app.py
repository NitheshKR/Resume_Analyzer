import streamlit as st
import pdfplumber
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# -------------------------------
# 📌 SKILL LIST
# -------------------------------
skills_list = [
    "python", "java", "c", "c++",
    "machine learning", "deep learning", "nlp",
    "cnn", "rnn", "lstm", "tensorflow", "keras",
    "data analysis", "data science", "sql",
    "pandas", "numpy", "matplotlib", "seaborn",
    "html", "css", "javascript",
    "react", "nodejs", "express",
    "embedded", "electronics", "microcontroller",
    "arduino", "raspberry pi", "vlsi", "verilog",
    "aws", "azure", "docker", "git", "github"
]

# -------------------------------
# 📌 FUNCTIONS
# -------------------------------

# Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

# Clean text
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace('•', ' ').replace('⋄', ' ')
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

# Extract skills
def extract_skills(text, skills_list):
    found_skills = []
    words = text.split()

    for skill in skills_list:
        skill_words = skill.split()

        if len(skill_words) == 1:
            if skill in words:
                found_skills.append(skill)
        else:
            if skill in text:
                found_skills.append(skill)

    return found_skills

# Match skills
def match_skills(resume_skills, job_skills):
    
    if len(job_skills) == 0:
        return 0, [], ["No recognizable job skills found"]
    
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    
    score = (len(matched) / len(job_skills)) * 100

    return score, matched, missing

# Role prediction
def suggest_role(skills):

    roles = {
        "Machine Learning Engineer": [
            "machine learning", "deep learning", "cnn", "rnn", "lstm"
        ],
        "Data Analyst": [
            "sql", "data analysis", "pandas", "numpy"
        ],
        "Web Developer": [
            "html", "css", "javascript", "react", "nodejs"
        ],
        "Embedded Engineer": [
            "embedded", "electronics", "microcontroller", "arduino"
        ],
        "Software Developer": [
            "c", "c++", "java", "python"
        ]
    }

    role_scores = {}

    for role, role_skills in roles.items():
        match_count = len(set(skills) & set(role_skills))
        role_scores[role] = match_count

    best_role = max(role_scores, key=role_scores.get)
    return best_role

# -------------------------------
# 📌 STREAMLIT UI
# -------------------------------

st.title("📄 Smart Resume Analyzer")
st.write("Upload your resume and compare with job description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description:

        # Extract text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Clean text
        clean_resume = clean_text(resume_text)
        clean_job = clean_text(job_description)

        # Extract skills
        resume_skills = extract_skills(clean_resume, skills_list)
        job_skills = extract_skills(clean_job, skills_list)

        # Match
        score, matched, missing = match_skills(resume_skills, job_skills)

        # TF-IDF
        docs = [clean_resume, clean_job]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(docs)

        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        ml_score = similarity[0][0] * 100

        final_score = (0.7 * score) + (0.3 * ml_score)

        # Role
        role = suggest_role(resume_skills)

        # OUTPUT
        st.subheader("📊 Analysis Result")

        st.write("### 🎯 Predicted Role")
        st.success(role)

        st.write("### ✅ Matched Skills")
        st.write(matched if matched else "None")

        st.write("### ❌ Missing Skills")
        st.write(missing if missing else "None")

        st.write(f"**Skill Score:** {score:.2f}%")
        st.write(f"**ML Score:** {ml_score:.2f}%")
        st.write(f"**Final Score:** {final_score:.2f}%")

    else:
        st.warning("Please upload resume and enter job description")
