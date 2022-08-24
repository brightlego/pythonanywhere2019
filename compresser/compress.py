from re import findall
def find_filesize(sec_l):
    d = data[:]
    d = findall('[01]{'+str(sec_l)+'}',d)
    counter = {}
    for i in d:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    k_len = len(bin(len(counter.keys()))[2:])
    d_len = len(d)
    return k_len*d_len+(len(counter.keys())*sec_l*k_len)

global data
global metadata
global counter
data = open("/home/emilyblack/compresser/in.txt").read()
data = list(data)
for i in range(len(data)):
    data[i] = '0'*(8-len(bin(ord(data[i]))[2:]))+bin(ord(data[i]))[2:]
data = ''.join(data)

key_lens = []
for i in range(1,len(data)/2):
    if len(data)%i == 0:
        key_lens.append((find_filesize(i),i,))
sec_l = min(key_lens)[1]
data = findall('[01]{'+str(sec_l)+'}',data)
find_filesize(sec_l)
c = {}
for i in range(len(counter.keys())):
    c[bin(i)[2:]] = counter.keys()[i]
