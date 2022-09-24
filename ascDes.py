lst = []
print("enter ur element")
i = 0
while i < 5:
    obje = int(input())
    lst.append(obje)
    i+=1

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)