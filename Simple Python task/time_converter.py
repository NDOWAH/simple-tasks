def my_time():
    request = input("please type in your time in seconds: ")
    hours =request//3600
    minutes = (request % 60)// 60
    seconds = request % 60
    print("The time is %s:%s:%s"%(hours,minutes,seconds))


time = my_time()
print(time)