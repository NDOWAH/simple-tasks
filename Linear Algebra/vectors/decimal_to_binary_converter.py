def binary_converter(number):
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
    return a[::-1]

print(binary_converter(12))