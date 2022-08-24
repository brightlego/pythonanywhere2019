execfile('ln.py')
execfile('latin_endings.py')


pretrans = ''
while pretrans.lower() != 'quit':
    pretrans = raw_input()
    translation = False
    incorect_stems = []
    for h in range(len(ln)):
        if translation == False:
            posttrans = ''
            tense = []
            stem = []
            conjugation = []
            ending = []
            pronoun = []
            len_stem = []
            english = []
            stem_num = []
            for i in range(len(ln)):
                for j in range(len(ln[i])-3,0,-1):
                    if pretrans.startswith(ln[i][j]) and len(ln[i][j]) < len(pretrans) and i not in incorect_stems:
                        conjugation.append(ln[i][len(ln[i])-2])
                        stem.append(ln[i][j])
                        len_stem.append(len(ln[i][j]))
                        tense.append(j-1)
                        english.append(ln[i][len(ln[i])-1])
                        stem_num.append(i)
            conj_stem = zip(len_stem,conjugation,stem,tense,english,stem_num)
            conj_stem.sort(reverse = True)
            if len(conj_stem) > 0:
                conj_stem = conj_stem[0]
                for i in range(len(ln_end[conj_stem[1]][conj_stem[3]])):
                    for j in range(6):
                        if pretrans == conj_stem[2] + ln_end[conj_stem[1]][conj_stem[3]][i][j]:
                            ending.append(en_end[conj_stem[3]][i][j])
                            pronoun.append(en_pron[conj_stem[3]][i][j])
                            translation = True
                if translation == True:
                    posttrans = conj_stem[4]
                if posttrans.endswith('y') and len(ending[0]) > 0 and not ending[0].startswith('i'):
                    posttrans = ''.join(list(posttrans)[:len(posttrans)-1])+'ie'
                if posttrans.endswith('e') and (ending[0].startswith('e') or ending[0].startswith('i')):
                    posttrans = ''.join(list(posttrans)[:len(posttrans)-1])
                if translation == True:
                    posttrans += ending[0]
                    if posttrans in en_irreg[0]:
                        posttrans = en_irreg[1][en_irreg[0].index(posttrans)]
                    posttrans = pronoun[0] + ' ' + posttrans
                if posttrans.startswith(' '):
                    posttrans = posttrans[1:]
                incorect_stems.append(conj_stem[5])
    if translation == True:
        print posttrans
    elif pretrans.lower() != 'quit':
        print 'Your Latin is incorrect'
    print '\n'
