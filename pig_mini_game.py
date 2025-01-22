import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input('enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('There must be 2-4 players.')
    else:
        print('Print the valid number next time.')


max_score = 50  #change in to input later
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        print('\nPlayer', player_index + 1, 'turn just started!\n')
        current_score = 0

        while True:
            should_roll = input('would you like to roll (y)? ')
            if should_roll.lower() != 'y':
                break

            value = roll_dice()
            if value == 1:
                current_score = 1
                print('You rolled a 1. Turn done!')
                break

            else: 
                current_score += value
                print('You rolled a:', value)

            print('Your score is:', current_score)

        player_scores[player_index] += current_score
        print('Your total score is:', player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print('Player', player_index + 1, 'is the winner with the score of:', max_score)