bill=2.5
paid=4
total=(bill+bill*0.0825)
print("your total bill is:", total)
if paid - total > 0:
    print("cashier must pay you:", paid-total)
else:
    print("you must pay the cashier:", total-paid)
