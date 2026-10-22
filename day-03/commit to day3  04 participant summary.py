full_name = input("Enter full name: ").strip()
staff_number = input("Enter staff number: ").strip()
level = input("Enter level: ").strip()

if full_name == "":
    print("Error: Full name cannot be empty.")
elif not staff_number.isdigit():
    print("Error: Staff number must contain numbers only.")
elif level == "":
    print("Error: Level cannot be empty.")
else:
    print("\n--- STAFF SUMMARY ---")
    print("Full Name:", full_name.title())
    print("Staff Number:", staff_number)
    print("Level:", level.upper())