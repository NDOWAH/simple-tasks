def decimal_binary(number):
    decimal_number = 0
    number = str(number)
    for digit in number:
        if int(digit) > 1:
           print("The number inputed is not a binary number, binary numbers contain only ones and zeros.")
        else:
            index = ""
            for i,  digit in enumerate(str(number)):
               index += str(i)
               break
            new_list = index[::-1]
            print(new_list)
            for i in new_list:
                   decimal_number += int(digit)*2**int(i)
    return f"The decimal equivalent of {number} is: {decimal_number}"



