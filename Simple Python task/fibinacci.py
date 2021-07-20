def fibinacci(n):
    if not isinstance(n, int):
        print("we can only find the fibinacci of integers")
    if n == 0:
        return 1
    else:
        return n * fibinacci(n-1)

print(fibinacci(5))