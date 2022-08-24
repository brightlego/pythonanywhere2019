s_n = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
n_s = {v: k for k, v in s_n.iteritems()}
stage1 = raw_input()
stage5 = stage1
stage1 = stage1.lower()
stage1 = stage1.replace(' ','')
stage4 = []
for i in range(0,26):
    stage1 = stage1.replace(' ','')
    stage2 = list(stage1)
    for j in range(0,len(stage1)):
        stage2[j] = n_s[(s_n[stage2[j]]+i)%26]
    stage3 = ''
    for k in range(0,len(stage5)):
        if stage2[k] != stage5[k]:
            if stage5[k] == ' ':
                stage2.insert(k,' ')
    for m in range(0,len(stage5)):
        if stage5[m] == stage5[m].upper():
            stage2[m] = stage2[m].upper()
    for l in range(0,len(stage2)):
        stage3 =stage3 + stage2[l]
    print stage3 + ';','rot',i,'''
    '''