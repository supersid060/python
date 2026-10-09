count = int(input("what number do you want to square? "))
bread= int(input("what power do you want to raise the number to? "))
 for i in range(1, count + 1):
     num = int(input(f"Enter number {i}: "))
     square = num ** bread 
     print(f"the square of {num} is {square}
