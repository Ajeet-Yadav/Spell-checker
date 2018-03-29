import json #json file kindda python dictionary structure


import difflib
#from difflib import SequenceMatcher
#SequenceMatcher(None,"rainn","rain").ration()
#output: 0.88888

from difflib import get_close_matches
#get_close_matches("rainn",["hello","Hi","rain"])
#get_close_matches("rainn",data.keys())  using default cutoff for word-matching
#output: ['rain','train','rainy']

data=json.load(open("data.json")) #Similar to file=open("file-name.txt",'r') nested in json.load()

def search(word):
    word=word.lower()    ##Converting into lower-case so that 'RAIN', 'RaIN', 'raiN' etc are converted into 'rain'
#    word=word[0].upper()+word[1:]
    if word.title() in data:  ####for exception such as Delhi, Paris etc
        return data[word.title()]

    word=word.lower()
    if word in data:  ##if 'rain' exist in 'data', dictionary's output either is true and false
        return data[word]

    elif word.upper() in data: ##for exception such as NATO, USA, etc
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys()))>0:
        print ("Did you mean '%s' instead? Enter 'Y' for Yes and 'N'for No: "%get_close_matches(word,data.keys())[0])
        Ans=input()
        if Ans=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif Ans=="N":
            print("Word doesn't exist please recheck it")
        else:
            print("We didn't understand your query ")
    else:
        print("Word doesn't exist please recheck it") ## "rainn" won't work here therefore, using external library difflib

word=input("Enter the word to find its meaning: ")
output=search(word)
if output!=None:
    for item in output:
        print(item)
