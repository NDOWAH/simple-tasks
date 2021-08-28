def prime_checker(number):
           try:
              for num in range(9):
    
               while number % num != 0:
                  print("{0} is a prime number".format(number))
               else:
                  print("{0} is not a prime number.".format(number))
           except ZeroDivisionError:
                 print("division by zero is not allowed")
                 
            
#To be corrected
    

print(prime_checker(5))