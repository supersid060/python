try:
num1,num2=eval(input("please enter two numbers:"))
    answer=num1/num2
    print("answer is:", answer)
except ZeroDivisionError:
    print("There is Division by Zero")
except SyntaxError:
    print("Comma is missing.Enter numbers seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("This Will Execute No Matter What")