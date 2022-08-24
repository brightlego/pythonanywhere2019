alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def sample2002():
    def q1ab():
        nfriends = input('How many friends? ')
        nwords = input('How many words in the rhyme? ')
        friends = []
        for i in range(0,nfriends):
            friends.append(i)
        j = 0
        order_ = []
        for i in range(0,nfriends-1):
            j = (j+nwords-1)%len(friends)
            order_.append(str(friends[j]+1))
            del friends[j]
        return(friends,order_)
    def q2a():
        alphabet = list('ABCDEFGHIJKLMNOPRSTUVWXYZ')
        alphabet = [alphabet[:],alphabet[:]]
        keys = [list(raw_input().upper()),list(raw_input().upper())]
        for i in range(0,2):
            j = 0
            while j < len(keys[i])-1:
                k = j+1
                while k < len(keys[i]) and k > j:
                    if keys[i][j] == keys[i][k]:
                        del keys[i][k]
                    k+=1
                j+=1
        grids = [[[],[],[],[],[]],[[],[],[],[],[]]]
        gridlen = [0,0]
        for h in range(0,2):
            for i in range(1,(len(keys[h])/5)+2):
                grids[h][i-1] = keys[h][5*(i-1):5*i]
                gridlen[h] += len(keys[h][5*(i-1):5*i])
                for j in range(0,len(keys[h][5*(i-1):5*i])):
                    alphabet[h].remove(keys[h][5*(i-1)+j])
        for i in range(0,2):
            apos = 0
            for j in range(gridlen[i],25):
                grids[i][j/5].append(alphabet[i][apos])
                apos+=1
        for i in range(0,5):
            grids[1][i].reverse()
        grids[1].reverse()
        type_ = ''
        for i in range(0,5):
            print ' '.join(grids[0][i]) + '     ' + ' '.join(grids[1][i])
        while type_ != 'Q':
            print ''
            type_ = ''
            while type_ != 'E' and type_ != 'D' and type_ != 'Q':
                type_ = raw_input().upper()
            code = ''
            if type_ != 'Q':
                code = list(raw_input().upper())
            if type_ == 'E':
                direction = 1
            elif type_ == 'D':
                direction = -1
            if len(code)%2 == 1 and type_ == 'E':
                code.append('X')
            encryption = []
            if type_ != 'Q':
                i = 0
                while i < len(code):
                    sline = 0
                    for j in range(0,5):
                        if code[i] in grids[0][j] and code[i+1] in grids[1][j]:
                            encryption.extend([grids[0][j][(grids[0][j].index(code[i])+direction)%len(grids[0][j])],grids[1][j][(grids[1][j].index(code[i+1])+direction)%len(grids[1][j])]])
                        elif code[i] in grids[0][j]:
                            for k in range(0,5):
                                if code[i+1] in grids[1][k]:
                                    encryption.extend([grids[0][k][grids[0][j].index(code[i])],grids[1][j][grids[1][k].index(code[i+1])]])
                    i+=2
                if type_ == 'D' and ''.join(encryption).endswith('X'):
                    del encryption[len(encryption)-1]
                print ''.join(encryption)



    question = input('What question number do you want? ')
    if question == 1:
        friends,order = q1ab()
        print 'a:', friends[0]+1
        print 'b:', ', '.join(order)
    if question == 2:
        print 'a:'
        q2a()
        print 'b:', 2*4+1*2
        print 'c:', 20*21-1

def BIO2002(question):
    def q1a():
        lojban_decimal = {'pa':'1','re':'2','ci':'3','vo':'4','mu':'5','xa':'6','ze':'7','bi':'8','so':'9','no':'0'}
        lojban = list(raw_input('Lojban: '))
        decimal = []
        for i in range(0,len(lojban)/2):
            decimal.append(lojban_decimal[lojban[2*i]+lojban[(2*i)+1]])
        print 'Number: ' +  ''.join(decimal)
    def q2():
        def b_(stack):
            stack_ = stack[1:]+stack[0]
            return(stack_)
        def i_(stack):
            stack1 = stack[:(len(stack)/2+len(stack)%2)]
            stack2 = stack[(len(stack)/2+len(stack)%2):]
            stacks = [len(stack1),len(stack2)]
            stacks_ = [stack1,stack2]
            stack_ = []
            for i in range(0,min(stacks)):
                stack_.extend([stack1[i],stack2[i]])
            for i in range(0,max(stacks)-min(stacks)):
                stack.append(stacks_[stacks.index(max(stacks))][i+max(stacks)-min(stacks)])
            return(stack_)
        def o_(stack):
            stack1 = stack[:(len(stack)/2+len(stack)%2)]
            stack2 = stack[(len(stack)/2+len(stack)%2):]
            stacks = [len(stack1),len(stack2)]
            stacks_ = [stack1,stack2]
            stack_ = []
            for i in range(0,min(stacks)):
                stack_.extend([stack2[i],stack1[i]])
            for i in range(0,max(stacks)-min(stacks)):
                stack.append(stacks_[stacks.index(max(stacks))][i+max(stacks)-min(stacks)])
            return(stack_)
        numbers = '1234567890'
        shuffletype = raw_input()
        shuffletype_ = []
        output = ['1','2','3','4','5','6','7','8']
        shuffletype = list(shuffletype)
        i = 0
        while i < len(shuffletype):
            if shuffletype[i] == '(':
                bstart = i
                bend = 0
                for j in range(i,len(shuffletype)):
                    if bend == 0 and shuffletype[j] == ')':
                        bend = j
                if shuffletype[i-1] in numbers:
                    for i in range(1,int(shuffletype[i-1])):
                        shuffletype_.append(shuffletype[bstart:bend+1])
                shuffletype_.append(shuffletype[bstart:bend+1])
                i += bend
            else:
                shuffletype_.append(shuffletype[i])
                i += 1
        shuffletype_v = shuffletype_[0]
        depth = 0
        print shuffletype
        while i < len(shuffletype_):
            shuffletype_v = shuffletype_[:]
            for h in range(0,len(shuffletype_v)):
                if type(shuffletype_v[h]) == list and depth > 0:
                    shuffletype_v = shuffletype_v[h]
                    depth += 1
                elif type(shuffletype_[h]) == list:
                    shuffletype_v = shuffletype_[h]
                    depth += 1
                else:
                    shuffletype_v = shuffletype_[:]
                    if depth > 0:
                        depth -= 1
                if shuffletype_v[h] == 'o':
                    if shuffletype_v[h-1] in numbers:
                        for j in range(1,int(shuffletype_v[h-1])):
                            output.append(o_(shuffletype_v))
                    output.append(o_(shuffletype_v))
                elif shuffletype_v[h] == 'i':
                    if shuffletype_v[h-1] in numbers:
                        for j in range(1,int(shuffletype_v[h-1])):
                            output.append(i_(shuffletype_v))
                    output.append(i_(shuffletype_v))
                elif shuffletype_v[h] == 'b':
                    if shuffletype_v[h-1] in numbers:
                        for j in range(1,int(shuffletype_v[h-1])):
                            output = (b_(output))
                    output = (b_(output))
            i += 1
        print ' '.join(output)
    if question == 1:
        print 'a:'
        q1a()
        print 'b:\npareno'
        print 'c:\nnozeci'
    if question == 2:
        q2()