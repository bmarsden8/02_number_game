import random

print('-------------------------------------')
print('         GUESS THAT NUMBER GAME      ')
print('-------------------------------------')

##the_number = random.randint(0,100)

the_number = random.randint(0,100)

name = input('What is your name?')

guess_text = 0

while guess_text != the_number:
    guess_text = input('Guess a number between 1 and 100:   ')
    if int(guess_text) == the_number:
        print('Yes, that is correct!')
        break
    if int(guess_text) < the_number:
        print('Sorry {0}, your guess of {1} was too low. Guess higher!'.format(name, guess_text))
    if int(guess_text) > the_number:
        print('Sorry {0}, your guess of {1} was too high. Guess lower!'.format(name, guess_text))


