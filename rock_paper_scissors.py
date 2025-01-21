import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to exit: ').lower()
    if user_input == 'q':
        print('User wins:', user_wins)
        print('Computer wins:', computer_wins)
        break
    if user_input not in options:
        print('choose the correct option next time.')
        continue
    random_number = random.randint(0,2)
    #0 - rock    1 - paper    2 - scissors
    computer_pick = options[random_number]
    print('Computer picked', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print('You win!')
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print('You win!')
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_wins += 1
        print('You win!')
    else:
        computer_wins += 1
        print('You lost!')

print('Goodbye! Thanks for playing.')