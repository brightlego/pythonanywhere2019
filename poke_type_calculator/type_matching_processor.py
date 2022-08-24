f = open('/home/emilyblack/poke_type_calculator/type matching.txt').read().strip().split('\n')
f[0] = f[0].split('\t')
for i in range(1,len(f)):
    f[i] = f[i].split('\t')
    for j in range(len(f[i])):
        f[i][j] = f[i][j].split(', ')
o_d = {f[0][0]:f[0][1:]}
for i in f[1:]:
    o_d[i[0][0]] = i[1:]

d = {}
for i in o_d.keys():
    if i != 'Type':
        d[i] = {}
        for j in range(2,len(o_d[i])):
            for k in o_d[i][j]:
                if k.endswith(' (Immune)'):
                    d[i][k[:-9]] = 0
                else:
                    d[i][k] = [0.5,2][j-2]
        for j in o_d.keys():
            if j not in d[i] and j != 'Type':
                d[i][j] = 1



flag = True
while flag:
    poke_type = raw_input('Enemy pokemon type(s): ').split()
    flag = False
    for i in poke_type:
        if i not in d:
            print(i+' is not a pokemon type.')
            flag = True
m_d = {0:[],0.25:[],0.5:[],1:[],2:[],4:[]}
for i in d:
    m = 1
    for j in poke_type:
        m *= d[j][i]
    m_d[m].append(i)
for i in sorted(list(m_d)):
    if m_d[i]:
        print(str(i) + ':\t' + ', '.join(m_d[i]))