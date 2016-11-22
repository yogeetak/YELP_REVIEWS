##Sentiment Analysis of reviews text - Using Bing Lus Dictionary of positive and negative words
##http://www.slideshare.net/mcjenkins/how-sentiment-analysis-works?next_slideshow=1
##NLTK sentiment analysizer package
##http://stackoverflow.com/questions/32879532/stanford-nlp-for-python
import csv
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import re
import string

header_row=['business_id','total_words','review_rating','affin_word_score','cal_sentiment_rating','final_review_text']
def main():
    
    ##Reading from scrapped reviews, for each business id collecting all possible Review_text
    sid = SentimentIntensityAnalyzer()
    with open('chicago_reviews_part1.csv', 'r',encoding='ISO-8859-1',newline='') as csvreaderfile:
        reader = csv.DictReader(csvreaderfile)
        with open('chicago_reviews_part1_dictsentiment_Data.csv', 'w',encoding='ISO-8859-1',newline='') as csvwriterfile:
            writer = csv.writer(csvwriterfile, dialect='excel')
            writer.writerow(header_row)
            
            i=0
            for row in reader:

                review_rating=row['star_rating']
                business_id=row['business_id']
                ##Processing the text
                processed_review_text=text_processing(row['review_text'])

                lines_list = sent_tokenize(processed_review_text)
                for sentence in lines_list:
                    print(sentence)
                    ss = sid.polarity_scores(sentence)
                    for k in sorted(ss):
                        print('{0}: {1}, '.format(k, ss[k]), end='')
                        print()
            

                
                ##temp_row=[business_id,total_words,review_rating,word_score,cal_sentiment_score,row['review_text']]
                ##writer.writerow(temp_row);
            
def text_processing(text):
    words=[]
    text=text.strip().lower()                      #remove trailing spaces
    text = re.sub("\d", '', text)                  #remove digits
    text = re.sub(r'\-', ' ', text)                #replace - with white space
    text = re.sub(r'\'m', ' am', text)             #replace apostrophe m ('m) with am
    text = re.sub(r'\'d', ' would', text)          #replace apostrophe d ('d) with would
    text = re.sub(r'\'re', ' are', text)           #replace apostrophe re ('re) with are
    text = re.sub(r'n\'t', ' not', text)           #replace apostrophe t ('nt) with not
    text = re.sub(r'\'ll', ' will', text)          #replace apostrophe ll ('ll) with will
    text = re.sub(r'\&', 'and', text)              #replace & with and
    text = re.sub(r'didnt ', 'did not', text)      #replace didnt  with did not
    text = re.sub(r'dont', 'do not', text)         #replace dont with do not
    text = re.sub(r'wont', 'will not', text)       #replace wont with will not
    text = re.sub(r'cant', 'can not', text)        #replace cant with can not 
    text = re.sub(r'wouldnt', 'would not', text)   #replace wouldnt with would not
    text = re.sub(r'couldnt', 'could not', text)   #replace couldnt with could not
    text = re.sub(r'isnt', 'is not', text)         #replace isnt with is not
    text = re.sub(r'wasnt', 'was not', text)       #replace wasnt with was not
    text = re.sub(r'\'s', ' ', text)               #replacing any apostrphe ('s) with empty space


     ##Stop Words,Punctuation and Stemming
    stop_words=set(stopwords.words('english'))
    PUNCTUATION = set(string.punctuation)
    token_words=word_tokenize(text)
    filtered_review=[w for w in token_words if not w in stop_words]
    for word in filtered_review:
        punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])  
        words.append(str(punct_removed))
    text = ' '.join(words)
    return text
    


if __name__ == '__main__':
    main()
    
