from random import randint

number = randint(1, 100)
print('Guess the number from 1 to 100: ')

while True:
    guess = int(input('Entre your number: '))

    if guess < number:
        print('Your number is less than guessed')
    if guess > number:
        print('Your number is greater than guessed')
    if guess == number:
        break

print('You\'ve got a great intuition, you\'ve guessed the number')

