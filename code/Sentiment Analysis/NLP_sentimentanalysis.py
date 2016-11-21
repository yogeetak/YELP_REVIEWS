##Sentiment Analysis of reviews text - Using Bing Lus Dictionary of positive and negative words
##http://www.slideshare.net/mcjenkins/how-sentiment-analysis-works?next_slideshow=1
##NLTK sentiment analysizer package

import csv
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from pycorenlp import StanfordCoreNLP
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import string

pos_words={}
neg_words={}
final_list=[]
def main():
    nlp = StanfordCoreNLP('http://corenlp.run/')
##    ####Creating a dictionary with all positive & negativewords
##    text_file= open('/Users/apple/Desktop/YELP_REVIEWS/code/Sentiment Analysis/opinion-lexicon-English/positive-words.txt', 'r',encoding='utf8',newline='')
##    pos_words=text_file.readlines()
##    text_file.close()
##
##    text_file_1= open('/Users/apple/Desktop/YELP_REVIEWS/code/Sentiment Analysis/opinion-lexicon-English/negative-words.txt', 'r',encoding='ISO-8859-1',newline='')
##    neg_words=text_file_1.readlines()
##    text_file_1.close()


    ##Reading from scrapped reviews, for each business id collecting all possible Review_text
    with open('CHICAGO_part2.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
        reader = csv.DictReader(csvreaderfile)
        i=0
        for row in reader:
            cal_sentiment='undefined'
            pos_word_count=0
            neg_word_count=0
            i=i+1
            review_rating=row['star_rating']
            business_id=row['business_id']
            ##Processing the text
            processed_review_text=text_processing(row['review_text'])
            token_sentence=sent_tokenize(processed_review_text)
            for sent in token_sentence:
                res = nlp.annotate(processed_review_text,
                                   properties={'annotators': 'sentiment','outputFormat': 'json'}
                                   )
               
            print("&&&&&&&&&&&&&&&&&&&")
            print()
            for s in res["sentences"]:
                print ("%d: '%s': %s %s" % (s["index"], " ".join([t["word"] for t in s["tokens"]]), s["sentimentValue"], s["sentiment"]))
            print()

            
    
            ##calculating scores:
##            for word in processed_review_text.split(''):
##                if(word in pos_words):
##                    pos_word_count=pos_word_count+1
##                    continue
##                if(word in new_words):
##                    neg_word_count=neg_word_count+1
##                    continue
##                
##            if(pos_word_count > neg_word_count):
##                cal_sentiment='positive'
##            elif(pos_word_count < neg_word_count):
##                cal_sentiment='negative'
##            elif(pos_word_count == neg_word_count):
##                 cal_sentiment='neutral'
                
            
##            final_list.append(business_id+" ,##, "+ review_rating +" ,##, "+ processed_review_text + ",##,"+cal_sentiment)
    

def text_processing(text):
    words=[]
    text=text.strip().lower()                      #remove trailing spaces
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
    text = re.sub(r'didnt ', 'did not', text)      #replace didnt  with did not
    text = re.sub(r'dont', 'do not', text)         #replace dont with do not
    text = re.sub(r'wont', 'will not', text)       #replace wont with will not
    text = re.sub(r'cant', 'can not', text)        #replace cant with can not 
    text = re.sub(r'wouldnt', 'would not', text)   #replace wouldnt with would not
    text = re.sub(r'couldnt', 'could not', text)   #replace couldnt with could not
    text = re.sub(r'isnt', 'is not', text)         #replace isnt with is not
    text = re.sub(r'wasnt', 'was not', text)       #replace wasnt with was not
    text = re.sub(r'\'s', ' ', text)               #replacing any apostrphe ('s) with empty space



##     ##Stop Words,Punctuation and Stemming
##    stop_words=set(stopwords.words('english'))
##    PUNCTUATION = set(string.punctuation)
##    stemmer = SnowballStemmer('english')
##    
##    token_words=word_tokenize(text)
##    filtered_review=[w for w in token_words if not w in stop_words]
##    for word in filtered_review:
##        punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])  
##        stemmedWord = stemmer.stem(punct_removed)
##        words.append(str(stemmedWord))
##    text = ' '.join(words)
    return text
    


if __name__ == '__main__':
    main()
##    for i in final_list:
##        print(i)
##        print()
##    
##with open('testcase1_ChicagoPart1_ReviewText_Data.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
##        writer = csv.writer(csvwriterfile, dialect='excel')
##        writer.writerow(header_row)
##
##        for bid in final_dict:
##            if(bid in business_url_info): business_url=business_url_info[bid]   ##If Valid URL exists, then proceed
##            else: continue
##
##            review_rating=0.0
##            actual_review_text=''
##            final_review_text=''
##
##            review_list=final_dict[bid]
##            if(len(review_list) > 10):
##                sample_review_list=random.sample(review_list,10)  ##Taking a random sample of 10 reviews from each business id
##            else:
##                sample_review_list=random.sample(review_list,len(review_list)) 
##
##            for text in sample_review_list:
##                review_rating = review_rating + float(text.split(',##,')[0])  ##Adding the ratings for all 10 reviews
##                actual_review_text=text.split(',##,')[1]
##
##                if("." in actual_review_text):
##                    split_review_text=actual_review_text.split('.')   ##Splitting the text with fulllstops and taking a random index of the sentence
##                    randno=randrange(0,len(split_review_text))
##                    selected_sent=split_review_text[randno]
##                    if(selected_sent == ''):
##                        randno=randrange(0,len(split_review_text))
##                        selected_sent=split_review_text[randno]
##                    final_review_text=final_review_text.strip()+"."+selected_sent.lstrip()[0:].capitalize()
##                elif(len(actual_review_text) <= 500):
##                    final_review_text=final_review_text+actual_review_text.lstrip()[0:].capitalize()+"."
##            
##            if(final_review_text==''):
##                continue
##
##            final_review_rating=int(round(review_rating/10)) ##Rounding to nearest integer
##    
##            final_review_text=final_review_text.lstrip('.')+"."
##            final_review_text=final_review_text.lstrip()[0:].capitalize()
##            temp_row=[bid,business_url,final_review_rating,final_review_text]
##            writer.writerow(temp_row);
