import random

print('---------Choose One----------')
print('Rock = r, Paper = p, Scissor = s')
youstr = input('Enter your choice: ')
youdict = {'r': 2, 's': 1, 'p': 0}
redict = {2: 'Rock', 1: 'Scissor', 0: 'Paper'}
you = youdict[youstr]
computer = random.choice([0, 1, 2])

print(f'You choose', redict[you], '& Computer choose', redict[computer])

if computer != you:
    if computer == 2 and you == 1:
        print('You Lose')
    elif computer == 0 and you == 2:
        print('You Lose')
    elif computer == 1 and you == 0:
        print('You Lose')
    elif computer == 0 and you == 1:
        print('You Win')
    elif computer == 2 and you == 0:
        print('You Win')
    elif computer == 1 and you == 2:
        print('You Win')
elif computer == you:
    print("Draw")
else:
    print('Something went wrong!!!')
