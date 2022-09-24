
pyrmds = input("enter number to build a pyrm\n")
number = int(pyrmds)
for i in range(number):
    for j in range(i+1):
        print("* ", end="")
    print("\n")