count = 0
total = 0

mark = int(input("Enter a mark (0-100), or -1 to stop: "))

while mark != -1:
    if mark >= 0 and mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print("Invalid mark. Enter 0 to 100.")

    mark = int(input("Enter a mark (0-100), or -1 to stop: "))

if count > 0:
    average = total / count
    print("Number of valid marks:", count)
    print("Total of valid marks:", total)
    print(f"Average: {average:.2f}")
else:
    print("No valid marks were entered.")
