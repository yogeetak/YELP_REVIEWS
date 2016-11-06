##TEST CASE 10 - REVIEW DATA PREP
##natural reviews
##Pick reviews from businesses of same categories or chains and report them to other businesses
##Pick random 10 samples or lesser if the business has lesser number of reviews 
####Splitting the text of each review with fulllstops and a random index of the sentence between (0,#of split sentences)
##prepare final reivew with average star rating
##OUTPUT: CSV Document for test case 10

import csv
import random
from random import randrange

business_url_info={} ##Dictionary of Business Names and URL's
final_dict={}
business_similar_categories={}
header_row=['business_id','business_url','review_rating','formed_review_text']

##Creating a dictionary with all same categories of Business ID and URLS
with open('/Users/apple/Desktop/YELP_REVIEWS/SearchAPI results/chicago_chinese_categories.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        business_similar_categories[row['business_id']]=row['business_url']


##Reading from scrapped reviews, for each business id collecting all possible (Rating ,##, Review_text)
with open('//Users//apple//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
    reader = csv.DictReader(csvreaderfile)
    
    for row in reader:
        if(row['business_id'] not in business_similar_categories):
            continue
        
        if(row['elite_status'] == '0'):  ##considering reviews of only elite users
            continue
        if(row['business_id'] not in final_dict):
            final_dict[row['business_id']] = [row['star_rating']+" ,##, "+row['review_text']]
        else:
            original_list = final_dict.get(row['business_id'])
            original_list.append(row['star_rating']+" ,##,  "+row['review_text'])
            final_dict[row['business_id']] = original_list
 
with open('testcase10_ChicagoPart1_ReviewText_Data.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
        writer = csv.writer(csvwriterfile, dialect='excel')
        writer.writerow(header_row)

        for text in final_dict:
            print(text)
            print(final_dict[text])
            print()
##            review_rating = review_rating + float(text.split(',##,')[0])  ##Adding the ratings for all 10 reviews
##            actual_review_text=text.split(',##,')[1]
##            if("." in actual_review_text):
##                split_review_text=actual_review_text.split('.')   ##Splitting the text with fulllstops and taking a random index of the sentence
##                randno=randrange(0,len(split_review_text))
##                final_review_text=final_review_text.strip()+"."+split_review_text[randno].lstrip()[0:].capitalize()
##                elif(len(actual_review_text) <= 500):
##                    final_review_text=actual_review_text.lstrip()[0:].capitalize()+"."
##            if(final_review_text==''):
##                continue
##
##            final_review_rating=int(round(review_rating/10)) ##Rounding to nearest integer
##    
##            final_review_text=final_review_text.lstrip('.')+"."
##            final_review_text=final_review_text.lstrip()[0:].capitalize()
##            temp_row=[bid,business_url,final_review_rating,final_review_text]
##            writer.writerow(temp_row);
