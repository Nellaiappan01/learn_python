from math import factorial


for no in range(5):
    print(no,end=' ')
print()
for no in range(1,5):
    print(no,end=' ')
print()
for no in range(1,5,2):
    print(no,end=' ')
print()
for no in range(10,1,-2):
    print(no,end=' ')
print()
#reversed alpha type-1
word='nellai'
for i in range(len(word)-1,-1,-1):
    print(word[i],end=" ")
print()
#reversed alpha type-2 palindrome
word='nellai'
word2=word[ : : -1]
print(word2,end= "       ")