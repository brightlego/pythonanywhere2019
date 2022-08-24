import re
import matplotlib.pyplot as plt
import numpy as np

input_text = open("/home/emilyblack/john_misc/word_counter/input_text.txt","r").read().lower()


input_text = re.findall("[a-z]+",input_text)

word_list = []
word_count = []

for i in input_text:
	if i not in word_list:
		word_list.append(i)
		word_count.append(1.0)
	else:
		word_count[word_list.index(i)] += 1

words = zip(word_count,word_list)

words.sort()
#words.reverse()

for i in words:
	t = ""
	for j in range(5-(len(i[1])/7)):
		t += "\t"
	print i[1] + ":"+t, int(i[0])
word_count.sort(reverse = True)
plt.clf()
plt.plot(np.log((np.array(word_count))))
plt.savefig("/home/emilyblack/john_misc/word_counter/tmp.png")

'''for i in word_count:
    if i == 1:
        del i'''
normal_word = []
previous_num = len(word_count)
for i in word_count:
    if previous_num - i > 10:
        normal_word.append(1)
        previous_num = i
    else:
        normal_word[len(normal_word)-1] += 1
print normal_word
plt.clf()
plt.plot(normal_word)
plt.savefig("/home/emilyblack/john_misc/word_counter/tmp_log.png")