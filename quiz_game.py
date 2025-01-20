print('Welcome to my first quiz game!')

playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()

score = 0

answer = input('1. What is the capital of Ireland? ')
if answer.lower() == 'dublin':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('2. What is the capital of Canada? ')
if answer.lower() == 'ottawa':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('3. What is the capital of Ukraine? ')
if answer.lower() == 'kyiv':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('4. What is the capital of Slovakia? ')
if answer.lower() == 'bratislava':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('5. What is the capital of Italy? ')
if answer.lower() == 'rome':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('6. What is the capital of Russia? ')
if answer.lower() == 'moscow':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('7. What is the capital of Belarus? ')
if answer.lower() == 'minsk':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('8. What is the capital of Poland? ')
if answer.lower() == 'warsaw':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('9. What is the capital of France? ')
if answer.lower() == 'paris':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('10. What is the capital of Spain? ')
if answer.lower() == 'madrid':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

print('Game is over! Your score is',score, 'out of 10.')





