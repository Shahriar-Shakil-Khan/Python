#Aiub Grading System

marks=float(input("Enter your Exam number : = "))
if marks<=100 and marks>=90:
    print("A+")
elif marks<90 and marks>=85:
    print("A")
elif marks < 85 and marks >=80:
    print("B+")
elif marks < 80 and marks >=75:
    print("B")
elif marks < 75 and marks >=70:
    print("C+")
elif marks < 70 and marks >=65:
    print("C")
elif marks < 65 and marks >=60:
    print("D+")
elif marks < 60 and marks >=50:
    print("D")
else:
    print("F")