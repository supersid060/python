string = input("Please enter a word: ")
char=input("Please enter a letter to check for repetition: ")
count=0
i = 0
while i < len(string):
    if string[i] == char:
       count=count+1
    i=i+1
print("the letter", char , "appears", count, "times in",string)