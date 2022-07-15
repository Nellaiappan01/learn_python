#   first  second   third
#    -1      0       1
#     0      1       1
#     1      1       2
#     1      2       3
#     2      3       5

#type-1
first = -1
second = 1
count = 1
#while count<=10:
while True:
    third=first+second
    print(third)
    if third==34:
        break
    first = second
    second = third
    count+= 1
#type-2
first = -1
second = 1
count = 1

while count<=10:
    third=first+second
    print(third)
    first = second
    second = third
    count+= 1
    
#type-3
