
#
#
#

import random

words=[]

random.seed(13910328)

f = open('20k.txt','r')

for n in range(4096):
  words.append(f.readline().strip('\n'))

f.close()

o=open('scrambled_list.txt','w')

random.shuffle(words)

for w in words:
  o.write(w+'\n')


