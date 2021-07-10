a = ""
number = int(input("type in any number: "))
number = bin(number)
for num in list(number)[2:]:
    a += str(num)
print(a)

