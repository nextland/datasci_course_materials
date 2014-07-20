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
        texts.append(items.get('entities',""))
    print entities

if __name__ == '__main__':
    main()
