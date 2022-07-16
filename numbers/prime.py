no=int(input("enter number"))
div=2
while div<no:
    if no%div==0:
        print("not prime")
        break
    div+=1
else:
    print("prime")
