#printing number reversal -int
#bread=1234
#print(bread%10)     #4
#bread =bread//10    #123
#print(bread%100) 
#bread=bread//100    #1
#print(bread%10)     #0
#bread=bread//10
#print(bread)
bread=int(input("Enter any number "))
count=0
while bread>0:
    print(bread%10,end="")
    count+=1
    bread=bread//10
else:
    print("      count of digits is",count)

#addition of digits

bread=int(input("Enter any number "))
count=0
total=0
while bread>0:
    total=total+bread%10
    print(bread%10,end="")
    count+=1
    bread=bread//10
else:
    print("      count of digits is",count)
    print("      addition of digits is",total)

#4*10+3=43 (concept understand_forward adding number)----->reversed value

bread=int(input("Enter any number "))
count=0
total=0
while bread>0:
    total=(total*10)+bread%10       #total=
    print(bread%10,end="")
    count+=1
    bread=bread//10
else:
    print("      count of digits is",count)
    print("      addition of digits is",total)
    print("      reversed value is",total)
