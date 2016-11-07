##TEST CASE 10 - REVIEW DATA PREP
##natural reviews - Pick reviews from businesses of same categories 
##Pick random 10 samples of businesses within same category
##For each business from the sample, pick a random review
##Splitting the text of the review with fulllstops and a selecting random sentence between (0,#of split sentences)
##Move to next business and iterate
##prepare final reivew with average star rating
##OUTPUT: CSV Document for test case 10

import csv
import random
from random import randrange

final_dict={}
business_similar_categories={}
header_row=['business_id','business_url','review_rating','formed_review_text']

##Creating a dictionary with same categories of Business ID and URLS
##with open('/Users/apple/Desktop/YELP_REVIEWS/SearchAPI results/chicago_chinese_categories.csv', 'r',encoding='utf8',newline='') as csvfile:
with open('C://Users/ykutta2//Desktop//YELP_REVIEWS//SearchAPI results//chicago_sandwiches_categories.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        business_similar_categories[row['business_id']]=row['business_url']


##Reading from scrapped reviews, for each business id collecting all possible (Rating ,##, Review_text)
##with open('//Users//apple//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
with open('C://Users//ykutta2//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
    reader = csv.DictReader(csvreaderfile)
    
    for row in reader:
        if(row['business_id'] not in business_similar_categories):
            continue
        
        if(row['business_id'] not in final_dict):
            final_dict[row['business_id']] = [row['star_rating']+" ,##, "+row['review_text']]
        else:
            original_list = final_dict.get(row['business_id'])
            original_list.append(row['star_rating']+" ,##,  "+row['review_text'])
            final_dict[row['business_id']] = original_list
 
with open('testcase10_chicago_sandwiches_categories_ChicagoPart1_ReviewText_Data.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
        writer = csv.writer(csvwriterfile, dialect='excel')
        writer.writerow(header_row)


        for bid_sim in business_similar_categories:
            random_sample=random.sample(list(final_dict.keys()),10) ##Selecting a random sameple of reviews from all businesses
            final_review_text=''
            actual_review_rating=0.0

            for bid in random_sample:

                if(bid_sim == bid):    ##Take reviews from other businesses, not same business
                    continue

                actual_review_text=''
                
                review_list=final_dict[bid]             ##Contains all reviews for one business
                randno=randrange(0,len(review_list))    ##Take one random review for each business
                review_text=review_list[randno]
               
                actual_review_rating = actual_review_rating + float(review_text.split(',##,')[0])  ##Adding the ratings for all reviews
                actual_review_text=review_text.split(',##,')[1]
                
                if("." in actual_review_text):
                    split_review_text=actual_review_text.split('.')         ##Splitting the text with fulllstops and taking a random index of the sentence
                    randno_sen=randrange(0,len(split_review_text))          ##Choosing random sentence from the list of slit sentences
                    selected_review_text=split_review_text[randno_sen]
                else:
                    selected_review_text=actual_review_text

                final_review_text=final_review_text.strip()+"."+selected_review_text.lstrip()[0:].capitalize()  ##Adding text to final review

            final_review_rating= int(round(actual_review_rating/10)) ##Rounding to nearest integer
            final_review_text=final_review_text.lstrip('.')+"."
            final_review_text=final_review_text.lstrip()[0:].capitalize()
            business_url=business_similar_categories[bid_sim]
            

            temp_row=[bid_sim,business_url,final_review_rating,final_review_text]
            writer.writerow(temp_row);
            

                
