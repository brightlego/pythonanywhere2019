import numpy as np
import random
s_n = {'q':1,'w':2,'e':3,'r':4,'t':5,'y':6,'u':7,'o':8,'p':9,'a':10,'s':11,'d':12,'f':13,'g':14,'h':15,'j':16,'k':17,'l':18,'z':19,'x':20,'c':21,'v':22,'b':23,'n':24,'m':25,'i':26,'1':27,'2':28,'3':29,'4':30,'5':31,'6':32,'7':33,'8':34,'9':35,'0':36,' ':37,',':38,'.':39,'Q':40,'W':41,'E':42,'R':43,'T':44,'Y':45,'U':46,'I':47,'O':48,'P':49,'A':50,'S':51,'D':52,'F':53,'G':54,'H':55,'J':56,'K':57,'L':58,'Z':59,'X':60,'C':61,'V':62,'B':63,'N':64,'M':65,'`':66,'!':68,'$':71,'%':72,'^':73,'&':74,'*':75,'(':76,')':77,'-':78,'_':79,'=':80,'+':81,'  ':82,'[':83,'{':84,']':85,'}':86,';':87,':':88,'@':90,'#':91,'~':92,'|':93,'<':67,'>':89,'/':69,'?':70}
n_s = {v: k for k, v in s_n.iteritems()}

key = [random.randint(1,len(s_n)),random.randint(1,len(s_n)),random.randint(1,len(s_n)),random.randint(1,len(s_n)),random.randint(1,len(s_n))]

primes = list(np.load('primes_to_10000.npy')[0])
squares = list(np.load('squares.npy')[0])
fib = list(np.load('fibbonachi.npy')[0])

stage1 = raw_input()
stage1 = stage1.replace('''
''', '//')

stage2 = []
i = 0
while i < len(stage1):
    stage2.append(stage1[i])
    i = i+1
i = 0
stage2.reverse()

while i < len(stage1):
    stage2[i] = s_n[stage2[i]]
    i = i + 1
stage3 = stage2
i = 0
while i < len(stage2):
    stage3[i] = ((stage3[i]+key[i%5]+squares[i%len(squares)]-primes[i%len(primes)])%len(s_n))+1
    i = i+1
i = 0
stage4 = stage3
while i <len(stage3):
    stage4[i] = n_s[stage4[i]]
    i = i+1
stage5 = ''
i = 0
while i <len(stage4):
    stage5 = stage5+stage4[i]
    i = i+1

i = 0
while i <len(key):
    key[i] = n_s[key[i]]
    i = i+1
i = 0
while i <len(key):
    stage5 = stage5+key[i]
    i = i+1
print stage5