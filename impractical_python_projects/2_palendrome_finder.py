words = open('/home/emilyblack/impractical_python_projects/words.txt').read().split('\r\n')
print('Palindromes:')
output = ''
for i in words:
    if i == i[::-1]:
        output += i + '    '
print(output)
print('Palingrams:')
output = ''
for i in words:
    for j in words:
        if i+j == (i+j)[::-1]:
            output += i + ' ' + j + '    '
print(output)
