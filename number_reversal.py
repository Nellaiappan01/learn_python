#printing number reversal -int
#bread=1234
#print(bread%10)     #4
#bread =bread//10    #123
#print(bread%100) 
#bread=bread//100    #1
#print(bread%10)     #0
#bread=bread//10
#print(bread)
bread=int(input("Enter any number"))
while bread>0:
    print(bread%10,end="")
    bread=bread//10