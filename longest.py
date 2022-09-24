name=input("enter word: ")
def sub(word):
    long = word[0]
    order = word[0]
    for i in word [1:]:
        if i >= order[-1]:
            order += i
            if len(order) > len(long):
                long = order
            else:
                order = i
    print(long)

sub(name)
