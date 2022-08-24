# This Python file uses the following encoding: utf-8
from random import randint
from time import ctime
import numpy as np
from random import choice
import os

def cs(lines):
    for i in range(lines):
        print ''


def encrypt(message,transformation_key,encryption_key):
    transformation_key_key = ['9','j','H']
    chosen_transformation = randint(0,2)
    encryption_key_key = ['q','S','T','w','E']
    chosen_encryption = randint(0,4)
    for i in range(len(message)):
        message[i] = transformation_key[(chosen_transformation + i)%3].index(message[i])
        message[i] = encryption_key[(chosen_encryption + i)%5][message[i]]
    message.extend([transformation_key_key[chosen_transformation],encryption_key_key[chosen_encryption]])
    return(message)

def decrypt(message,transformation_key,encryption_key_):
    transformation_key_key = ['9','j','H']
    encryption_key_key = ['q','S','T','w','E']
    chosen_encryption = encryption_key_key.index(message[len(message)-1])
    chosen_transformation = transformation_key_key.index(message[len(message)-2])
    del message[len(message)-2:]
    for i in range(len(message)):
        message[i] = encryption_key[(chosen_encryption+i)%5].index(message[i])
        message[i] = transformation_key[(chosen_transformation+i)%3][message[i]]
    return(message)


def shuffle(list_):
    prime_key = [5,3,4,7,6]
    prime_code = ['M','u','H','c','Z']
    prime_key_choice = randint(0,4)
    i = 0
    while i<11 or len(list_)%prime_key[prime_key_choice]  == 0:
        list_.insert(randint(0,len(list_)-1),choice(['`','¬','£']))
        i+= 1
    for h in range(prime_key[prime_key_choice]):
        list_n = []
        for i in range((len(list_)/prime_key[prime_key_choice])+1):
            list_n.append([])
        for i in range(len(list_)):
            list_n[i/prime_key[prime_key_choice]].append(list_[i])
        list_n_ = []
        for i in list_n:
            i.reverse()
            list_n_ += i
        list_ = list_n_
        list_.append(list_[0])
        del list_[0]
    list_.append(prime_code[prime_key_choice])
    return(list_)

def deshuffle(list_):
    prime_key = [5,3,4,7,6]
    prime_code = ['M','u','H','c','Z']
    prime_key_choice = prime_code.index(list_[len(list_)-1])
    list_.pop()
    for h in range(prime_key[prime_key_choice]):
        list_.insert(0,list_.pop())
        list_n = []
        for i in range((len(list_)/prime_key[prime_key_choice])+1):
            list_n.append([])
        for i in range(len(list_)):
            list_n[i/prime_key[prime_key_choice]].append(list_[i])
        list_n_ = []
        for i in list_n:
            i.reverse()
            list_n_ += i
        list_ = list_n_
    while '`' in list_:
        list_.remove('`')
    while '\xc2\xa3' in list_:
        list_.remove('\xc2\xa3')
    while '\xc2\xac' in list_:
        list_.remove('\xc2\xac')
    return(list_)

transformation_key = [
['"', 'B', 'O', '/', 'w', '*', 'H',' ', '!', '~', ';', 'F', 'Q', 'n', 'p', '1', '.', 'h', 'I', 'u', '8', 'l', 'V', "'", 'r', 'k', '4', '7', '?',
'[', 'm', 'U', '(', '^', '5', '_', 'f', 'e', 't', 'x', 'J', 'Z', 'P', '9', '+', ']', ',', '>', 'D', 'X', '|', 'C', 'R', 'b', 'G', 'S', 'z', 'a', '\\', 'Y', 'M',
'%', 'v', '=', 's', 'o', 'A', ':', 'L', 'T', '}', 'g', '<', 'E', ')', '$', '@', '0', 'i', 'c', '&', '2', '3', 'W', 'y', 'N', 'K', 'q', '-', '{', 'd', 'j', '6'],

['9', '1', 'w', '\\', '>', '<', 'M', '?', 'y', "'", '}', '4', ')', '@', 'p', 'n', '0', 'W', 'S', 'r', '5', '^', '{', 'Y', 'R', 'C', 's', '%', 'F', 'z',
'H', '_', 'X', 'b', 'A', 'E', '=', 'c', 'Q', 'D', 'K', 'i', 'P', '"', '/', ']', 'e',' ', 'm', '.', ':', '2', 'I', 'N', 'V', 'a', 'Z', '[', 'O', 'U', 'q', 'o'
, 'L', 'J', '7', 'd', 'f', 'T', 'G', 'g', '&', '(', '#', ';', 'k', '!', 'u', 'x', 'h', 'v', '3', '|', 't', 'B', ',', '-', '6', 'j', '~', '$', '*', 'l',
'+', '8'],

['b', 's', ']', 'y', 'I', 'e', 'K', 'd', 'h', 'U', '!', 'C', 'g', 'V', '4', 'R', '-', 'N', '3', 'W', 'H', '>', '6', 'J', 'Y', 't', 'k', '<', 'j', 'X',
'q', 'O', 'i', '*', '=', 'P', 'r', "'", '+', 'E', 'G', 'p', '^', '{', 'v', 'F', '"', '?', '0', 'A', '1', '%', 'c', 'B', '8', 'T', '$', 'x', '7', '[', '/',
'o', '#', 'm', '|', 'S', '~', '9', ',', '&', '_', 'Z', '(', 'D', 'z', 'Q', 'f',' ', '}', 'w', '2', ':', 'u', 'M', 'L', ')', '5', '.', '@', 'a', 'n', ';',
'\\', 'l']]

encryption_key = [
['L', '@', 't', 'V', 'R', 'l', '%', '4', 'k', 'W', '#', ';', '7', 'm', '5', '2', '~', '3', 'e', '>', '0', 'a', 'h', '[', '+', 'v', 'G', 'N', '_', 'z',
'o', 'r', 'U', ')', 'S', '^', 'H', 'p', '?', 'O', 'i', 'K', '!', 'b', 'I', '{', 'X', '=', ',', '|', '"', 'T', '-', '$', 'B', ']', 'Y', 'j', 'J', 's', 'c',
'A', 'w', 'n', '}', 'y', 'D', ':', 'u', '1', '*', 'Q', 'Z', '8', 'P', '9', '&', 'f', 'E', 'g', '.', "'",' ', 'F', '6', 'C', '(', 'd', 'M', '/', 'x',
'q', '<'],

['c', 'n', 'M', 'k', 'p', '?', 'x', '"', '[', 'e', '}', '$', 'A', 'q', "'", 'm', 'B', 'y', '{', 'V', '/', 'f', '%', '=', 'i', ':', '|', '2', 'U', '3',
'Y', 'h', 'z', '1', '-', '(', 'b', '.', 'g', '>', '9',' ', 'I', 'u', 'L', 'Q', 'O', 'W', '*', '&', 'j', '5', 'K', 'w', 's', 'T', 'o', ',', 'Z', '#', '_', 't',
'r', 'S', 'X', ';', '7', ')', '8', 'C', ']', 'v', 'H', '4', 'P', 'N', 'J', 'd', 'l', '+', '6', 'R', '0', 'G', 'a', '^', 'D', 'E', 'F', '!', '@',
'<', '~'],

['t', '~', '$', 'f', '?', 'A', '-', '.', 'R', '3', '#', 'S', '!', 'g', '>', '%', 'X', '@', 'x', '9', 'u', 'K', '"', '5', 'O', 'm', 'J', 'a', 'W', 'Q',
'p', 'Z', '4', ']', 's', 'o', ',', 'j', '0', '\\',' ', 'C', 'e', 'q', 'd', 'c', '+', '|', 'B', 'i', 'l', 'k', 'I', 'w', '(', 'D', 'N', 'n', 'y', ')', 'r', 'T',
'=', 'H', '}', 'G', ';', 'P', 'L', '2', '&', 'E', '^', 'z', '8', '{', 'M', '7', 'F', '_', '6', '*', 'V', 'h', 'U', 'v', 'b', "'", '[', '1', '/', ':',
'Y', '<'],

['.', 's', '-', 'j', 'U', '(', 'h', 'N', '@', '2', '<', 'l', 'O', '8', '+', 'H', 'g', 'G', 'X', '_', '[', 'r', '?', '|', 'd', '#', "'", '7', 'a', 'e', '*',
'^', 't', 'L', 'S', 'Q', 'z', 'F', 'p', ',', 'c', '\\', 'v', 'J', 'R',' ', '{', '9', 'Z', 'o', 'x', 'K', '=', 'w', '6', '4', '/', 'B', 'n', '"', 'i', 'T',
'C', '5', 'V', 'b', 'W', '&', 'P', '!', ';', 'E', 'u', '0', '>', 'D', ':', 'm', '~', ']', '$', 'y', '%', 'q', '3', ')', 'Y', 'M', 'A', '1', '}', 'I',
 'k', 'f'],

['y', '@', 'L', '1', 'x', 'V', '=', 'u', 'v', ':', ',', 'E', '-', 'I', '&', '}', '|', 'f', 'e', "'", '3', 'R', 'G', '>', 'M', '_', 'X', '9', '\\', 'U',
'a', '<', '/', 'D', 'N',' ', '%', 'C', 'F', 'j', 'b', ')', '6', 'P', 'n', 'O', '8', 'm', 'Q', '*', '"', '0', '7', '?', '+', 'i', 'c', 'K', 'd', '!', '#', 'w',
'$', 'o', '[', '(', 'S', 'H', 'Z', 'l', '.', 'g', '~', 'B', 'z', 'k', 'J', 'h', 't', ']', '5', 'T', '4', '{', 'r', 'q', 'W', 'p', 'Y', 's', ';', '2',
'A', '^']]
lines = 32
quit = False
cs(lines)
account = raw_input('Do you want to make a new account (N) or log into an existing one (L)? ').upper()
cs(lines)
usernames_ = open('/home/emilyblack/john_misc/encrypter_mk2/usernames.txt','r')
usernames = usernames_.read().split('\n')
usernames_.close()
if account == 'N':
    username = usernames[0]
    while username in usernames:
        username = raw_input('What do you want your username to be? ')
        cs(lines)
        if username in usernames:
            print('That username is already used, try again.')
    usernames_ = open('/home/emilyblack/john_misc/encrypter_mk2/usernames.txt','a')
    usernames_.write('\n' + username)
    usernames_.close
    usernames_ = open('/home/emilyblack/john_misc/encrypter_mk2/usernames.txt','r')
    usernames = usernames_.read().split('\n')
    usernames_.close()
    password = raw_input('What do you want your password to be, ' + username + '? ' )
    cs(lines)
    password = list(password)
    password = encrypt(password,transformation_key,encryption_key)
    password = ''.join(password)
    os.makedirs('/home/emilyblack/john_misc/encrypter_mk2/user-' + username)
    settings = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','w')
    settings.write(password)
    settings.write('\n20')
    settings.close()
    inbox = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/inbox.txt','w')
    inbox.close()
    outbox = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/outbox.txt','w')
    outbox.close()
else:
    username = 0
    while username not in usernames:
        username = raw_input('What is your username? ')
        cs(lines)
        if username not in usernames:
            print('That username does not exist, try again.')
    correct_password = False
    while not correct_password:
        password_ = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','r')
        password = password_.read().split('\n')[0]
        password_.close()
        password = list(password)
        password = decrypt(password,transformation_key,encryption_key)
        password = ''.join(password)
        password_attempt = raw_input('What is your password? ')
        cs(lines)
        correct_password = (password_attempt == password)
        if not correct_password:
            print('That is not ' + username + "'s password, try again. ")
settings = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','r')
lines = int(settings.read().split()[1])
settings.close()
while not quit:
    encrypt_or_decrypt = raw_input('Do you want to send a message (M), look at your inbox (I), look at your outbox (O),\nlook at your settings (S) or quit (Q)? ').lower()
    cs(lines)
    if encrypt_or_decrypt == 'm':
        message = raw_input('What message do you want to encrypt? ')
        cs(lines)
        message = list(message)
        message = encrypt(message,transformation_key,encryption_key)
        message = shuffle(message)
        message = ''.join(message)
        user_to = 0
        while user_to not in usernames:
            user_to = raw_input('Who do you want to send this message to? ')
            if user_to not in usernames:
                print('That username does not exist, try again.\n')
        sent_message = open("/home/emilyblack/john_misc/encrypter_mk2/user-" + user_to + "/inbox.txt",'a')
        sent_message.write('\nnewmessage+ctime ' + ctime() + ' ' + username + ': ' + ' ctime,message ' + message)
        saved_message = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/outbox.txt','a')
        password_ = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','r')
        password = password_.read().split('\n')[0]
        password_.close()
        saved_message.write('\nnewmessage+ctime ' + ctime() + ' ' + user_to + ': ' + ' ctime,message ' + message)
        sent_message.close()
        saved_message.close()
    elif encrypt_or_decrypt == 'i' or encrypt_or_decrypt == 'o':
        if encrypt_or_decrypt == 'i':
            previous_encryptions = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/inbox.txt','r')
        else:
            previous_encryptions = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/outbox.txt','r')
        previous_encryption_list = ''.join(previous_encryptions.readlines()).split('\nnewmessage+ctime ')
        previous_encryption_list.reverse()
        page_ = 0
        option_picked = False
        for i in range(len(previous_encryption_list)):
            previous_encryption_list[i] = previous_encryption_list[i].split(' ctime,message ')
        while not option_picked:
            print 'Page' + str(page_+1) + '\n'
            for i in range(len(previous_encryption_list[lines*page_:lines*(page_+1)])):
                if previous_encryption_list[i + lines*page_][0] != '':
                    print previous_encryption_list[i + lines*page_][0] + ' (' + str(i+1) + ')'
            message = raw_input('Which message? (N for next page, P for previous and E for exit) ')
            cs(lines)
            if message.upper() == 'P':
                page_ -= 1
            elif message.upper() == 'N':
                page_ += 1
            elif message.upper() == 'E':
                option_picked = True
                message = '```\xc2\xac\xc2\xacT\xc2\xa3\xc2\xa3H`\xc2\xac\xc2\xac`u'
            else:
                message = int(message)
                message = previous_encryption_list[message + lines*page_ - 1][1]
                option_picked = True
        message = list(message)
        i = 0
        message_ = []
        while i < len(message):
            if message[i] == '\xc2':
                if message[i+1] == '\xac':
                    message_.append('\xc2\xac')
                elif message[i+1] == '\xa3':
                    message_.append('\xc2\xa3')
                i+= 2
            else:
                message_.append(message[i])
                i+= 1
        message = message_
        message = deshuffle(message)
        message = decrypt(message,transformation_key,encryption_key)
        raw_input(''.join(message))
        cs(lines)
        previous_encryptions.close()
    elif encrypt_or_decrypt == 's':
        settings = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','r')
        changed_settings = settings.read().split('\n')
        settings.close()
        settings = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','w')
        setting_quit = False
        while not setting_quit:
            setting_to_change = raw_input('Which setting to you want to change? (P for password, H for screen hight and Q for quit) ').lower()
            cs(lines)
            if setting_to_change == 'p':
                correct_password = False
                while not correct_password:
                    old_password = raw_input('What is your old password? ')
                    cs(lines)
                    password = changed_settings[0]
                    password_.close()
                    password = list(password)
                    password = decrypt(password,transformation_key,encryption_key)
                    password = ''.join(password)
                    correct_password = (password == old_password)
                password = raw_input('What is your new password? ')
                cs(lines)
                password = list(password)
                password = encrypt(password,transformation_key,encryption_key)
                password = ''.join(password)
                changed_settings[0] = password
            elif setting_to_change == 'h':
                i = 0
                screen_hight = ''
                print('Type anything when this is at the top of your screen.')
                while screen_hight == '':
                    screen_hight = raw_input(':')
                    i += 1
                changed_settings[1] = i
            else:
                setting_quit = True
                settings.write(changed_settings[0] + '\n' + str(changed_settings[1]))
                settings.close()
                settings = open('/home/emilyblack/john_misc/encrypter_mk2/user-' + username + '/settings.txt','r')
                lines = int(settings.read().split()[1])
                settings.close()
    else:
        quit = True



