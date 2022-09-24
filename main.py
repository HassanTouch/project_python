
name = input("what is ur name: ")
vowels = ['a', 'e', 'i', 'o', 'u']
sum = 0
for i in name:
    if i in vowels:
        sum = sum+1
print(sum)
