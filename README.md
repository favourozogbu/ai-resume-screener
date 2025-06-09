# 🧠 AI Resume Screener

A lightweight tool that compares a candidate's resume against a job description using NLP and machine learning techniques. Designed for recruiters and developers to evaluate resume relevance based on keyword similarity.

## 🚀 Features

- Parse resumes in PDF format and job descriptions in TXT
- Compute a match score using TF-IDF vectorization and cosine similarity
- Simple CLI interface with easy execution
- Classifies the match as Strong, Moderate, or Weak

## 📂 File Structure

```
ai-resume-screener/
├── ai_resume_screener_main.py
├── requirements.txt
└── README.md
```

## 🔧 Installation

1. Clone the repository
2. Create a virtual environment (optional)
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python ai_resume_screener_main.py --resume path/to/resume.pdf --job path/to/job_description.txt
```

## 💡 Output

- Match Score: [0–100]%
- Match Category: Strong 🟢 / Moderate 🟡 / Weak 🔴

## 📌 Example

```bash
python ai_resume_screener_main.py --resume resumes/john_doe.pdf --job jobs/software_engineer.txt
```

## 👨‍💻 Author

**Favour S. Ozogbu**  
📧 favoursozogbu@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/favourozogbu)