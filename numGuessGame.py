import random

num = random.randint(1,9)
chances = 0
while chances>5:
    guess = int(input('enter guess\n'))
    if guess>9 or guess<1:
        print('guess outside limit')
    else:
        chances+=1
        if guess == num:
            print('CONGRATS!!! You won')
            break
        elif guess > num:
            print('Guess too high')
        elif guess < num:
            print('Guess too low')
        if chances==5:
            print('Too many chances, the number was ' + str(num))
    
