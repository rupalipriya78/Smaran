# SMARAN – Assignment, Exam & To-Do Tracker

##  Project Overview
**Smaran** (Remembrance) is a simple and aesthetic productivity tool designed specifically for students. It acts as a centralized academic planner to manage assignment deadlines, exam schedules, and daily to-do tasks. 

By distinguishing between urgent academic deadlines and regular tasks, Smaran helps students stay organized, reduce anxiety, and ensure no deadline is ever missed.

---

##  Problem Statement
Students frequently struggle with managing multiple deadlines across different subjects. Without a unified tracking system, tasks get lost in WhatsApp groups or mental notes, leading to:
* Missed assignment submissions.
* Lack of preparation time for exams.
* Decreased overall productivity.

**Smaran solves this** by providing a unified, color-coded platform to add, view, manage, and complete all academic tasks in a structured way.

---

## Features

### 1. Smart Categorization
*  **Exams:** Highlighted for high priority.
*  **Assignments:** Distinct color for submission tracking.
*  **To-Dos:** For daily non-academic tasks.

### 2. Task Management
* **Add Items:** Input title, category, date, and time.
* **Deadline Tracking:** Automatically calculates time remaining.
* **Visual Status:** Mark items as **Completed** (strike-through) or **Delete** unwanted entries.

### 3. Aesthetic UI
* Clean, minimalist interface designed for focus.
* Responsive design using Bootstrap 5.

---

##  Tech Stack
* **Backend:** Python (Flask)
* **Database:** SQLite (SQLAlchemy) - *Ensures data is saved permanently.*
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Templating:** Jinja2

---

##  Steps to Install & Run

1.  **Clone the repository** (or download files):
    ```bash
    git clone [https://github.com/yourusername/smaran.git](https://github.com/yourusername/smaran.git)
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    python run.py
    ```
4.  **Open in Browser**:
    Go to `http://127.0.0.1:5001`

---

##  Instructions for Testing

1.  **Register/Login:** Create a new account to access your private planner.
2.  **Add an Exam:** * Click "Add New Item".
    * Select Category: "Exam".
    * Set a date in the future.
    * *Check:* Verify it appears with a Red indicator.
3.  **Test Overdue Logic:**
    * Add a task with a date in the *past*.
    * *Check:* Verify it highlights as **OVERDUE**.
4.  **Complete a Task:**
    * Click the "Done" checkmark.
    * *Check:* Verify it moves to the "Recently Completed" history list.

---

## System Architecture

`User` → `HTML Dashboard` → `Flask Controller (Python)` → `SQLite Database` → `Updated View`

---
