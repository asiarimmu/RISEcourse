#guess the number game :)
#run module

import random
num_guesses = 0
name = input('Hi, what is your name? ')
number = random.randint(1, 20)
print('Welcome, {}! I am thinking of a number between 1 and 20'.format(name))
while num_guesses < 6:
    guess = int(input('Take a guess'))
    num_guesses += 1
    if guess < number:
        print('too low')
    if guess > number:
        print('too high')
    if guess == number:
        break
if guess == number:
    print('congratulations {}! you guessed the correct number it took you {} attempts'.format(name, num_guesses))
else:
    print('sorry {} you lose! the number was {}'.format(number))
    
                
