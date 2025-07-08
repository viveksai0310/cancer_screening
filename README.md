# 🧠 Cancer Screening Reminder and Risk Stratification System

## 🔍 Problem Statement

Build a system that tracks screening schedules and identifies patients who need priority screening based on risk factors.

---

## 🎯 Project Summary

This is a Python-based system that:

- Calculates a patient's cancer risk (Low/Medium/High)
- Sets appropriate screening schedules (1, 2, or 3 years)
- Adjusts screening types based on gender
- Outputs a personalized reminder summary

---

## ⚙️ How It Works

### 📥 Inputs:
- Name
- Gender (male/female)
- Age
- Family history of cancer (yes/no)
- Smoker (yes/no)
- Alcohol use (yes/no)

### 🧠 AI Logic:
Uses a **rule-based model** (simulated AI) to calculate risk scores:
- Age ≥ 50 → +2
- Age ≥ 40 → +1
- Family history → +2
- Smoker → +1
- Alcohol use → +1

### 📊 Risk Level:
- **High**: score ≥ 4 → screen every 1 year
- **Medium**: score 2-3 → every 2 years
- **Low**: score < 2 → every 3 years

### 📅 Screening Schedules:
- **Breast Cancer**: all genders (can be adjusted)
- **Cervical Cancer**: only for females
- **Colorectal Cancer**: all patients

---

## 🖥 How to Run

1. Download or clone this repo.
2. Make sure you have Python 3 installed.
3. Open terminal or command prompt.
4. Run:

```bash
python cancer_screening.py
