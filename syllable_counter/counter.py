import re
def count_syllables(line):
    vowels = ['a','e','i','o','u','y']
    dipthongs = [
        'aa','ae','ai','au','ay',
        'ea','ee','ei','eo','ey',
        'ie','io',
        'oe','oi','oo','ou','oy',
        'ya','ye','yi','yo','yu']
    syllables = []
    selected_syllable = ''
    for i in range(len(line)):
        selected_syllable += line[i]
        #print(selected_syllable)
        if i != 0 or line[i] != 'y' or not(i != 0 and re.match('\s',line[i-1])):
            if line[(i-1)%len(line)] + line[i] in dipthongs and i != 0:
                syllables.append(selected_syllable)
                selected_syllable = ''
            elif line[i] + line[(i+1)%len(line)] in dipthongs and i != len(line)-1:
                ''
            elif line[i] in vowels:
                syllables.append(selected_syllable)
                selected_syllable = ''
            elif line[i] == ' ':
                selected_syllable = ''
    print syllables
    return(len(syllables))

text = open('/home/emilyblack/syllable_counter/input.txt','r').read().strip().split('\n')
syllable_count = []
for i in text:
    syllable_count.append(str(count_syllables(i)))
print(' '.join(syllable_count))