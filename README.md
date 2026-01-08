AI Study Planner:

An AI-based personalized study planner that helps students allocate daily study time intelligently based on subject difficulty and exam deadlines.

Problem Statement:
Students often struggle to divide their study time efficiently across multiple subjects before exams. This project solves that problem by generating a data-driven daily study plan.

Solution:
The system calculates urgency using:
- Subject difficulty
- Remaining days until the exam

It then distributes available daily study hours proportionally.

Tech Stack:
- Python
- Pandas
- Streamlit

Project Structure
ai-study-planner/
│
├── data/
│ └── subjects.csv
├── app.py
├── planner.py
├── requirements.txt
└── README.md


How to Run ?
cmd prompt
pip install -r requirements.txt
python -m streamlit run app.py

Sample I/P:
subject,difficulty,exam_date
Maths,4,2026-02-15
AI,5,2026-02-18
OS,3,2026-02-20

Sample O/P:
A personalized daily study schedule showing:
 1. Subject name.
 2. Daily hours allocated.
 3. Days left until exam.

