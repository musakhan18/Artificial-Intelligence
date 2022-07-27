lis1 = []  
n = int(input("Enter number of elements: ")) 

for i in range(0, n):
    str = (input())
    lis1.append(str) 
print('List before removing duplicates')
print('--------------------------------')
print(lis1)
lis2=[]
flag=0
for i in range(0, n):
    str1=lis1[i]
    for j in range(i+1,n):
        if str1==lis1[j]:
            flag=1
            break
        else:
            flag=0
    if flag  ==0:
        lis2.append(str1)
print("List after removing duplicates")
print('-------------------------------')
print(lis2)
lis2.sort()
print("List after sorting")
print('-------------------')
print(lis2)