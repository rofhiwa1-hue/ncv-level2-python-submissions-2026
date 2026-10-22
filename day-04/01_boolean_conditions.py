
# Program to determine a learner's result

mark = float(input("Enter the learner's mark (0-100): "))

if mark < 0 or mark > 100:
    print("Invalid mark. Enter a mark between 0 and 100.")
elif mark >= 75:
    print("Result: Distinction")
elif mark >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
