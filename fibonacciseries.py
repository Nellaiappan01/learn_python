#   first  second   third
#     0      1       1
#     1      1       2
#     1      2       3
#     2      3       5

first = 0
second = 1
count = 1
#print(first)
#print(second)
while count<=2:
    third=first+second
    print(third)
    first=second
    second=third
    count+=1
else:
    print(third)