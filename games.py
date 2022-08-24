continue_ = 1
while continue_ == 1:
    game_ = input('''What game do you want to play?
1 for O and X
2 for 21
3 for monopoly
''')
    if game_ == 1:
        execfile('O_and_X.py')
    elif game_ == 2:
        execfile('twentyone.py')
    elif game_ == 3:
        execfile('mono.py')
        movement_money()
    continue_ = input('Do you want to contine? (1 for yes) ')
