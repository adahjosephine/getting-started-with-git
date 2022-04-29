# Guess My Number Game
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money.


name = input('What\'s your name my friend\n')
print('Welcome to the my \'Guess My Number\'!Game', name, '\a')
print('\nI\'m thinking of a number between 1 and 100.')
print('This game allows your guess a number.\n')

import random

# set the initial values
# sentry variables

my_number = random.randint(1, 100) # this allows the computer to choose a number
guess = int(input('Take a guess '))
tries = 1

# guessing loop

while guess != my_number:
    if guess > my_number:
        print('you guessed too high! Try again')
    else:
        print('you guessed too low! ouch! try again')
        
    guess = int(input('\nTake another guess:'))
    tries += 1
    if tries == 6:
        print('\nYou are a dummy, you have two chances left.')
        
    if tries == 8:
        print('\nYou\'ve ruled your chance of becoming a champion.')
        print('Oh Oh, too bad. Game Over!! Run the program again')
        break
       
if tries<=6:
    print('\nyaay! you\'re a genius!!! You guess it right.' \
          'You deserve a cup of icecream.')
    print('\nYou made it in', tries, 'tries')
else:
    print('\nThe number was ', my_number)
    print('\nYou made it in', tries, 'tries. Don\'t be a dummy next time')

input('\n\nPress the enter key to escape')

