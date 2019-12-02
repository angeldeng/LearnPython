number=23
guess=int(input('Enter an integer:'))
if guess==number:
    print('Congratulations,you guessed it') #新块开始地方
    print('but you do not win any prices') #新块结束区
elif guess<number:
    print('No,it is a little higher than that')#另一块

else:
    print('No,it is a little lower than that')
print('Done')


