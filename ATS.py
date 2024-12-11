# # # import re
# # # import os
# # # from PyPDF2 import PdfReader
# # # from docx import Document
# # # import spacy
# # # from collections import Counter
# # # import docx 


# # # # Load NLP model
# # # nlp = spacy.load("en_core_web_sm")

# # # # Predefined criteria
# # # JOB_CRITERIA = {
# # #     "keywords": ["Python", "Machine Learning", "Data Analysis", "Team Collaboration", "Project Management"],
# # #     "skills": ["Python", "SQL", "Data Visualization", "Problem Solving", "Communication"],
# # #     "education": ["B.Tech", "MCA", "Computer Science"],
# # #     "format_issues": ["tables", "images", "complex formatting"]
# # # }

# # # # Function to extract text from PDF
# # # def extract_text_from_pdf(filepath):
# # #     reader = PdfReader(filepath)
# # #     text = ""
# # #     for page in reader.pages:
# # #         text += page.extract_text()
# # #     return text

# # # # Function to extract text from Word document
# # # def extract_text_from_docx(filepath):
# # #     doc = Document(filepath)
# # #     return "\n".join([p.text for p in doc.paragraphs])

# # # # Function to parse and analyze resume
# # # def analyze_resume(filepath):
# # #     # Extract text
# # #     if filepath.endswith(".pdf"):
# # #         text = extract_text_from_pdf(filepath)
# # #     elif filepath.endswith(".docx"):
# # #         text = extract_text_from_docx(filepath)
# # #     else:
# # #         raise ValueError("Unsupported file format!")
    
# # #     doc = nlp(text)
    
# # #     # Analysis results
# # #     results = {
# # #         "keyword_matches": [],
# # #         "missing_keywords": [],
# # #         "skills_matches": [],
# # #         "missing_skills": [],
# # #         "education_matches": [],
# # #         "missing_education": [],
# # #         "format_issues": []
# # #     }
    
# # #     # Keyword matching
# # #     resume_keywords = [token.text.lower() for token in doc]
# # #     for keyword in JOB_CRITERIA["keywords"]:
# # #         if keyword.lower() in resume_keywords:
# # #             results["keyword_matches"].append(keyword)
# # #         else:
# # #             results["missing_keywords"].append(keyword)
    
# # #     # Skill matching
# # #     for skill in JOB_CRITERIA["skills"]:
# # #         if skill.lower() in resume_keywords:
# # #             results["skills_matches"].append(skill)
# # #         else:
# # #             results["missing_skills"].append(skill)
    
# # #     # Education matching
# # #     resume_text = text.lower()
# # #     for edu in JOB_CRITERIA["education"]:
# # #         if edu.lower() in resume_text:
# # #             results["education_matches"].append(edu)
# # #         else:
# # #             results["missing_education"].append(edu)
    
# # #     # Format check (basic example)
# # #     if "table" in resume_text or "image" in resume_text:
# # #         results["format_issues"].append("Contains tables or images")
    
# # #     return results, text

# # # # Function to calculate score
# # # def calculate_score(results):
# # #     total_criteria = sum(len(v) for k, v in JOB_CRITERIA.items() if k != "format_issues")
# # #     matched_criteria = len(results["keyword_matches"]) + len(results["skills_matches"]) + len(results["education_matches"])
# # #     score = (matched_criteria / total_criteria) * 100
# # #     return round(score, 2)

# # # # Function to generate feedback
# # # def generate_feedback(results, output_path="feedback.txt"):
# # #     feedback = []
# # #     if results["missing_keywords"]:
# # #         feedback.append(f"Missing Keywords: {', '.join(results['missing_keywords'])}")
# # #     if results["missing_skills"]:
# # #         feedback.append(f"Missing Skills: {', '.join(results['missing_skills'])}")
# # #     if results["missing_education"]:
# # #         feedback.append(f"Missing Education: {', '.join(results['missing_education'])}")
# # #     if results["format_issues"]:
# # #         feedback.append(f"Formatting Issues: {', '.join(results['format_issues'])}")
    
# # #     with open(output_path, "w") as f:
# # #         f.write("\n".join(feedback))
# # #     return output_path

# # # # Main function
# # # def ats_algorithm(filepath):
# # #     results, _ = analyze_resume(filepath)
# # #     score = calculate_score(results)
# # #     feedback_file = generate_feedback(results)
# # #     return score, feedback_file

# # # # Usage
# # # resume_file = "resume.pdf"  # Replace with your resume file path
# # # try:
# # #     score, feedback_path = ats_algorithm(resume_file)
# # #     print(f"Resume Score: {score}%")
# # #     print(f"Feedback saved to: {feedback_path}")
# # # except Exception as e:
# # #     print(f"Error: {e}")




# # import re

# # string1 = """Hello! My name is John Doe, and my email is john.doe@example.com. I live in California, USA, and my phone number is +1-555-123-4567. 
# # I recently made a purchase on 2024-12-10 for $123.45 from Amazon. My order ID was #ORD12345.
# # I have a second email address, john_alt123@example.org, which I use for work. 
# # My website is https://johndoe.dev, and you can follow me on Twitter @JohnD123.
# # Sometimes, I also write blogs on topics like Python, JavaScript, \n and AI"""

# # strpattern = r"\d{5}"
# # res = re.search(strpattern,string1)
# # print(f"{type(res)},{res}")

# # string2= "a" *458

# # print(len(string2))
# # res= re.fullmatch(r".{458}",string2)
# # if res != None:
# #     print(res)
# # else:
# #     print("No match found")


# # print("--------------------------------XXXXXXXXXX----------------------------------")


# # split_ex = string1.split()
# # print("Split string is  --> ", split_ex)
# # print(len(split_ex))

# # res1 = re.split(r"\s",string1)
# # print("--------------------------------XXXXXXXXXX----------------------------------")
# # print(res1)
# # print(len(res1))


# import re

# subject_string = """
# John Doe: 123-456-7890 | jane_doe@example.com | Order ID: ORD-45231
# Invoice Date: 2023-11-23 | Total: $1,250.00 | Website: https://example.com
# File list: report1.pdf, summary.txt, temp_report.txt, image.png
# Errors: ERR-1001, ERR-2002 (Critical), ERR-3003 (Ignored)
# """
# # email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# email_pattern = r'([a-zA-Z0-9._%+-]+)@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# val_email = re.search(email_pattern,subject_string)

# if val_email :
#     print(val_email.group())


# name_pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+'
# name_match = re.match(name_pattern, subject_string)
# if name_match:
#     print("Valid Name Found at Start:", name_match.group())
# else:
#     print("No valid name at the start.")


# order_id_pattern = r'ORD-\d+'
# order_ids = re.findall(order_id_pattern, subject_string)
# print("Order IDs Found:", order_ids)


# print("-------------------------------------********************************-------------------------------------")

# error_pattern = r'ERR-\d+'
# replace_error = re.sub(error_pattern,"[ERROR]",subject_string)
# print(replace_error)

# print("-------------------------------------********************************-------------------------------------")

# anonymous_email = re.sub(email_pattern,r'\1@hidden.com',subject_string)
# print(anonymous_email)
