try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
