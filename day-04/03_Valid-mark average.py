
count = 0
total = 0

mark = int(input("Enter mark (0-100) or -1 to stop: "))

while mark != -1:

    if 0 <= mark <= 100:
        count = count + 1
        total = total + mark
    else:
        print("Invalid mark. Enter a mark from 0 to 100.")

    mark = int(input("Enter mark (0-100) or -1 to stop: "))

if count > 0:
    average = total / count
    print("Number of valid marks:", count)
    print("Total of valid marks:", total)
    print(f"Average mark: {average:.2f}")
else:
    print("No valid marks were entered.")
