###TESTCASE 4 : POSITIVE REVIEWS WITH REGATIVE RATING
##PICK all positive 4,5 rating reviews from same business
##Pick random samples from same business page,
####Splitting the text of each review with fulllstops and a random index of the sentence between (0,#of split sentences)
##prepare final reivew with either 1 or 2  star rating
##OUTPUT: CSV Document for test case 1


import csv
import random
from random import randrange

business_url_info={} ##Dictionary of Business Names and URL's
final_dict={}
header_row=['business_id','business_url','review_rating','formed_review_text']

with open('/Users/apple/Desktop/YELP_REVIEWS/SearchAPI results/chicago.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        business_url_info[row['business_id']]=row['business_url']
   
with open('//Users//apple//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
    reader = csv.DictReader(csvreaderfile)
    
    for row in reader:
        if(row['star_rating'] == '4' or row['star_rating'] == '5'):  ##considering reviews of rating 4 or 5 only
            if(row['business_id'] not in final_dict):
                final_dict[row['business_id']] = [row['star_rating']+" ,##, "+row['review_text']]
            else:
                original_list = final_dict.get(row['business_id'])
                original_list.append(row['star_rating']+" ,##,  "+row['review_text'])
                final_dict[row['business_id']] = original_list
 
with open('testcase4_ChicagoPart1_ReviewText_Data.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
        writer = csv.writer(csvwriterfile, dialect='excel')
        writer.writerow(header_row)

        for bid in final_dict:
            
            if(bid in business_url_info): business_url=business_url_info[bid]   ##If Valid URL exists, then proceed
            else: continue

            actual_review_text=''
            final_review_text=''
            review_list=final_dict[bid]
            sample_review_list=random.sample(review_list,len(review_list)) ##choose random sample of reviews for each business

            for text in sample_review_list:
                actual_review_text=text.split(',##,')[1]
                if("." in actual_review_text):
                    split_review_text=actual_review_text.split('.')   ##Splitting the text with fulllstops and taking a random index of the sentence\
                    randno=randrange(0,len(split_review_text))
                    final_review_text=final_review_text.strip()+"."+split_review_text[randno].lstrip()[0:].capitalize()

            if(final_review_text==''):
                continue

            final_review_rating= randrange(1,3)
            final_review_text=final_review_text.lstrip('.')+"."
            final_review_text=final_review_text.lstrip()[0:].capitalize()

            temp_row=[bid,business_url,final_review_rating,final_review_text]
            writer.writerow(temp_row);
