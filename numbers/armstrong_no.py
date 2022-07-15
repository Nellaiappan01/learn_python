#eg:378----->all single digits power cube addition =same number 378 its called armstrong no
bread=int(input("enter number"))
no =bread
total=0
while bread>0:
    dig=bread%10
    digpower=dig*dig*dig
    total=total+digpower
    bread=bread//10
else:
    if total==no:
        print("armstrong number")
    else:
        print("not armstrong number")

