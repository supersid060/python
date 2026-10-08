# Prompt the user for a decimal number
num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary representation: 0")
else:
    power = 0
    temp = num
    while temp > 1:
        power += 1
        temp //= 2

    
    binary_str = ""
    for i in range(power, -1, -1):
        if (num & (1 << i)):
            binary_str += "1"
        else:
            binary_str += "0"

    print(f"Decimal: {num}")
    print(f"Binary: {binary_str}")

