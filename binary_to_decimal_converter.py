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
            for i in enumerate(str(number)):
                index += str(i)
                print(digit)
                new_list = index[::-1]
                for i in new_list:
                    print(index)
                # decimal_number += int(digit)*2**int(i)
    return (f"The decimal equivalent of {number} is: {decimal_number}")

decimal_binary(100)