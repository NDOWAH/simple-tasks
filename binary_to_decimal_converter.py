def decimal_binary(number):
    decimal_number = 0
    number = str(number)
    for digit in number:
        break

    if int(digit) > 1:
        print("The number inputed is not a binary number, binary numbers contain only ones and zeros.")

    else:
        for i, digit in enumerate(str(number)):
            decimal_number += int(digit)*2**int(i)
    return f"The decimal equivalent of {number} is: {decimal_number}"


print(decimal_binary(11111111111000001))