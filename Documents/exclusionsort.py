# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:45:49 2022

@author: Marsarthim
"""
import random as r
from copy import deepcopy

#check if list is sorted
def check(mylist):
    for i in range(len(mylist)):
        if i<len(mylist)-1 and mylist[i]>mylist[i+1]:
            return False
    return True

#exclusion sorting algorithm
def exclusion(mylist):
    if mylist==unsorted:    #first pass initialise
        # print("PASS1 ",end='')
        # print(mylist)
        # print("PASS2 ",end='')
        # print(unsorted)
        global count
        count = 0
        global store
        global choose
        choose = 99
        store = []
        
        
        
    #print("hi i bring ",end='')
    #print(store)
    #print(mylist)
    
    try:
        if not check(mylist):   #if not sorted,
            
            count+=1
            #check if trivial
            if len(mylist)==2:
                #print("SORTED, SWAP")
                mylist = [mylist[1],mylist[0]]
                print(*mylist,end='|')
                print(*[x[0] for x in store])
                return exclusion(mylist)
            
            #remove
            
            pindex = r.randrange(0,len(mylist))
            
            while pindex==choose:               #make sure not choosing the same position
                pindex = r.randrange(0,len(mylist))
            
            choose = pindex
            
            pivot = mylist[pindex]
            store.append([pivot,pindex])
            mylist.remove(pivot)
            
            #recurse
            #print("GOING DEEPER WITH "+str(store[-1][0]))
            
            print(*mylist,end='|')
            print(*[x[0] for x in store])
            return exclusion(mylist)
            
            
        else:   #list is sorted
            if len(store)==0:   #if none in storage, return
                print("Sorted!")
                return mylist
            else:               #add pivot back, and return
                
                #read position of most recent pivot and put er back in
                prevpivot = store[-1]
                store.pop(-1)
                #print(store[-1])
                #print(mylist)
                
                if len(mylist)<=prevpivot[1]:
                    mylist.append(prevpivot[0])
                else:
                    mylist.insert(prevpivot[1],prevpivot[0])
                    
                #print("GOING UP, ADDING BACK " + str(prevpivot[0]))
                count+=1
                print(*mylist,end='|')
                print(*[x[0] for x in store])
                return exclusion(mylist)
    except:
        print("We've gone too deep cap'n!!! This is all I could salvage")
        for i in range(len(store)):
            prevpivot = store[-1]
            store.pop(-1)
            #print(store[-1])
            #print(mylist)
            
            if len(mylist)<=prevpivot[1]:
                mylist.append(prevpivot[0])
            else:
                mylist.insert(prevpivot[1],prevpivot[0])
        return mylist

#print(check([1,2,3,4,3]))


n = int(input("n = ...?\n"))
unsorted = []

for i in range(n):
    unsorted.append(i+1)
    print(i+1,end=' ')
    
print("\nShuffling...")
r.shuffle(unsorted)
print(*unsorted)

print("Sorting...")

print(*exclusion(deepcopy(unsorted)))
print("Steps: "+str(count))

d = input("done")
