# resume_matcher.py

import re
from collections import Counter

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

def keyword_match_score(resume_text, job_description):
    resume_words = preprocess(resume_text)
    job_words = preprocess(job_description)

    resume_counter = Counter(resume_words)
    job_counter = Counter(job_words)

    common_keywords = set(resume_counter.keys()) & set(job_counter.keys())
    
    score = sum(min(resume_counter[word], job_counter[word]) for word in common_keywords)
    total_keywords = sum(job_counter.values())

    match_percentage = (score / total_keywords) * 100 if total_keywords > 0 else 0

    return round(match_percentage, 2), common_keywords


if __name__ == "__main__":
    resume = """
    Python developer with experience in machine learning, deep learning,
    NLP, data analysis, and web development.
    """

    job_description = """
    Looking for a Python developer skilled in machine learning,
    NLP, and data engineering.
    """

    score, keywords = keyword_match_score(resume, job_description)

    print(f"Match Score: {score}%")
    print("Matched Keywords:", keywords)
