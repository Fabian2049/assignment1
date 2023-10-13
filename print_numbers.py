for number in range(100):
    if number % 5 == 0 and number % 3 == 0:
     print("fizzbizz", number)
    elif number % 3 == 0:
        print("fizz", number)
    elif number % 5 == 0:
        print("bizz", number)
    elif number % 5 != 0 and number % 3 != 0:
        print ("nothing", number)









