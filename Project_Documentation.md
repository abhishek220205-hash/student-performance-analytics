# Student Performance Analytics System

## 1. Project Title
* **Project Name:** Student Performance Analytics System
* **Student Name:** Abhishek Kumar
* **College:** Guru Gobind Singh Indraprastha University (GGSIPU)
* **Internship Domain:** Python with AI (EWB EduTech)
* **Trainer:** Chandini

---

## 2. Objective
The objective of the **Student Performance Analytics System** is to automate the evaluation, statistical processing, and performance analysis of student academic records using **Python**, **NumPy**, and **Pandas**. Instead of manually calculating marks, averages, grades, and pass/fail statuses across spreadsheets, this system ingests a structured CSV dataset, performs vectorized numerical computations, applies rule-based grading and attendance thresholds, and generates a comprehensive analytical report—including an AI-inspired Placement Readiness Score using feature normalization, weighted dot products, and ReLU activation.

---

## 3. Technologies Used
* **Programming Language:** Python 3
* **Numerical Computing:** NumPy (`np.array`, `np.sum`, `np.mean`, `np.max`, `np.min`, `np.dot`, `np.maximum`, `np.round`)
* **Data Manipulation & Analysis:** Pandas (`pd.read_csv`, `DataFrame`, `.iloc`, boolean filtering, `.sort_values`, `.head`)
* **Visualization (Optional Enhancement):** Matplotlib (`performance_chart.png`)
* **Version Control:** Git & GitHub

---

## 4. Dataset Description
The dataset (`students.csv`) contains **20 realistic student records** across 9 structured columns:
* `Student_ID`: Unique identifier for each student (`STU101` to `STU120`)
* `Name`: Full name of the student
* `Department`: Academic branch (`CSE`, `AI & ML`, `IT`, `Data Science`, `ECE`)
* `Python`, `SQL`, `HTML`, `CSS`, `JavaScript`: Subject-wise marks scored out of 100 (`int64`)
* `Attendance`: Overall semester attendance percentage (`float64`)

---

## 5. Implementation
The project is modularized into three main files (`students.csv`, `functions.py`, and `main.py`):
1. **Data Preparation & Loading (`Step 1 & Step 2`):** `main.py` loads `students.csv` into a Pandas DataFrame using `pd.read_csv("students.csv")`.
2. **Numerical Processing with NumPy (`Step 3`):** `calculate_totals_and_averages()` extracts the 5 subject columns as a 2D NumPy matrix and calculates row-wise totals (`np.sum(..., axis=1)`) and averages (`np.mean(..., axis=1)`).
3. **Rule-Based Evaluation with Functions & Loops (`Step 3`):** `evaluate_students()` iterates over all records using a `for` loop and `df.iloc[i]`, calling `assign_grade()` (`if-elif-else` ladder: `A+`, `A`, `B`, `C`, `D`, `F`) and `check_pass_fail()` (requiring `Average >= 50` AND `Attendance >= 75%`).
4. **AI Readiness Neuron (Day 9 Concept):** `compute_ai_readiness_score()` normalizes marks (`marks / 100.0`), computes the weighted dot product (`np.dot(normalized_marks, weights) + bias`), and applies the **ReLU activation function** (`np.maximum(0, x)`).
5. **Statistical & Subject-Wise Analysis (`Step 4 & Step 5`):** `StudentAnalyticsSystem` (OOP class) computes class average, highest/lowest scorers, pass/fail counts, subject-wise averages (`axis=0`), and ranks the top 5 performers.

---

## 6. Key Features
* Automated CSV ingestion and structured Pandas DataFrame organization.
* High-speed row-wise and column-wise numerical aggregations via NumPy.
* Reusable modular functions (`functions.py`) and clean Object-Oriented design (`main.py`).
* Multi-condition Pass/Fail verification combining academic marks (`>= 50%`) and attendance (`>= 75%`).
* Subject-wise performance comparison identifying the highest-scoring subject.
* AI/Neural-Network-inspired readiness metric using feature normalization, dot product weights, and ReLU activation.

---

## 7. Sample Output
```text
================================================================================
           STUDENT PERFORMANCE ANALYTICS SYSTEM - FINAL REPORT
================================================================================

3. OVERALL CLASS PERFORMANCE STATISTICS:
   - Total Students Analyzed : 20
   - Overall Class Average   : 77.33%
   - Highest Average Score   : 94.8% (Sneha Iyer - STU104)
   - Lowest Average Score    : 41.0% (Manish Tiwari - STU115)
   - Total Students Passed   : 17
   - Total Students Failed   : 3

4. SUBJECT-WISE PERFORMANCE ANALYSIS:
   Subject  Average_Marks  Highest_Marks  Lowest_Marks
    Python          77.90             96            42
       SQL          76.30             94            39
      HTML          80.75             97            46
       CSS          76.90             94            40
JavaScript          74.80             96            38
   -> Best Performing Subject: HTML (Average: 80.75%)

5. TOP 5 PERFORMING STUDENTS:
Student_ID          Name Department  Total  Average Grade  AI_Readiness
    STU104    Sneha Iyer        CSE    474     94.8    A+          89.7
    STU112   Divya Menon    AI & ML    470     94.0    A+          88.2
    STU118 Nisha Agarwal    AI & ML    460     92.0    A+          83.9
    STU101  Aarav Sharma        CSE    450     90.0    A+          79.6
    STU108    Neha Gupta        CSE    445     89.0     A          78.8
================================================================================
```

---

## 8. Final Outcome
The system processes all 20 student records with zero errors. It accurately identifies an overall class average of **77.33%**, highlights **Sneha Iyer (`STU104`, 94.8%)** as the top performer, flags **3 failing students** (including **Rahul Nair (`STU111`)** due to attendance below 75% despite a 55.4% mark average), and determines **HTML (80.75%)** as the highest-performing subject.

---

## 9. Challenges & Learning
* **Challenge 1 (Row vs. Column Aggregations):** Distinguishing between student-level totals and subject-level averages in a 2D array. **Solution:** Applied `axis=1` for horizontal student calculations and `axis=0` for vertical subject aggregations in NumPy.
* **Challenge 2 (Multi-Criteria Pass/Fail Logic):** Ensuring students with passing marks but low attendance were properly flagged. **Solution:** Implemented a logical `and` condition inside `check_pass_fail(avg_marks, attendance)`.
* **Key Learning:** Gained hands-on proficiency in combining core Python fundamentals (`functions`, `loops`, `conditionals`, `OOP`) with data science libraries (`NumPy` and `Pandas`) to build a modular analytics pipeline.

---

## 10. How to Run the Project
```bash
pip install numpy pandas matplotlib
python main.py
```
