def counter(object):
    count = 0
    for i in object:
        count +=1
    return (f"The number of items are: {count}")


print(counter("they are two of them in the class"))