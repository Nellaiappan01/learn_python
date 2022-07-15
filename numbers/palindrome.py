#-------->reversed number
bread=int(input("enter number"))
no =bread
rev=0
while bread>0:
    rev=(rev*10)+bread%10
    bread=bread//10
else:
    print("reversed value is",rev)
    if rev==no:
        print("palindrome")
    else:
        print("not palindrome")
