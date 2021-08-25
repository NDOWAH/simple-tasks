def prime_checker(number):
    for num in range(1,10):
        if number % num ==0:
            pass
        else:
            print("{0} is a prime number.".format(number))
            break
#To be corrected
    

print(prime_checker(4))