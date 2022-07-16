no=int(input("enter number"))
for div in range(2,no):
    if no%div==0:
        print("not prime")
        break
else:
    print("prime")
