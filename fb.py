def fizzBuzz():

    for num in range(1, 100):
        if num % 3 == 0 & num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print("Invalid")

print(fizzBuzz())