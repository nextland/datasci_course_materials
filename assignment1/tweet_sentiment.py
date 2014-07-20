import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    data = []

    for line in tweet_file:
        data.append(json.loads(line))

    terms ={}

    texts = []
    for term in data:
        items = dict(term.items())
        if  items.get('lang',"") == "en":
            texts.append(items.get('text',""))

    
    words = [i.split(',') for i in texts]
    sentiments = [] 

    j = 0;
    for line in texts:
        sentiments.insert(j,0)
        for word in line.split(): 
           if word not in scores:
                scores[word]=0
           sentiments[j] +=scores[word]
        if sentiments[j] < 6:
            print sentiments[j]
        j+=1

    #for sentiment in sentiments:
        #print sentiment

if __name__ == '__main__':
    main()
