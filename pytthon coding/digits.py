num = int(input("Please enter any positive integer: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print(f"The number of digits in {num} is {count}")