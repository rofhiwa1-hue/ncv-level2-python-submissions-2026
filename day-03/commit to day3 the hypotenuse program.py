
import math

# INPUT
side_a = float(input("Enter the first shorter side in metres: "))
side_b = float(input("Enter the second shorter side in metres: "))

# PROCESS AND OUTPUT
if side_a <= 0 or side_b <= 0:
    print("Error: Both sides must be greater than zero.")
else:
    hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
    print(f"Hypotenuse: {hypotenuse:.2f} m")
