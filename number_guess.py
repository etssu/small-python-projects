from random import randint

maximum = input('what is the maximum number?: ')
if maximum.isdigit():
    maximum = int(maximum)
    random_number = randint(0, maximum)
else:
    print('print a number next time.')
    quit()

attempt_max = input('enter the number of attempts: ')
if attempt_max.isdigit():
    attempt_max = int(attempt_max)
attempt = 0


while attempt <= attempt_max:
    attempt += 1
    player_guess = input('What is your guess? ')
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print('Print a number next time.')
        continue

    if player_guess == random_number:
        if attempt > 1:
            print("You got it in", attempt, "tries :) ")
        elif attempt == 1:
            print("You got it in", attempt, "try :) ")
        break
    elif player_guess > random_number:
        print('You are above.')
    else:
        print('You are below.')
else:
    print('Print a number next time.')
    quit()
    
