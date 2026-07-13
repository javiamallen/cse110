# ---------------------------------------------------------------------------
# Developer: Javiera Allende (Javiam Allen)
# GitHub: https://github.com/javiamallen
# LinkedIn: https://www.linkedin.com/in/javierallend1/
# Project: W03 Code-along Activity - Grade Calculator Program
# Course: CSE 110 - Introduction to Programming (BYU)
# 
# Enhancement: Added sign logic (+/-) using core modulo math while filtering 
# invalid designations for A+ and F level grades.
# ---------------------------------------------------------------------------

# --- 1. GET USER INPUT ---
grade = int(input("What is your grade percent? "))

# --- 2. DETERMINE BASE LETTER GRADE ---
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# --- 3. CALCULATE THE SIGN (+ or -) ---
sign = ""
last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Handle specific grading edge cases (No A+, No F+/F-)
if grade >= 93:
    sign = ""
if letter == "F":
    sign = ""

# --- 4. DISPLAY RESULTS ---
print(f"Your letter grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")