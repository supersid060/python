print("Please select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

while True:
    choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip()
    if choice == 'q':
        print("Exiting calculator.")
        break
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid numbers. Please enter numeric values.")
        continue

    if choice == '1':
        result = add(n1, n2)
    elif choice == '2':
        result = subtract(n1, n2)
    elif choice == '3':
        result = multiply(n1, n2)
    elif choice == '4':
        result = divide(n1, n2)

    print(f"{n1} {choice} {n2} = {result}")
How it works
Separate functions (add, subt