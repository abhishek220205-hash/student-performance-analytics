import numpy as np
import pandas as pd

SUBJECT_COLS = ["Python", "SQL", "HTML", "CSS", "JavaScript"]

def calculate_totals_and_averages(df, subject_cols=SUBJECT_COLS):
    """Calculate total and average marks for each student using NumPy."""
    marks_matrix = df[subject_cols].values
    totals = np.sum(marks_matrix, axis=1)
    averages = np.round(np.mean(marks_matrix, axis=1), 2)
    return totals, averages

def assign_grade(avg_marks):
    """Assign letter grade based on average marks using if-elif-else rules."""
    if avg_marks >= 90:
        return "A+"
    elif avg_marks >= 80:
        return "A"
    elif avg_marks >= 70:
        return "B"
    elif avg_marks >= 60:
        return "C"
    elif avg_marks >= 50:
        return "D"
    else:
        return "F"

def check_pass_fail(avg_marks, attendance):
    """Identify Pass/Fail status based on average marks (>=50) and attendance (>=75%)."""
    if avg_marks >= 50 and attendance >= 75.0:
        return "Pass"
    else:
        return "Fail"

def evaluate_students(df):
    """Iterate through student records using a for loop to assign grades and pass/fail status."""
    grades = []
    results = []
    for i in range(len(df)):
        avg = df.iloc[i]["Average"]
        att = df.iloc[i]["Attendance"]
        grades.append(assign_grade(avg))
        results.append(check_pass_fail(avg, att))
    return grades, results

def get_subject_wise_analysis(df, subject_cols=SUBJECT_COLS):
    """Compute subject-wise mean, highest, and lowest marks using NumPy."""
    marks_matrix = df[subject_cols].values
    subj_means = np.round(np.mean(marks_matrix, axis=0), 2)
    subj_max = np.max(marks_matrix, axis=0)
    subj_min = np.min(marks_matrix, axis=0)
    
    analysis_df = pd.DataFrame({
        "Subject": subject_cols,
        "Average_Marks": subj_means,
        "Highest_Marks": subj_max,
        "Lowest_Marks": subj_min
    })
    return analysis_df

def compute_ai_readiness_score(df, subject_cols=SUBJECT_COLS):
    """
    Day 9 AI Concept: Feature Normalization + Artificial Neuron (Dot Product + Bias + ReLU).
    Normalizes subject marks to [0, 1], applies domain weights, adds bias, and applies ReLU.
    """
    normalized_marks = df[subject_cols].values / 100.0
    weights = np.array([0.35, 0.25, 0.10, 0.10, 0.20])  # Higher weight on Python, SQL, JS
    bias = -0.50  # Threshold shift: students need >50% weighted score for positive activation
    
    linear_output = np.dot(normalized_marks, weights) + bias
    relu_activation = np.maximum(0, linear_output)
    readiness_score = np.round(relu_activation * 200, 2)  # Scale back to 0-100 readiness index
    return readiness_score
