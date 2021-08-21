def root_n(number,root):
    count = 0
    num = 1
    while count < number:
        num = ((num + root/number))/2
        count += 1
    return num

print(root_n(5,2))

