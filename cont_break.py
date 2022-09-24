count=0
total=0
while True:
    num = input("enter a number")
    if num == 'done':
        break
    elif not num.isnumeric():
        print("invalid number")
        continue
    else:
        in_num=int(num)
        count=count+1
        total+=in_num
        avg = total/count
print(count, total, avg)
