def bill_split(bill):
    print("Welcome to the tip calculator.")
    num_of_people = int(input("How many people should the bill be distributed to? "))
    percentage_split = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
    bill = round((bill * (1 - percentage_split / 100)) / num_of_people, 3)
    print(f"Each person will pay: ${bill}".format(bill))

