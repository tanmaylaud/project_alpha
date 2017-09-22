from libs import other_analysis
from libs import corpus
from libs import sentence_comparison as sc
from libs import get_relevant_tweets_local as tweets_db

def analyze(query):
    keywords = corpus.remove_stopwords(query)
    print keywords
    tweets = tweets_db.find_all(keywords)
    values = []
    for tweet in tweets:
        values.append(sc.my_sentence_similarity(query, tweet))
        print values
    mean_value = mean(values)
    percentage = mean_value * 100 # Some processing
    return percentage
    #return other_analysis.analyze(query, percentage)

def mean(values):
    users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]
    avg = [80, 50, 75, 40, 70, 80, 20, 10]
    sum = 0
    count = 0
    denom = 0
    for x in values:
        sum += (x + 0.1) * avg[count]
        denom += avg[count]
        count += 1
    if count == 0:
        return 0
    return float(sum)/denom

'''
def match_sentences(query, tweets):
    values = []
    for tweet in tweets:
        values.append(sentence_comparison(query, tweet))
    return values
'''
