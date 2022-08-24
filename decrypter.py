s_n = {'q':1,'w':2,'e':3,'r':4,'t':5,'y':6,'u':7,'o':8,'p':9,'a':10,'s':11,'d':12,'f':13,'g':14,'h':15,'j':16,'k':17,'l':18,'z':19,'x':20,'c':21,'v':22,'b':23,'n':24,'m':25,'i':26,'1':27,'2':28,'3':29,'4':30,'5':31,'6':32,'7':33,'8':34,'9':35,'0':36,' ':37,',':38,'.':39,'Q':40,'W':41,'E':42,'R':43,'T':44,'Y':45,'U':46,'I':47,'O':48,'P':49,'A':50,'S':51,'D':52,'F':53,'G':54,'H':55,'J':56,'K':57,'L':58,'Z':59,'X':60,'C':61,'V':62,'B':63,'N':64,'M':65,'`':66,'!':68,'$':71,'%':72,'^':73,'&':74,'*':75,'(':76,')':77,'-':78,'_':79,'=':80,'+':81,'  ':82,'[':83,'{':84,']':85,'}':86,';':87,':':88,'@':90,'#':91,'~':92,'|':93,'<':67,'>':89,'/':69,'?':70}
n_s = {v: k for k, v in s_n.iteritems()}
stage1 = raw_input()
stage2 = list(stage1)
length = len(stage1)
primes = list(np.load('primes_to_10000.npy')[0])
squares = list(np.load('squares.npy')[0])
fib = list(np.load('fibbonachi.npy')[0])

for i in range(0,length):
    stage2[i] = s_n[stage2[i]]

key = []

for j in range(0,5):
    key.append(stage2.pop())
key.reverse()
length = len(stage2)

for k in range(0,length):
    stage2[k] = (stage2[k]+len(s_n)-key[k%5]-squares[k%len(squares)]+primes[k%len(primes)]-1)%len(s_n)

stage2.reverse()

for l in range(length):
    stage2[l] = n_s[stage2[l]]
stage3 = ''

for m in range(0,length):
    stage3 = stage3+stage2[m]
stage3.replace('//','''
''')
print stage3