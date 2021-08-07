def converter2(number):
    a = ""
    number = bin(number)
    for num in list(number)[2:]:
        a += str(num)
    return a



