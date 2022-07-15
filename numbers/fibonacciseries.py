#   first  second   third           A       B       A       B(water ltr understand 2 container)
#    -1      0       1              0       0       1       0
#     0      1       1              9       0       0       1
#     1      1       2              5       4       9       1
#     1      2       3              5       0       6       4
#     2      3       5              1       4        
#type-1
fi = -1
sec = 1
count = 1
#while coun<=10:
while True:
    thi=fi+sec
    print(thi)
    if thi==34:
        break
    fi = sec
    sec = thi
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

#type-3(water ltr understand 2 container)
f = -1
s = 1
count = 1
while count<=8:
    print(f+s)
    s = f+s   #0
    f = s-f   #1
    count+=1