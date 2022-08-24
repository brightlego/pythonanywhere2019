
def main_game():
    pc = -1
    name = 0
    name = raw_input('What is your name? ')
    print('')
    print('Welcome ' + name)
    #chapter 1
    print('''

    ''')
    pc = input('''
    You have woken up in a...
Research facility on a waistland planet (1),
Small wooden lodge in the middle of a forest(2),
or a castle out in the countryside (3).
Plese choose.
    ''')
    print('')
    if pc == 1:
        pc = input('''
You get up and look around. There is a calender lets you know that it is 1st Jan 3017. You pick up a bottle of water and take a sip. There is a plate of food by your side.

What should you do first?
Explore the area and take a look outside first(1),
or eat the breakfast first(2)
        ''')
        if pc == 1:
            print('''

You start to walk to the door when suddenly a hidden hologram springs into life.
"Good morning, ''' + name + '''." Said the man in the hologram, "I, your boss, would like you to go out and investigate an unidentified, wierd object or UWO, that appered on the radar at 00:00 today."
Fearing your Job, you have no choice but to accept.

''')
        elif pc == 2:
            print('''

You star to eat your breakfast when suddenly a hidden hologram springs into life.
"Good morning, ''' + name + '''." Said the man in the hologram, "I, your boss, would like you to go out and investigate an unidentified, wierd object or UWO, that appered on the radar at 00:00 today."
Fearing your Job, you have no choice but to accept.

''')
        print('''
You pull a pressurised thermal suit onto yourself and walk out the air lock. As you strole towards your target, you wander to yourself, 'I wander what this planet was like 1000 years ago'.

Soon you could see a glowing white dot exacly where the UWO is suppost to be.
You, being curious, walk up to the Glowing Dot and as you got closer, time seemed to slow down and when you finaly held your finger out,  you got sucked in to a maze of tubes.
''')
    if pc == 2:
        pc = input('''

You wake up in a comfy bed in a wooden room with wooden furnature. There is a window by your bed and when you look out there is a bird shelter. You feel hungry but you also want to go for a strole in the woods.

What should you do first?
Go for a stole in the woods(1),
or make and eat breakfast(2).

''')

"""
1: space
2: zooologist
3: nobals's child
"""






