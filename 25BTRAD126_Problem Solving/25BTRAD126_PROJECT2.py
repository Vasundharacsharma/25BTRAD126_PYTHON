# Student Grading Program

print("STUDENT GRADE CALCULATOR")

register_no = input("Enter student's register number: ")
marks = int(input("Enter your marks (0-100): "))

print("\nRegister Number:", register_no)

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")