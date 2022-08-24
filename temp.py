num = str(input("Enter number: "))
log = len(num)-2
if num == '1':
    print('1')
elif str(int(num) - 10**log+1)[0] == '1' and str(num)[0] == '1':
    num = num[1:]
    num = str(int(num)+1)
    if len(num)-2 == log:
        print(num + num[:-1][::-1])
    else:
        print(num+num[::-1])
else:
    num = int(num)
    if str(num)[0] == '1':
        num = num-10**(log)+1
    else:
        num = num - 10**(log+1)+1
    num = str(int(num))
    print(num + num[:-1][::-1])

'''
num = str(input("Enter number: "))
if len(num) == 1:
    palindrome = num
    if num == '9':
        palindrome = '11'
elif len(num)%2 == 0:
    palindrome = num[:len(num)/2]+num[:len(num)/2][::-1]
    if int(palindrome) <= int(num):
        palindrome = str(int(num[:len(num)/2])+1) + str(int(num[:len(num)/2])+1)[::-1]
        if len(palindrome) > len(num):
            palindrome = str(int(num)+2)
else:
    palindrome = num[:len(num)/2+1]+num[:len(num)/2][::-1]
    if int(palindrome) <= int(num):
        palindrome = str(int(num[:len(num)/2+1])+1)+str(int(num[:len(num)/2+1])+1)[:-1][::-1]
        if int(palindrome) <= int(num):
            palidrome = str(int(num)+2)
print(palindrome)'''