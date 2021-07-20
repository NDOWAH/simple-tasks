def my_time(seconds):
    request = input("please type in your time in seconds: ")
    hours = seconds//3600
    minutes = (seconds % 60)// 60
    seconds = seconds % 60
    print("The time is %s:%s:%s"%(hours,minutes,seconds))