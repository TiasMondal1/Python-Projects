# Guess the number that is randomly generated using random function
import random

while True:
    number = random.randint(1,100)
    no_of_guesses = 0

    while True:
        guess = input('Im thinking of a number! Try to guess the number: ')
        no_of_guesses += 1
        
        if guess == number:
            print('You guessed the number {0} correctly in {1} times'.format(number, no_of_guesses))
            play_again = input('Thats the number! Would you like to play again? (Yes/No): ').lower()
            if play_again != 'yes':
                print('Thanks for playing!')
                exit()
            break
        elif guess < number:
            print('Too low! Guess again.')
        else:
            print("Too high! Guess again.")