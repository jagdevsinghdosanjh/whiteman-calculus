# Calculus Learning Portal (MIT + Whitman)

A modular, Streamlit-based LMS that delivers a 16‑week Calculus curriculum
based on MIT RES 18.001 and Whitman Calculus. Includes:

- Supabase authentication
- Joining-date based pacing (Mon–Sat only)
- Daily attendance tracking
- Daily progress logging
- Week overview pages (Week 01 → Week 16)
- Visualizers (Limits, Derivatives, Integrals, ODE, Multivariable)
- Student Dashboard (Plotly charts)
- Admin Analytics Dashboard
- Assignment + Quiz Engine (MCQ, Numeric, Symbolic)

---

## 📁 Project Structure

calculus_portal/
│
├── app.py
├── supabase_client.py
│
├── data/
│   ├── curriculum.json
│   └── attendance/
│       └── {student_id}.json
│
├── pages/
│   ├── Week_01.py → Week_16.py
│   ├── Student_Dashboard.py
│   ├── Admin_Dashboard.py
│   └── Assignments.py
│
├── modules/
│   ├── limits/
│   ├── derivatives/
│   ├── integrals/
│   ├── differential_equations/
│   ├── multivariable/
│   └── utils/
│
├── utils/
│   ├── date_utils.py
│   ├── attendance_utils.py
│   ├── pacing_utils.py
│   └── generate_week_pages.py
│
├── supabase/
│   ├── schema/
│   ├── policies/
│   └── migrations/
│
├── assets/
│   ├── styles.css
│   └── logo.png
│
├── .env
├── requirements.txt
└── README.md


---

## 🚀 Running the Project

### 1. Install dependencies


---

## 🚀 Running the Project

### 1. Install dependencies


### 2. Add your Supabase keys to `.env`

SUPABASE_URL=...
SUPABASE_KEY=...

### 3. Start Streamlit
streamlit run app.py

---

## 🧠 Core Features

### ✔ Daily Pacing  
Each student’s **Day 1 = joining date**.

### ✔ Attendance  
Automatically marked “Present” when the student opens the app.

### ✔ Progress Logging  
Week/day stored in Supabase daily.

### ✔ Dashboards  
- Student Dashboard → Plotly charts  
- Admin Dashboard → Heatmaps, analytics  

### ✔ Visualizers  
- Limits  
- Derivatives  
- Integrals  
- ODE  
- Multivariable  

### ✔ Assignment + Quiz Engine  
Supports MCQ, numeric, symbolic auto‑grading.

---

## 🔐 Supabase Tables

- `students`
- `attendance`
- `student_progress`
- `assignments`
- `questions`
- `submissions`
- `submission_items`

All with RLS enabled.

---

## 📦 Auto‑Generate Week Pages

python -m utils.generate_week_pages

Creates:

pages/Week_01.py → pages/Week_16.py

---

## 📞 Support

For issues, contact:

**Jagdev Singh Dosanjh**  
Owner/Admin — physicsbyjsd.org  
Amritsar, Punjab, India

---

This README is ready for GitHub and Streamlit Cloud.

---

If you want, I can now generate:

### **I)** Video lectures + PDF viewer  
### **J)** Student leaderboard  
### **K)** Teacher assignment creation UI  

Tell me which one you want next.