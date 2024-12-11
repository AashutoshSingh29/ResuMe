import re
import os
import json
from PyPDF2 import PdfReader
from docx import Document
import spacy
from collections import Counter
import docx

# Load NLP model
nlp = spacy.load("zh_core_web_sm")

# Load job criteria from JSON file
def load_job_criteria(json_path=r'C:\Users\ILG2KOR\Desktop\CERTIFICATES\assignment2\ATS_Project\job_criteria.json'):
    with open(json_path, "r") as f:
        return json.load(f)

# Function to extract text from PDF
def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from Word document
def extract_text_from_docx(filepath):
    doc = Document(filepath)
    return "\n".join([p.text for p in doc.paragraphs])

# Function to parse and analyze resume
def analyze_resume(filepath, job_criteria):
    # Extract text
    if filepath.endswith(".pdf"):
        text = extract_text_from_pdf(filepath)
    elif filepath.endswith(".docx"):
        text = extract_text_from_docx(filepath)
    else:
        raise ValueError("Unsupported file format!")
    
    doc = nlp(text)
    
    # Analysis results
    results = {
        "keyword_matches": [],
        "missing_keywords": [],
        "skills_matches": [],
        "missing_skills": [],
        "education_matches": [],
        "missing_education": [],
        "format_issues": []
    }
    
    # Keyword matching
    resume_keywords = [token.text.lower() for token in doc]
    for keyword in job_criteria["keywords"]:
        if keyword.lower() in resume_keywords:
            results["keyword_matches"].append(keyword)
        else:
            results["missing_keywords"].append(keyword)
    
    # Skill matching
    for skill in job_criteria["skills"]:
        if skill.lower() in resume_keywords:
            results["skills_matches"].append(skill)
        else:
            results["missing_skills"].append(skill)
    
    # Education matching
    resume_text = text.lower()
    for edu in job_criteria["education"]:
        if edu.lower() in resume_text:
            results["education_matches"].append(edu)
        else:
            results["missing_education"].append(edu)
    
    # Format check (basic example)
    if "table" in resume_text or "image" in resume_text:
        results["format_issues"].append("Contains tables or images")

    # Add social details check
    social_results = socialCheck(text, json_path=r'C:\Users\ILG2KOR\Desktop\CERTIFICATES\assignment2\ATS_Project\job_criteria.json')
    results.update(social_results)

    return results, text

# Function to check social contact details in the resume
def socialCheck(text, json_path="job_criteria.json"):
    # Load social patterns from the JSON file
    def load_social_patterns(json_path):
        with open(json_path, "r") as f:
            criteria = json.load(f)
        return criteria.get("social_patterns", {})

    social_patterns = load_social_patterns(json_path)

    # Initialize results dictionary
    results = {
        "email": [],
        "phone": [],
        "linkedin": [],
        "github": [],
        "missing_email": False,
        "missing_phone": False
    }

    # Check for matches using the loaded patterns
    for key, pattern in social_patterns.items():
        matches = re.findall(pattern, text)
        results[key] = matches
        
        # Set flags for missing email and phone
        if key == "email" and not matches:
            results["missing_email"] = True
        if key == "phone" and not matches:
            results["missing_phone"] = True

    return results

# Function to calculate score
def calculate_score(results, job_criteria):
    total_criteria = sum(len(v) for k, v in job_criteria.items() if k != "format_issues")
    matched_criteria = len(results["keyword_matches"]) + len(results["skills_matches"]) + len(results["education_matches"])

  # Add points for social components
    social_points = 0
    if not results.get("missing_email", True):
        social_points += 1
    if not results.get("missing_phone", True):
        social_points += 1
    if not results.get("missing_linkedin", True):
        social_points += 1
    if not results.get("missing_github", True):
        social_points += 1

    matched_criteria += social_points
    total_criteria += 4  # Account for social components in total criteria

    score = (matched_criteria / total_criteria) * 100
    return round(score, 2)

# Function to generate feedback
def generate_feedback(results, output_path="feedback.txt"):
    feedback = []
    if results["missing_keywords"]:
        feedback.append(f"Missing Keywords: {', '.join(results['missing_keywords'])}")
    if results["missing_skills"]:
        feedback.append(f"Missing Skills: {', '.join(results['missing_skills'])}")
    if results["missing_education"]:
        feedback.append(f"Missing Education: {', '.join(results['missing_education'])}")
    if results["format_issues"]:
        feedback.append(f"Formatting Issues: {', '.join(results['format_issues'])}")

    # Social feedback
    if results.get("missing_email", True):
        feedback.append("Missing Email: Include your email address in the resume.")
    if results.get("missing_phone", True):
        feedback.append("Missing Phone Number: Include your phone number in the resume.")

    with open(output_path, "w") as f:
        f.write("\n".join(feedback))
    return output_path

# Main function
def ats_algorithm(filepath, job_criteria_path="job_criteria.json"):
    job_criteria = load_job_criteria(job_criteria_path)
    results, text = analyze_resume(filepath, job_criteria)
    score = calculate_score(results, job_criteria)
    feedback_file = generate_feedback(results)
    return score, feedback_file

# Usage
resume_file = r'C:\Users\ILG2KOR\Desktop\Documents\Aashutosh_Resume.pdf'  # Replace with your resume file path
try:
    score, feedback_path = ats_algorithm(resume_file)
    print(f"Resume Score: {score}%")
    print(f"Feedback saved to: {feedback_path}")
except Exception as e:
    print(f"Error: {e}")
