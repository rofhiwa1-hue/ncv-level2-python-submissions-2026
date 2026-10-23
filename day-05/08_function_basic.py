def capture_marks():
    marks = []

    for i in range(5):
        mark = float(input("Enter mark (0-100): "))

        while mark < 0 or mark > 100:
            print("Invalid mark! Enter a mark between 0 and 100.")
            mark = float(input("Enter mark (0-100): "))

        marks.append(mark)

    return marks


def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def find_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


def main():
    marks = capture_marks()

    average = calculate_average(marks)
    highest = find_highest(marks)

    print("\n--- Results ---")
    print("Marks:", marks)
    print("Average mark:", round(average, 2))
    print("Highest mark:", highest)


main()