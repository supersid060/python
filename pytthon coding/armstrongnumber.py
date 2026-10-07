num=int(input("enter number you are trying to check:"))
sum=0
temp=num
pwr=int(input("enter number of digits:"))
while temp>0 :
    digit=temp % 10
    sum=sum+(digit**pwr)
    temp//=10
if num==sum :
    print(num ,"is an armstrong number")
else :
    print(num ,"is not an armstrong number")