
import argparse
import fitz  # PyMuPDF
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read()


def compute_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)


def main(resume_path, job_path):
    resume_text = extract_text_from_pdf(resume_path)
    job_text = extract_text_from_txt(job_path)
    score = compute_similarity(resume_text, job_text)
    print(f"Match Score: {score}%")
    if score >= 75:
        print("🟢 Strong Match")
    elif score >= 50:
        print("🟡 Moderate Match")
    else:
        print("🔴 Weak Match")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Resume Screener")
    parser.add_argument("--resume", required=True, help="Path to resume PDF")
    parser.add_argument("--job", required=True, help="Path to job description TXT")
    args = parser.parse_args()
    main(args.resume, args.job)
