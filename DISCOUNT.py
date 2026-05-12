#Take shopping amount input:
# Above 5000 → 20% discount
# Above 2000 → 10% discount
# Otherwise no discount

AMOUNT=int(input("how much amount:"))
if AMOUNT >= 2000 and AMOUNT<5000:
    print("With discount your amount will be:",AMOUNT-(0.1*AMOUNT))
elif AMOUNT >= 5000:
    print("With discount your amount will be:",AMOUNT-(0.2*AMOUNT))
else:
    print("NO DISCOUNT")