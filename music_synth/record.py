from time import time,sleep
from os import system
import re
def clear():
    _ = system('clear')

raw_input('Press ENTER to start recording 10s clip.')
clear()
st = time()
recording = '0'
hex_ = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while time()-st < 10:
    clear()
    print('Press ENTER to record sound.')
    bt = time()
    raw_input('')
    et = time()
    t = et-bt
    t = [t//16,int(t%16),t%1]
    t[2] = int(1/t[2])
    if t[1] > 0:
        recording += '0F'*int(t[0]) + '0' + hex_[t[1]]
    if t[2] < 36:
        recording += hex_[t[2]]

clear()
print('Playing audio (at 0.5x speed).')
rec = re.findall('0?\w',recording)
for i in rec:
    if not i.startswith('0'):
        i = hex_.index(i)
        i = 1.0/i
        sleep(i*2)
        print('\x07')
    else:
        i = hex_.index(i[1])
        sleep(i*2)