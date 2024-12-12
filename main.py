from functions import load_job_criteria, analyze_resume, calculate_score, generate_feedback,generate_appreciation

def ats_algorithm(filepath, job_criteria_path="job_criteria.json"):
    job_criteria = load_job_criteria(job_criteria_path)
    results, text = analyze_resume(filepath, job_criteria)
    score = calculate_score(results, job_criteria)
    feedback_file = generate_feedback(results)
    appreciation_file = generate_appreciation(results)
    return score, feedback_file

# Usage
resume_file = r'C:\Users\ILG2KOR\Desktop\Documents\Aashutosh_Resume.pdf'  # Replace with your resume file path
try:
    score, feedback_path = ats_algorithm(resume_file)
    print(f"Resume Score: {score}%")
    print(f"Feedback saved to: {feedback_path}")
except Exception as e:
    print(f"Error: {e}")
