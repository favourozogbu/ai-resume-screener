# AI Resume Screening Web App

A lightweight tool that compares a candidate's resume against a job description using NLP and machine learning techniques. Designed for recruiters and developers to evaluate resume relevance based on keyword similarity.

## Features

- Parse resumes in PDF format and job descriptions in TXT
- Compute a match score using TF-IDF vectorization and cosine similarity
- Simple CLI interface with easy execution
- Classifies the match as Strong, Moderate, or Weak

## How It Works
1. Admin uploads a job description
2. Users upload resumes (PDF)
3. NLP engine parses and ranks resumes
4. Results are displayed with matching scores

## Tech Stack
- **Frontend:** React
- **Backend:** Node.js, Express
- **AI/NLP:** Python, spaCy, Scikit-learn
- **Storage:** Local or MongoDB (optional)
- **Deployment:** Localhost or cloud

## File Structure

```
ai-resume-screener/
├── ai_resume_screener_main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
2. Create a virtual environment (optional)
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python ai_resume_screener_main.py --resume path/to/resume.pdf --job path/to/job_description.txt
```

## Output

- Match Score: [0–100]%
- Match Category: Strong 🟢 / Moderate 🟡 / Weak 🔴

## Example

```bash
python ai_resume_screener_main.py --resume resumes/john_doe.pdf --job jobs/software_engineer.txt
```

## Upcoming Future Improvements
- Add candidate dashboard
- Improve ML model with larger datasets
- Integrate third-party resume parsing APIs

## 👨‍💻 Author's Contact   
**For collaboration or freelance work:**

**Favour S. Ozogbu**   
📧 favoursozogbu@gmail.com  
🔗 [GitHub](https://github.com/favourozogbu)
🔗 [LinkedIn](https://www.linkedin.com/in/favourozogbu)









