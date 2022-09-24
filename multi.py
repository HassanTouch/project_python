
table = int(input("enter ur table or number\n"))
lst = []
i = 1
while i <= table:
    multipl = [i*j for j in range(1,i+1)]
    lst.append(multipl)
    i+=1
print(lst)
