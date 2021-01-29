str1=input()
y=str1
str2=input()
x=str1
for i in str2:
    if i not in x:
        str1+=i
print("Union is",end=" ")
print(str1)
z=y
res=""
for i in y:
    if i in str2 and not i in res:
        res+=i
print("Intersection is ",end=" ")
print(res)


