no =int(input("enter the value   "))
div=2
while div<no:
    if no%div==0:
        print('not prime')
        break
    div+=1
else:
    print("prime")
    print(div)
#if div==n0:
#   print("prime")