import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

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

    texts = {}
    add = False
    for term in data:
        items = dict(term.items())
        if items.get('text',"") and items.get('place',""):
            texttweet = items.get('text',"")
            for key, value in items.get('place',"").items():
                if key=="country_code" and value=="US":
                    if items['place'].get(key,""):
                        fullname = items['place'].get("full_name","")
                        ps=fullname.split()[-1]
                        if ps in states:
                            texts[ps]=texttweet

    sentiments = []
    result = {}
    j = 0;
    for state, line in texts.items():
        sentiments.insert(j,0)
        for word in line.split(): 
           if word not in scores:
                scores[word]=0
           sentiments[j] +=scores[word]
        if key not in result:
           result[state] = sentiments[j]
        else:
           result[state] += sentiments[j]
        j+=1
    print max(result, key=result.get)

if __name__ == '__main__':
    main()
