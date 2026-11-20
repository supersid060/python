start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
odd_squares = []
even_squares = []
for num in range(start, end + 1):
    square = num * num
    if num % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

# Display results
print("Odd squares:", odd_squares)
print("Even squares:", even_squares)