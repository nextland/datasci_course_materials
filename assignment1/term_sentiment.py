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
           word = word.lower()
           word = word.encode("utf-8") 
           if word in scores:
                sentiments[j] +=scores[word]
        j+=1

    j = 0
    non = {}
    for line in texts:
        for word in line.split():
            word = word.lower()
            if word not in scores:
                if re.match(r'\A[\w-]+\Z', word):
                    if word not in non:
                        non.setdefault(word, [])
                        non[word].append(0)
                        non[word].append(0)
                        non[word].append(0)
                    if sentiments[j] > 0:
                        non[word][0] += 1
                    if sentiments[j] < 0:
                        non[word][1] += 1
                    non[word][2] += 1
        j+=1

    for key, values in non.items():
        pos = values[0]
        neg = values[1]
        suma = values[2]

        try:
            if neg==0:
                scores[key] = (float(pos)/suma)
            else:
                scores[key] = (float(pos)/suma)/(float(neg)/suma)
            if scores[key] < 1:
                print "{} {}".format(key, scores[key])
        except ZeroDivisionError:
            print key, values                
        

if __name__ == '__main__':
    main()
