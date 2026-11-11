while True:
    age_input = input("Enter your age: ").strip()
    try:
        age = int(age_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue  
    if age % 2 == 0:
        print(f"Your age {age} is even.")
    else:
        print(f"Your age {age} is odd.")
    break