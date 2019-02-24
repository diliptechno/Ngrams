import fileinput
import nltk
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print (a)
print (b)
data = []
for line in fileinput.input(sys.argv[3:]):
    data.append(line)
# print (data)
h=""
for d in data:
    h+= d
# a = h.strip('\n')
#print(h)
#
# print (type (h))
tokens = nltk.word_tokenize(h)
print(tokens)
