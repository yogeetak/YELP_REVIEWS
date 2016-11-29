##Sentiment Analysis of reviews text - Using Bing Lus Dictionary of positive and negative words
##http://www.slideshare.net/mcjenkins/how-sentiment-analysis-works?next_slideshow=1
##NLTK sentiment analysizer package

import csv
from pycorenlp import StanfordCoreNLP
header_row=['business_id','username','user_id','review_id','review_text','star_rating',
            'calculated_senti_rating','total_senences','very_posivite_counts','posivite_counts','neutral_counts','very_negative_counts','negative_counts','nlp_sentences']

def main():
    nlp = StanfordCoreNLP('http://localhost:9000')
    ##Reading from scrapped reviews, for each business id collecting all possible Review_text
    with open('chicago_reviews_part1.csv', 'r',encoding='ISO-8859-1',newline='') as csvreaderfile:
        reader = csv.DictReader(csvreaderfile)

        with open('chicago_reviews_part1_sentiments.csv', 'w',encoding='ISO-8859-1',newline='') as csvwriterfile:
            writer = csv.writer(csvwriterfile, dialect='excel')
            writer.writerow(header_row)
            
            for row in reader:
               
                pos_word_count=0
                total_pos_word_count=0
                total_neg_word_count=0
                very_pos_word_count=0
                neg_word_count=0
                very_neg_word_count=0
                neutral_count=0
                total_sentences=0
                calculated_sentiment_rating=0
                nlp_sentences = ' '
                
                review_rating=row['star_rating']
                business_id=row['business_id']

                ##Processing the text
                processed_review_text=text_processing(row['review_text'])

                res = nlp.annotate(processed_review_text,
                                       properties={'annotators': 'sentiment','outputFormat': 'json'}
                                       )
                try:
                        
                    for s in res["sentences"]:
                        ##print ("%d: '%s': %s %s" % (s["index"], " ".join([t["word"] for t in s["tokens"]]), s["sentimentValue"], s["sentiment"]))

                        tempstr=" ".join([t["word"] for t in s["tokens"]])+" : "+ s["sentiment"]
                        nlp_sentences=nlp_sentences+ '\n' +tempstr    
        
                        if(s["sentiment"] == 'Neutral'):
                            neutral_count=neutral_count+1
                            continue

                        total_sentences=total_sentences+1

                        if( s["sentiment"] == 'Verynegative'):
                            very_neg_word_count=very_neg_word_count+1
                            continue
                        elif(s["sentiment"] == 'Negative'):
                            neg_word_count=neg_word_count+1
                            continue
                        elif( s["sentiment"] == 'Verypositive'):
                            very_pos_word_count=very_pos_word_count+1
                            continue
                        elif(s["sentiment"] == 'Positive'):
                            pos_word_count=pos_word_count+1
                            continue
                except:
                    continue

                if(very_pos_word_count > 0):
                    total_pos_word_count=pos_word_count + (very_pos_word_count * 2) #very positive gets counted twice
                else:
                    total_pos_word_count=pos_word_count

                if(very_neg_word_count > 0):
                    total_neg_word_count=neg_word_count + (very_neg_word_count * 2)  #very negative gets counted twice
                else:
                    total_neg_word_count=neg_word_count

                ##total sentiment score calculation 
                if(very_pos_word_count > 1):     ##Highest Rating
                    calculated_sentiment_rating=5
                
                elif(very_neg_word_count > 1):  ##Lowest Rating
                    calculated_sentiment_rating=1
                
                elif(total_pos_word_count == total_neg_word_count): ##Neutral
                    calculated_sentiment_rating=3
            
                elif(total_pos_word_count > total_neg_word_count): ##Positive
                    calculated_sentiment_rating=4

                elif(total_pos_word_count < total_neg_word_count): ##Negative
                    calculated_sentiment_rating=2

                if( total_sentences > 0 and ((total_pos_word_count/total_sentences)  > (total_neg_word_count/total_sentences)) ): ##[Total=11, Neg=2, Pos=9] implies most postivie rating
                    calculated_sentiment_rating=5
                
                elif( total_sentences > 0 and ((total_pos_word_count/total_sentences) < (total_neg_word_count/total_sentences)) ): ##[Total=11, Neg=9, Pos=2] implies most negative rating
                    calculated_sentiment_rating=1

                temp_row=[business_id,row['username'],row['user_id'],row['review_id'],row['review_text'],review_rating,calculated_sentiment_rating,total_sentences,very_pos_word_count,pos_word_count,neutral_count,very_neg_word_count,neg_word_count,nlp_sentences]
                writer.writerow(temp_row)

 
def text_processing(text):
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
