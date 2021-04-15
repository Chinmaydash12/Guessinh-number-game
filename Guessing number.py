import random
choice='y'
while choice.lower()=='y':
    g=random.randint(1,20)
    i=0
    while i<6:
        n=int(input('Guess a number between 1-20'))
        if n<g and n>0:
            print('Gueaaing low')
            i=i+1
        elif n>g and n<=20:
            print('Guessing high')
            i=i+1
        elif g==n:
            print('BINGO')
            score=(6-i)*10
            print('Score is:',score)
            break
          
        else:
            print('Invalid')
    if i==6:
        print('You lost')
        print('Number was',g)
    choice=input('Press "y" to play again')
        
