import re

def codon_to_amino_table(code):
    if code == 0:
        return (({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg']))
    elif code == 1:
        return (({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i',
        'ata':'m','atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'stop','agg':'stop',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },{'Bos':['ata'],'Homo':['ata','att'],'Mus':['ata','att','atc'],'Cortunix/Gallus':['gtg']}))
    '''elif code == 2:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l',
        'ctt':'t','ctc':'t','cta':'t','ctg':'t',
        'att':'i','atc':'i',
        'ata':'m','atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r',
        'cgc':'','cga':'',
        'cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 3:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },{'Trypansoma':['tta','ttg','ctg'],'Leishmania':['att','ata'],'Tetrahymena':['att','ata','atg'],'Paramecium':['att','ata','atg','atc','gtg','gta']})'''
    if code == 2:
        return(({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i',
        'ata':'m','atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'s','agg':'s',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },{'Apis':['atc'],'Polyplacophora':['gtg'],'Ascaris/Caenorhabditis':['ttg'],'None of the above':['ata','att']}))
    '''
    elif code == 5:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'q','tag':'q',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 6:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n','aaa':'n',
        'aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s','aga':'s','agg':'s',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 7:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c','tga':'c',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 8:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg','ttg','ctg'])
    elif code == 9:
        return({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l',
        'ctg':'s',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 10:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i',
        'ata':'m','atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'g','agg':'g','ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg','gtg','ttg'])
    elif code == 11:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y','taa':'y',
        'tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n','aaa':'n',
        'aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s','aga':'s','agg':'s',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 12:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop',
        'tag':'q',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 13:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop',
        'tag':'l',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 14:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i',
        'ata':'m','atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n','aaa':'n',
        'aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s','aga':'s','agg':'s',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg','gtg'])
    elif code == 15:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s',
        'tca':'stop',
        'tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop',
        'tag':'l',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 16:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'stop',
        "ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg','att','gtg'])
    elif code == 17:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'w','tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s','aga':'s',
        'agg':'k',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    elif code == 18:
        return ({
        "ttt":"f","ttc":"f",
        "tta":'l',"ttg":'l','ctt':'l','ctc':'l','cta':'l','ctg':'l',
        'att':'i','atc':'i','ata':'i',
        'atg':'m',
        'gtt':'v','gtc':'v','gta':'v','gtg':'v',
        'tct':'s','tcc':'s','tca':'s','tcg':'s',
        'cct':'p','ccc':'p','cca':'p','ccg':'p',
        'act':'t','acc':'t','aca':'t','acg':'t',
        'gct':'a','gcc':'a','gca':'a','gcg':'a',
        'tat':'y','tac':'y',
        'taa':'stop','tag':'stop',
        'cat':'h','cac':'h',
        'caa':'q','cag':'q',
        'aat':'n','aac':'n',
        'aaa':'k','aag':'k',
        'gat':'d','gac':'d',
        'gaa':'e','gag':'e',
        'tgt':'c','tgc':'c',
        'tga':'stop',
        'tgg':'w',
        'cgt':'r','cgc':'r','cga':'r','cgg':'r',
        'agt':'s','agc':'s',
        'aga':'r','agg':'r',
        'ggt':'g','ggc':'g','gga':'g','ggg':'g'
        },['atg'])
    '''



dna = open("/home/emilyblack/dna_reader/input.txt","r").read().strip().lower().replace('u','t')
codons = re.findall("[acgt]{3}",dna)
tables = ['The standard code (1)','The vertebrate mitochondrial code (2)','The invertebrate mitocondrial code (3)']

print('Pick one:\n'+'\n'.join(tables))
table = int(input())-1
(codon_to_amino,starts) = codon_to_amino_table(table)
if type(starts) == dict:
    keys = starts.keys()
    for i in range(len(keys)):
        keys[i] += ' ('+str(i+1)+')'
    print('\n\nPick a taxinomic group:\n'+'\n'.join(keys))
    starts = starts.values()[input()-1]

proteins = []
start = False
protein = ""
for codon in codons:
    if not start and codon in starts:
        start = True
    elif start:
        amino = codon_to_amino[codon]
        if amino == 'stop':
            start = False
            proteins.append(protein.upper())
            protein = ''
        else:
            protein += amino

out = open("/home/emilyblack/dna_reader/output.txt","w")
out.write('\n'.join(proteins))
out.close()