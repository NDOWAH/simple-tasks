def prime_checker(number):
              test_val = " "
              for num in range(1,9):
                     test_val += str(num)
                     for val in test_val:
                        if number % int(val) != 0:
                           print("{0} is a prime number".format(number))
                        else:
                          print("{0} is not a prime number.".format(number))
                        break
                           
#To be corrected
    

print(prime_checker(7))