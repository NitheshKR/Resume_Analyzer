# 📄 Smart Resume Analyzer (NLP + Machine Learning)

## 🔗 Live Demo
👉 https://resumeanalyzer-6yxrcngiiagznrsrjwapuz.streamlit.app/

---

## 📌 Project Overview
The Smart Resume Analyzer is a web-based application that analyzes resumes and compares them with job descriptions using Natural Language Processing (NLP) and Machine Learning techniques. It helps in identifying skill gaps, matching skills, and predicting suitable job roles.

---

## 🎯 Objectives
- Extract text from resumes (PDF)
- Perform NLP preprocessing
- Identify candidate skills
- Compare with job requirements
- Calculate match score
- Suggest suitable job role

---

## ⚙️ Technologies Used
- Python
- NLP (Text Processing)
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit (UI)
- Scikit-learn
- NLTK
- PDFPlumber

---

## 🧠 Working Methodology

### 1. Resume Parsing
- Extract text from PDF using PDFPlumber

### 2. Text Preprocessing
- Lowercasing
- Removing punctuation
- Stopword removal

### 3. Skill Extraction
- Rule-based matching using predefined skill dictionary

### 4. Skill Matching
- Compare resume skills with job description
- Identify:
  - Matched skills
  - Missing skills

### 5. Machine Learning (TF-IDF)
- Convert text into numerical vectors
- Compute similarity using cosine similarity

### 6. Final Score Calculation
- Combine:
  - Skill-based score
  - ML-based similarity score

### 7. Role Prediction
- Predict best-fit role based on skill overlap

---

## 📊 Features
- Upload resume (PDF)
- Enter job description
- Skill match analysis
- Missing skill detection
- Role prediction
- Score visualization

---

## 🖥️ User Interface
Built using Streamlit:
- File uploader
- Text input
- Result display with scores

---

## 📈 Sample Output
- Predicted Role: Machine Learning Engineer
- Matched Skills: Python, ML, DL
- Missing Skills: SQL, Data Analysis
- Final Score: 54%

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
