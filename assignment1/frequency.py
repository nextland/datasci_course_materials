import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    data = []

    for line in tweet_file:
        data.append(json.loads(line))

    terms ={}

    texts = []
    for term in data:
        items = dict(term.items())
        if (items.get('lang',"") == "en"):
            texts.append(items.get('text',""))

    words = {}
    lenght = 0
    for line in texts:
        for word in line.split():
           if re.match(r'\A[\w-]+\Z', word):
               lenght += 1
               word = word.lower()
               word = word.encode("utf-8") 
               if word not in words:
                    words[word] = 1
               else:
                    words[word] += 1
            

    for word, value in words.items():
        frequency = float(value)/lenght
        print "{} {}".format(word, frequency)
        

if __name__ == '__main__':
    main()
