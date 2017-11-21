import markovify
import subprocess
from random import *
import random


prefixFile="prefix"
suffixFile="suffix"

def getTitlePart(afile):
    lines = open(afile).read().splitlines()
    myline =random.choice(lines)
    return myline
    # titleCount=title.count("")
    # #print titleCount
    # synopsCountMax=eval("280 - titleCount")

def getContent(synopsCountMax):
# Get raw text as string.
    with open("whosynopsbig.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)
    #for i in range(1):
    synops=(text_model.make_sentence())
    #print synops
    #synops=""
    synopsCount=synops.count("")
    # print "1"
    # print synops
    # print synopsCount
    # print ".."
    #print synopsCount
    remaining=eval("synopsCountMax - synopsCount")
    #for i in range(1):
    #short=(text_model.make_short_sentence(remaining))
    while eval("synopsCount > synopsCountMax"):
    	print "too long, shortening"
        synops=(text_model.make_sentence())
        synopsCount=synops.count("")
     #    print synopsCount
        # print synops

    remaining=eval("synopsCountMax - synopsCount")
    #print remaining
    while eval("synopsCount < synopsCountMax"):
        #for i in range(1):
        #print "short"
        short=(text_model.make_short_sentence(remaining))
        #print short
        if short:
            synops+=str(" " + short)
            #synopsCount=synops.count("")
            synopsCount=eval("synopsCountMax + 1")
        else:
            synopsCount=eval("synopsCountMax + 1")
        

    #print title
    #print "--------------"
    return synops
    #print short
    #print
    #return 


def getTitle():
    rando=randint(1,4)
    if rando > 2:
        #suffix=getTitlePart(prefixFile)
        prefix=getTitlePart(suffixFile).lower()
        #print "flip"
    else:
        prefix=getTitlePart(prefixFile).lower()

    suffix=getTitlePart(suffixFile).lower()
    

    

    rando2=randint(1,5)
    if rando2 > 2:
        ofThe=" of the "
    elif rando2 > 5:
        ofThe=" of "
    else:
        ofThe=""

    if suffix.startswith("of ") or  suffix.startswith("in ") or  suffix.startswith("a ") or  suffix.startswith("to ") or  suffix.startswith("on ") or  suffix.startswith("for ") or  suffix.startswith("and ") or  suffix.startswith("at "):
        ofThe=""
    if suffix.startswith("the "):
        ofThe="of "

    if prefix.startswith("of ") or  prefix.startswith("and ") or  prefix.startswith("in ")  or  prefix.startswith("a ") :
        #prefix=prefix.replace("of ", "The ")
        prefix.partition(' ')[2]

    title=("the " + prefix + " " + ofThe + " " + suffix)#.title()
    title = (title.replace("the of ", "the "))
    title = (title.replace("the the ", "the "))
    title = (title.replace("the the ", "the "))
    title = (title.replace("  ", " "))
    title = (title.replace("  ", " "))
    return title

storyTitle=getTitle().title()
titleCount=storyTitle.count("")
synopsCountMax=eval("280 - titleCount")
#print synopsCountMax
storyContent=getContent(synopsCountMax)
print storyTitle
print ""
print storyContent