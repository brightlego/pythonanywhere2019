global possible_moves
possible_moves = []
for a in ['0','1','2']:
    for b in ['0','1','2']:
        for c in ['0','1','2']:
            for d in ['0','1','2']:
                for e in ['0','1','2']:
                    for f in ['0','1','2']:
                        for g in ['0','1','2']:
                            for h in ['0','1','2']:
                                for i in ['0','1','2']:
                                    possible_moves.append(a+b+c+d+e+f+g+h+i)

possible_moves_ = []
for i in possible_moves:
    if not(i.count('1') not in [i.count('2'),i.count('2')+1]):
        possible_moves_.append(i)