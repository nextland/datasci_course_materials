import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #scores = {} # initialize an empty dictionary
    #for line in sent_file:
    #  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    #  scores[term] = int(score)  # Convert the score to an integer.

    data = []

    for line in tweet_file:
        data.append(json.loads(line))

    terms ={}

    entities = []
    for term in data:
        items = dict(term.items())
        entities.append(items.get('entities',""))

    hashtags = []
    for entity in entities:
        if isinstance(entity, dict):
            items = dict(entity.items())
            if items['hashtags']:
                hashtags.append(items['hashtags'])

    texts = []
    for values in hashtags:
        for value in values:
            if isinstance(value, dict):
                items = dict(value.items())
                texts.append(items['text'])

    values = {}
    for value in texts:
        if value in values:
            values[value] +=1
        else:
            values[value] = 1
    i = 0
    for w in sorted(values, key=values.get, reverse=True):
        if i < 10:
           print "{} {}".format(w.encode("utf-8"), values[w])
        i+=1   

if __name__ == '__main__':
    main()
