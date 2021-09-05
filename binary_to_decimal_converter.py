def decimal_binary(number):
    decimal_number = 0
    number = str(number)
    for digit in number:
        try:
            if int(digit) > 1:
                raise ValueError
        except ValueError:
            print("The number you inputed is not in base 2, numbers in base 2 are in zeros and ones only")
            break
        index = ""
        _list = (list(number))
        print(_list)
        break
    for j in range(0,len(_list),-1):
        for i in _list:
            decimal = int(i)*2**j




decimal_binary(100)