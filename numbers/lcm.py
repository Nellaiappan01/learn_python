no1,no2=3,30
big =no1 if no1>no2 else no2
if big%no1==0 and big%no2==0:
    print("lcm is",big)

no1,no2=3,34
big =no1 if no1>no2 else no2
while True:
    if big%no1==0 and big%no2==0:
        print("lcm is",big)
        break
    big+=1    