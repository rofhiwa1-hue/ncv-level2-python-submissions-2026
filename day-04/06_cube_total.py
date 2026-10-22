
n = int(input("Enter a positive whole number: "))

if n < 1:
    print("Invalid input. Enter a number greater than or equal to 1.")
else:
    total = 0

    for number in range(1, n + 1):
        cube = number ** 3
        print("Cube of", number, "=", cube)
        total = total + cube

    print("Total of cubes:", total)

