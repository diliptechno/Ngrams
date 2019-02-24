# Ngrams 
# Random sentence generations from N-grams using probabilty.
Natural Language processing
team - Evil Geniuses 
Professor - Ozlem Uzuner

Given a text file and the and the size of the N-grams (n = 1, 2, 3....) the program will generate the Random sentences by combining the various tokens from the trained data.

Data- the training data for his project is taken from the Brown Corpora to train the model. Some of the .txt files from this corpora are also provided. 

Initially, the data is converted into tokens and the data is trained depending on various factors like the starting of the sentences. And then the ngrams are formed depending on the input given by the user. These N-grams are then used to generate random sentences. The randomness of the sentences generated depends on the trained model. The frequency distribution is used to find the frequency and the probability of every N-gram is calculated. 

The end of the sentences is also random and the generation of the sentence stops when a particular sentences end tokens like ./,/ !/? etc. 

We can clearly see that the meaningfulness of the sentence increases with N in the N-grams. 
