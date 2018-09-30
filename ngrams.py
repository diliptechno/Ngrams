import sys
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from random import random
import numpy as np
import re

print("This program generates random sentences based on an Ngram model.")
for x in range(len(sys.argv[1:])):
    if(x==0):
        print("Ngrams= "+sys.argv[1])
        ngrams = int(sys.argv[1])
    elif(x==1):
        print("Number of sentences= "+sys.argv[2])
        sentences = sys.argv[2]
    else:
        print("File no."+ str(x-1)+"= "+ sys.argv[x+1])
#reading all the files and extracting tokens
txt_data=""
for y in range(2,len(sys.argv[1:])):
    with open(sys.argv[y+1],encoding="latin-1") as f_open:
        txt_data= txt_data + (f_open.read().lower())
# adding space for (-, ' , _)
text= re.sub(r'(-|\'|_|\.|\/|\*)', r' \1 ',txt_data)
#stored the tokenized words
tokens=[]
tokens = (word_tokenize(text))
#print(len(tokens))
#print(len(set(tokens)))
#fdist has the frequencies of the tokens
fdist = FreqDist(tokens)

# list for end tokens
end = ['.','!','?']
start = []
count =0
for word in tokens:
    if(word=="." or word=="!" or word=="?"):
        if(count== len(tokens)-1):
            break
        start.append(tokens[count+1])
    count+= 1
start = set(start)

#remove end tokens from start
t_start=[]
for word in start:
    if word in end:
        continue
    t_start.append(word)
start = t_start

#add start to freqdist
count = 0
for key,value in fdist.items():
    for word in start:
        if(key==word):
            count= count+ value
#print(count)
fdist["<start>"] = count

#add end to freqdist
count = 0
for key,value in fdist.items():
    for word in end:
        if(key==word):
            count= count+ value
#print(count)
fdist["<end>"] = count

#remove start and end tokens
fdist2 = {}
for key, value in fdist.items():
    if key in end: continue
    elif key in start: continue
    fdist2[key] = value

#create probability distribution

probdist={}
for key,value in fdist2.items():
    probdist[key]=value/len(tokens)

#probdist 

# create normal prob dist

# normprobdist={}
# sum=0
# for key,value in probdist.items():
#     sum=sum+value
# for key,value in probdist.items():
#     normprobdist[key]= value/sum
#normprobdist    

#create interval prob dist

# lineprobdist={}
# sum=0
# for key,value in probdist.items():
#     sum=sum+value
#     lineprobdist[key]=sum
#
# #1gram model
# for x in range(int(sentences)):
#     start_c=1
#     end_c=0
#     line="Sentence "+str(x+1)+" :"
#     while(end_c==0):
#         rand = random()
#         if(start_c==1):
#             line= line+" "+np.random.choice(list(start))
#             start_c=0
#         for key,value in lineprobdist.items():
#             if(rand<value):
#                 if(key=="<start>"):
#                     key = np.random.choice(list(start))
#                 elif(key=="<end>"):
#                     key = np.random.choice(list(end))
#                     end_c=1
#                 line=line+" "+key
#                 break
#
#     print(line)

#tokens for trigram n=4

gram = []
n = ngrams
for i in range(0, len( tokens)-(n-2)):
    x = ""
    for j in range(0, n-1):
        if(j==n-2):
            x+= tokens[i+j]
        else:
            x+=  tokens[i+j]+ " "
    gram.append(x)
    i=i+1

freq_dist_Ngram = FreqDist(gram)
# print(freq_dist_Ngram)

#for claculating the probalities






