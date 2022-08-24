def cs():
    for i in range(16):
        print('\n')

def is_int(string):
    numbers = '0123456789.-'
    is_int_v = True
    for i in string:
        if i not in numbers:
            is_int_v = False
    return(is_int_v)

def is_letter_or_number(string):
    letters_and_numbers = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890- '
    valid = True
    for i in string:
        if i not in letters_and_numbers:
            valid = False
    return(valid)

def create_database(data_names_used):
    data_name = data_names_used[0]
    while data_name in data_names_used:
        while not is_letter_or_number(data_name):
            cs()
            data_name = raw_input('What do you want your database to be called? (only letters, numbers, spaces and hyphens)\n')
    data_names_a = open('/home/emilyblack/database/data_names.txt', 'a')
    data_names_a.write('\n' + data_name)
    data_names_a.close()
    new_database = open('/home/emilyblack/database/data/' + data_name + '.txt','w')
    cs()
    data_base_value_names = raw_input("What different names do you want to give your values? (separate with ', ')\n")
    new_database.write(data_base_value_names + ', 0')
    new_database.close()
    return()

def append_database(data_names_used):
    database = '='
    while database not in data_names_used:
        cs()
        database = raw_input('Which database do you want to append to?\n')
    database_r = open('/home/emilyblack/database/data/' + database + '.txt', 'r')
    database_l = database_r.read().split('\n')
    values = database_l[0].split(', ')
    values.pop()
    database_l.reverse()
    database_l[0] = database_l[0].split(', ')
    database_l[0].reverse()
    next_index = int(database_l[0][0])+1
    database_r.close()
    database_a = open('/home/emilyblack/database/data/' + database + '.txt', 'a')
    while True:
        cs()
        new_data_name = raw_input('What do you want to call the new data? (press enter to quit)\n')
        if new_data_name == '':
            database_a.close()
            return()
        database_a.write('\n')
        database_a.write(new_data_name)
        for i in values:
            new_value = 'a'
            while not is_int(new_value):
                cs()
                new_value = raw_input(i + ': ')
            database_a.write(', '+ new_value)
        database_a.write(', ' + str(next_index))
    return()

def delete_from_database(data_names_used):
    database = '='
    while database not in data_names_used:
        cs()
        database = raw_input('Which database do you want to delete from?\n')
    database_r = open('/home/emilyblack/database/data/' + database + '.txt', 'r')
    database_l = database_r.read().split('\n')
    values = database_l[0]
    database_l = database_l[1:]
    cs()
    print('Which data do you want to delete? ')
    for i in range(len(database_l)):
        print(database_l[i][:len(database_l[i])-1])
        database_l[i] = database_l[i].split(', ')
    database_r.close()
    non_existing_data = True
    while non_existing_data:
        data_to_delete = raw_input()
        i = 0
        found = False
        while i < len(database_l) and not found:
            if data_to_delete == database_l[i][0]:
                non_existing_data = False
                del database_l[i]
                found = True
            else:
                i+=1
    for i in range(len(database_l)):
        database_l[i] = ', '.join(database_l[i])
    database_l = '\n'.join(database_l)
    database_w = open('/home/emilyblack/database/data/' + database + '.txt', 'w')
    database_w.write(values + '\n' + database_l)
    database_w.close()
    return()

def read_database(data_names_used):
    database = '='
    while database not in data_names_used:
        cs()
        database = raw_input('Which database do you want to read?\n')
    database_r = open('/home/emilyblack/database/data/' + database + '.txt', 'r')
    database = database_r.read().split('\n')
    values = database[0].split(', ')
    database_r.close()
    for i in range(len(database)):
        database[i] = database[i].split(', ')
    filter_ = ', '
    quit = False
    blacklist = database[1:]
    while not quit:
        filter_ = ', '
        while filter_ not in database[0][:len(database[0])-1] and filter_.lower() != 'name' and filter_ != '':
            cs()
            filter_ = raw_input('What do you want to filter by? (enter to quit or submit) (' +', '.join(database[0][:len(database[0])-1]) + ' or name) \n')
        if filter_.lower() != 'name' and filter_ != '':
            value = database[0].index(filter_)+1
            min_max = ['a','a']
            while not is_int(min_max[0]):
                cs()
                min_max[0] = raw_input('What do you want the minimum value to be? ')
            min_max[0] = int(min_max[0])
            while not is_int(min_max[1]):
                cs()
                min_max[1] = raw_input('What do you want the maximum value to be? ')
                cs()
            min_max[1] = int(min_max[1])
            for i in database[1:]:
                if not (float(i[value]) <= min_max[1] and float(i[value]) >= min_max[0]):
                    if i in blacklist:
                        blacklist.remove(i)
        elif filter_ != '':
            cs()
            start_with = raw_input('What do you want the name to start with? (leave blank for ' + "don't" + ' care)\n')
            cs()
            end_with = raw_input('What do you want the name to end with? (leave blank for ' + "don't" + ' care)\n')
            cs()
            in_name = raw_input('What do you want to be in the name? (leave blank for ' + "don't" + ' care)\n')
            cs()
            for i in database[1:]:
                if not (i[0].startswith(start_with) and i[0].endswith(end_with) and in_name in i[0]):
                    if i in blacklist:
                        blacklist.remove(i)
        else:
            cs()
            quit = True
            for i in blacklist:
                data = i[0] + ': '
                for j in range(len(i[1:len(i)-1])):
                    data += i[j+1] + ' (' + values[j] + '), '
                print(data)
    if len(blacklist) > 0:
        raw_input()
    return()

def modify_database(data_names_used):
    database_name = '='
    while database_name not in data_names_used:
        cs()
        database_name = raw_input('Which database do you want to modify?\n')
    while True:
        database_r = open('/home/emilyblack/database/data/' + database_name + '.txt', 'r')
        database = database_r.read().split('\n')
        values = database[0].split(', ')
        values.pop()
        database_r.close()
        cs()
        valid_names = []
        for i in range(len(database)):
            database[i] = database[i].split(', ')
            valid_names.append(database[i][0])
        del valid_names[0]
        data_to_modify = ', '
        while data_to_modify not in valid_names and data_to_modify != '':
            for i in range(1,len(database)):
                print(database[i][0] + ': ' + ', '.join(database[i][1:len(database[i])-1]))
            data_to_modify = raw_input('Which of these do you want to modify? (press enter to quit) ')
            cs()
        if data_to_modify == '':
            return()
        data_to_modify = valid_names.index(data_to_modify) + 1
        value_to_modify = ', '
        while value_to_modify not in values and value_to_modify.lower() != 'name':
            print(database[data_to_modify][0] + ':')
            for i in range(len(database[data_to_modify])-2):
                print(values[i] + ': ' + database[data_to_modify][i+1])
            value_to_modify = raw_input('Which value (' + ', '.join(values) + ' or name) do you want to modify?\n')
            cs()
        if value_to_modify == 'name':
            modified_value = raw_input('What do you want the new name to be? ')
            cs()
            database[data_to_modify][0] = modified_value
        else:
            modified_value = 'a'
            while not is_int(modified_value):
                print(database[data_to_modify][0] + ':')
                for i in range(len(database[data_to_modify])-2):
                    print(values[i] + ': ' + database[data_to_modify][i+1])
                modified_value = raw_input('What do you want the new ' + value_to_modify + ' to be? ')
                cs()
            database[data_to_modify][values.index(value_to_modify)+1] = modified_value
        for i in range(len(database)):
            database[i] = ', '.join(database[i])
        database = '\n'.join(database)
        database_w = open('/home/emilyblack/database/data/' + database_name + '.txt', 'w')
        database_w.write(database)
        database_w.close()

def add_value(data_names_used):
    database_name = '='
    while database_name not in data_names_used:
        cs()
        database_name = raw_input('Which database do you want to add a field?\n')
    cs()
    value_name = raw_input('What do you want the new field to be called?\n')
    database_r = open('/home/emilyblack/database/data/' + database_name + '.txt', 'r')
    database = database_r.read()
    database = database.split('\n')
    for i in range(len(database)):
        database[i] = database[i].split(', ')
    database[0].insert(len(database[0])-1,value_name)
    database[0] = ', '.join(database[0])
    for i in range(1,len(database)):
        new_value = 'a'
        while not is_int(new_value):
            cs()
            new_value = raw_input('What do you want ' + value_name + ' in ' + database[i][0] + ' to be? ')
        database[i].insert(len(database[i])-1,new_value)
        database[i] = ', '.join(database[i])
    database = '\n'.join(database)
    database_w = open('/home/emilyblack/database/data/' + database_name + '.txt', 'w')
    database_w.write(database)
    database_w.close()
    return()

quit = False
while not quit:
    data_names_used_r = open('/home/emilyblack/database/data_names.txt', 'r')
    data_names_used = data_names_used_r.read()
    data_names_used = data_names_used.split('\n')
    data_names_used_r.close()
    cs()
    type_ = raw_input('Do you want to make a new database (N), append to an existing one (A), delete from an existing \none (D), modify an existing one (M), create a new field (F) read one (R) or quit (enter)?\n').upper()
    if type_ == 'N':
        create_database(data_names_used)
    elif type_ == 'A':
        append_database(data_names_used)
    elif type_ == 'D':
        delete_from_database(data_names_used)
    elif type_ == 'R':
        read_database(data_names_used)
    elif type_ == 'M':
        modify_database(data_names_used)
    elif type_ == 'F':
        add_value(data_names_used)
    else:
        quit = True


