a = ""
count = 0
number = int(input("type any number: "))
while True:
    remainder = number % 2
    a += str(remainder)
    number = number // 2
    if number < 2:
        a += str(number)
        break
    else:
        count += 1
reverse_a = a[::-1]
print(reverse_a)





