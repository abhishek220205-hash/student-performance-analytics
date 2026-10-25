import pandas as pd
import numpy as np
from functions import (
    SUBJECT_COLS,
    calculate_totals_and_averages,
    evaluate_students,
    get_subject_wise_analysis,
    compute_ai_readiness_score
)

class StudentAnalyticsSystem:
    """OOP wrapper for the Student Performance Analytics System."""
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        return self.df

    def process_data(self):
        totals, averages = calculate_totals_and_averages(self.df, SUBJECT_COLS)
        self.df["Total"] = totals
        self.df["Average"] = averages
        
        grades, results = evaluate_students(self.df)
        self.df["Grade"] = grades
        self.df["Result"] = results
        self.df["AI_Readiness"] = compute_ai_readiness_score(self.df, SUBJECT_COLS)

    def display_report(self):
        print("=" * 80)
        print("           STUDENT PERFORMANCE ANALYTICS SYSTEM - FINAL REPORT")
        print("=" * 80)

        print("\n1. STUDENT DATASET (RAW RECORDS):")
        raw_cols = ["Student_ID", "Name", "Department"] + SUBJECT_COLS + ["Attendance"]
        print(self.df[raw_cols].to_string(index=True))

        print("\n2. PROCESSED STUDENT PERFORMANCE SUMMARY:")
        perf_cols = ["Student_ID", "Name", "Total", "Average", "Attendance", "Grade", "Result", "AI_Readiness"]
        print(self.df[perf_cols].to_string(index=True))

        # Class-level metrics using NumPy
        avg_array = self.df["Average"].values
        class_avg = np.round(np.mean(avg_array), 2)
        highest_avg = np.max(avg_array)
        lowest_avg = np.min(avg_array)

        top_student = self.df[self.df["Average"] == highest_avg].iloc[0]
        low_student = self.df[self.df["Average"] == lowest_avg].iloc[0]

        passed_count = len(self.df[self.df["Result"] == "Pass"])
        failed_count = len(self.df[self.df["Result"] == "Fail"])

        print("\n3. OVERALL CLASS PERFORMANCE STATISTICS:")
        print(f"   - Total Students Analyzed : {len(self.df)}")
        print(f"   - Overall Class Average   : {class_avg}%")
        print(f"   - Highest Average Score   : {highest_avg}% ({top_student['Name']} - {top_student['Student_ID']})")
        print(f"   - Lowest Average Score    : {lowest_avg}% ({low_student['Name']} - {low_student['Student_ID']})")
        print(f"   - Total Students Passed   : {passed_count}")
        print(f"   - Total Students Failed   : {failed_count}")

        print("\n4. SUBJECT-WISE PERFORMANCE ANALYSIS:")
        subj_df = get_subject_wise_analysis(self.df, SUBJECT_COLS)
        best_subj_row = subj_df.loc[subj_df["Average_Marks"].idxmax()]
        print(subj_df.to_string(index=False))
        print(f"   -> Best Performing Subject: {best_subj_row['Subject']} (Average: {best_subj_row['Average_Marks']}%)")

        print("\n5. TOP 5 PERFORMING STUDENTS:")
        top_5 = self.df.sort_values(by="Average", ascending=False).head(5)
        print(top_5[["Student_ID", "Name", "Department", "Total", "Average", "Grade", "AI_Readiness"]].to_string(index=False))
        print("=" * 80)

if __name__ == "__main__":
    system = StudentAnalyticsSystem("students.csv")
    system.load_data()
    system.process_data()
    system.display_report()
