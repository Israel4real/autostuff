def new_collatz(number):
    if number == 1:
        print(1)
        return 1
    elif number % 2 == 0:
        print(number // 2)
        return new_collatz(number // 2)
    else:
        print(3 * number + 1)
        return new_collatz(3 * number + 1)

print('Enter a number: ')
num = int(input())


new_collatz(num)
