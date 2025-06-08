# ResumeRanker
ResumeRanker – AI Resume Matching Tool
# 📄 ResumeRanker

**ResumeRanker** is an intelligent web-based system designed to evaluate resumes against job descriptions using advanced Natural Language Processing (NLP) techniques such as TF-IDF and cosine similarity. It provides a match score, identifies missing skills, and generates downloadable PDF feedback reports.

---

## 🚀 Features

- Upload resume (PDF) and paste job description
- Extract text from resumes and analyze relevance
- Calculate similarity score using TF-IDF & cosine similarity
- Keyword & skill extraction from resume and job description
- Feedback on missing skills
- Generate downloadable PDF report with match score & skill gap
- Preview uploaded resume in-browser
- 🆕 PDF Text Quality Enhancer
- 🧠 REST API Support for External Integrations
- 🧩 Skill Suggestion Module using GPT/NLP (Coming Soon)

---

## 🧠 Bonus Resources (Learning Section)

### 📚 Learning Courses (From `Course.py`)

#### Data Science
- [ML Crash Course by Google (Free)](https://developers.google.com/machine-learning/crash-course)
- [Machine Learning by Andrew NG](https://www.coursera.org/learn/machine-learning)
- [Data Scientist with Python – DataCamp](https://www.datacamp.com/tracks/data-scientist-with-python)

#### Web Development
- [Django Crash Course (Free)](https://youtu.be/e1IyzVyrLSU)
- [ReactJS Project Development Training](https://www.dotnettricks.com/training/masters-program/reactjs-certification-training)
- [Flask Web Development – Educative](https://www.educative.io/courses/flask-develop-web-applications-in-python)

#### Mobile App Development
- [Android Kotlin Development – Udacity](https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940)
- [iOS Swift Bootcamp](https://www.udemy.com/course/ios-13-app-development-bootcamp/)
- [Flutter & Dart Complete Course](https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/)

#### UI/UX Design
- [Google UX Design Certificate](https://www.coursera.org/professional-certificates/google-ux-design)
- [Adobe XD Tutorial (Free)](https://youtu.be/68w2VwalD5w)

---

## 🎥 Resume & Interview Prep

### Resume Building
- [How to Build a Great Resume](https://youtu.be/3agP4x8LYFM)

### Interview Preparation
- [Common Interview Questions & Tips](https://youtu.be/Tt08KmFfIYQ)

---

## 🛠️ Tech Stack

| Area                | Technology                  |
|---------------------|-----------------------------|
| Frontend            | Streamlit                   |
| Backend             | Python                      |
| NLP/ML              | TF-IDF, Cosine Similarity, NLTK, Scikit-learn |
| PDF Generation      | FPDF                        |
| Text Parsing        | PyPDF2                      |
| Image Handling      | PIL                         |

---

## 🧪 How to Run the Project

### Local Setup

```bash
git clone https://github.com/your-username/ResumeRanker.git
cd ResumeRanker
pip install -r requirements.txt
streamlit run app.py

ResumeRanker/
│
├── app.py
├── utils/
│   ├── course.py
│   └── ...
├── Logo/
│   └── logo2.png
├── Uploaded_Resumes/
│   └── [saved files]
├── requirements.txt
