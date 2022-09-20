from nltk.corpus import words
import re
import random

def Contains(test_str,string):
    for c in test_str:
        if c not in string:
            return False
    return True

wordlist = dict.fromkeys([x.lower() for x in words.words()])
n=0
print(len(wordlist))
for x in wordlist:
    if (
        #length
        len(x)==5 and
        #pattern
        re.search("a..i.",x)!=None and
        #does not contain
        re.search("[nsetc]",x)==None and
        #does contain
        Contains("a",x)

        and not Contains("i",x[2])
        ):
        print(x)
        n+=1
print(n)
penis=input()
