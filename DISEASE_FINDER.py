# PROGRAM TO FIND MEDICINES OF SOME DISEASE

Disease=["flu","strep throat","covid","fungal","hypertension","asthama"]
problem=input("Enter your Disease:")
if problem in Disease:
    if problem in "flu":
        print("Take Paracetamol")
    elif problem in "strep throat":
        print("Take Penicillin or Amoxicillin")
    elif problem in "covid":
        print("Take Paxlovid")
    elif problem in "fungal":
        print("Take Clotrimazole")
    elif problem in "hypertension":
        print("Take Hydrichlorothiazide")
    elif problem in "asthama":
        print("Take Inhaler")
else:
    print("Unkown Disease")