def print_fizz_buzz(amount):
    for number in range(amount+1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_fizz_buzz(50)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
