from nltk.corpus import words
import re
import random

print(type(words))
wordlist=words.words()

while True:
    random.shuffle(wordlist)
    num = int(input("Number:\n"))
    cutwords = [x for x in wordlist if len(x)==num]
    
    regex = re.compile(input("Regular expression:\n").lower())
    cutwords = [x for x in cutwords if regex.match(x)!=None]

    n=0
    while (n<len(cutwords) and n<25):
        print(cutwords[n])
        n+=1
    print("\n\n\n")
