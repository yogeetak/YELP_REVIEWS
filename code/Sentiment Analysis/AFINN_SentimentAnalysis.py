##Sentiment Analysis of reviews text - Using AFINN Dictionary of positive and negative words
##Sentiment Analysis of reviews text - Using Valder Sentiment Analyzer of NLTK library

import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk.tokenize import sent_tokenize
import math
import re
import string

affin={}
header_row=['business_id','username','user_id','review_id','review_text','review_date','total_words','review_rating','cal_affin_rating',
            'cal_valder_rating','affin_word_score','cal_valder_compound','cal_valder_pos','cal_valder_neg','cal_valder_neu',"need_inspection",'no_of_text_chars']

filenameAFINN="/Users/apple/Desktop/YELP_REVIEWS/code/Sentiment Analysis/opinion-lexicon-English/AFINN-111.txt"
add_filename="/Users/apple/Desktop/YELP_REVIEWS/code/Sentiment Analysis/opinion-lexicon-English/additional_words.txt"
def main():
    afinnfile = open(filenameAFINN,'r',encoding='ISO-8859-1')
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        affin[term] = int(score)  # Convert the score to an integer.

    ##adding addtional terms to afinn_dict
    add_file = open(add_filename,'r',encoding='ISO-8859-1')
    scores = {} # initialize an empty dictionary
    for line in add_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        affin[term] = int(score)  # Convert the score to an integer.
  

    ##Reading from scrapped reviews, for each business id collecting all possible Review_text
    sid = SentimentIntensityAnalyzer()
    with open('/Users/apple/Desktop/YELP_REVIEWS/code/data/ready_data/elgin/elgin_reviews_part13.csv', 'r',encoding='ISO-8859-1',newline='') as csvreaderfile:
        reader = csv.DictReader(csvreaderfile)
        with open('elgin_reviews_part13_dict_sentiment_Data.csv', 'w',encoding='ISO-8859-1',newline='') as csvwriterfile:
            writer = csv.writer(csvwriterfile, dialect='excel')
            writer.writerow(header_row)
        
            for row in reader:
                affin_word_score=0
                pos_score=0.0
                neg_score=0.0
                neu_score=0.0
                compound_score=0.0
                review_rating=row['star_rating']
                total_no_of_text_chars = len(row['review_text'])
                business_id=row['business_id']
                need_inspection="No"
                ##Processing the text for affin analysis
                affin_processed_review_text=affin_text_processing(row['review_text'])

                ##Processing the text for valder sent analysis
                senti_processed_review_text=senti_text_processing(row['review_text'])

                ##Calculating Valder Sentiment Scores
                lines_list = sent_tokenize(senti_processed_review_text)
               
                for sentence in lines_list:
                    ss = sid.polarity_scores(sentence)
                    pos_score=pos_score + ss['pos']
                    neg_score=neg_score + ss['neg']
                    neu_score=neu_score + ss['neu']
                    compound_score=compound_score + ss['compound']

                ##Ceiling compound score
                valder_senti_score=math.ceil(compound_score)
                if(valder_senti_score > 5):
                    valder_senti_score=5
    
                ##Calculating affin scores:
                for word in affin_processed_review_text.split(' '):
                    if(word in affin.keys()):
                        affin_word_score=affin_word_score + affin[word]
                    else:
                        synonyms = wordnet.synsets(word)
                        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
                        for syn_word in lemmas:
                            if(syn_word in affin.keys()):
                                affin_word_score=affin_word_score + affin[syn_word]
                        

                if(affin_word_score <= 10):                                     ## IF affin_word_score < 10 (negative, low rating) then rating=1
                    cal_sentiment_score= 1
                    
                elif(affin_word_score > 10 and affin_word_score <=50 ):         ## IF affin_word_score [10,50] range then rating=2
                    cal_sentiment_score= 2
                    
                elif(affin_word_score > 50 and affin_word_score <= 100 ):       ## IF affin_word_score [50,100] range then rating=3
                    cal_sentiment_score= 3
                    
                elif(affin_word_score > 100 and affin_word_score <= 130):       ## IF affin_word_score [100,130] range then rating=4
                    cal_sentiment_score= 4
                    
                elif(affin_word_score > 130):                                   ## IF affin_word_score > 130 range then rating=5
                    cal_sentiment_score= 5
                               

                total_words=len(affin_processed_review_text.split(' '))

                if((abs(float(review_rating) - valder_senti_score) > 3) and (abs(float(review_rating) - cal_sentiment_score) > 3)):
                    need_inspection="YES"
 
                
                temp_row=[business_id,row['username'],row['user_id'],row['review_id'],row['review_text'],row['review_date'],total_words,review_rating,cal_sentiment_score,
                          valder_senti_score,affin_word_score,compound_score,pos_score,neg_score,neu_score,need_inspection,total_no_of_text_chars]
                writer.writerow(temp_row);
            
def affin_text_processing(text):
    words=[]
    text=text.strip().lower()
    if("&#34;" in  text):
        text=text.replace("&#34;","'")
    if("&#39;" in  text):
        text=text.replace("&#39;","'")
    if("&amp;" in  text):
        text=text.replace("&amp;","&")
        
    text = re.sub("\d", '', text)                  #remove digits
    text = re.sub(r'\-', ' ', text)                #replace - with white space
    text = re.sub(r'\'m', ' am', text)             #replace apostrophe m ('m) with am
    text = re.sub(r'\'d', ' would', text)          #replace apostrophe d ('d) with would
    text = re.sub(r'\'re', ' are', text)           #replace apostrophe re ('re) with are
    text = re.sub(r'n\'t', ' not', text)           #replace apostrophe t ('nt) with not
    text = re.sub(r'\'ll', ' will', text)          #replace apostrophe ll ('ll) with will
    text = re.sub(r'\&', 'and', text)              #replace & with and
    text = re.sub(r'\'s', ' ', text)               #replacing any apostrphe ('s) with empty space

    ##Stop Words removal
    stop_words=set(stopwords.words('english'))
    token_words=word_tokenize(text)
    filtered_review=[w for w in token_words if not w in stop_words]
    for word in filtered_review:
        words.append(word)
    text = ' '.join(words)
    return text
    
def senti_text_processing(text):
    words=[]
    text=text.strip().lower()
    if("&#34;" in  text):
        text=text.replace("&#34;","'")
    if("&#39;" in  text):
        text=text.replace("&#39;","'")
    if("&amp;" in  text):
        text=text.replace("&amp;","&")
    return text

    
if __name__ == '__main__':
    main()
    
