number=23
running=True
while running:
    guess=int(input('Enter an integer:'))
    if guess==number:
        print('Congratulations,you guessed it')
        running=False #this causes the while loop to stop
    elif guess<number:
        print('NO,it is a littl higher than that')
    else:
        print('NO,it is a littl lower than that')
else:
    print('The while loop is over.')
    #Do anythiing else you want to do here
print('Done')