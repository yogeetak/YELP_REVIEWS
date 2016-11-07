###TESTCASE 8 : OLDEST ELITE USER POSITIVE RATING
##PICK oldest 5 star rating Elite user review from same business
#Repost review

import csv
from datetime import datetime

business_url_info={} ##Dictionary of Business Names and URL's
final_dict={}
header_row=['business_id','business_url','review_posted_date','review_rating','formed_review_text']

##with open('/Users/apple/Desktop/YELP_REVIEWS/SearchAPI results/chicago.csv', 'r',encoding='utf8',newline='') as csvfile:
with open('C://Users//ykutta2//Desktop//YELP_REVIEWS//SearchAPI results//chicago.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        business_url_info[row['business_id']]=row['business_url']
   
##with open('//Users//apple//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part2.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
with open('C://Users//ykutta2//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
    reader = csv.DictReader(csvreaderfile)
    lowest_date_val=datetime.strptime('31/12/14', '%d/%m/%y').date()
    business_id=0
    review_text=''
    review_rating=''
    for row in reader:
        if(row['star_rating'] == '5' and row['elite_status'] == '1'):  ##considering reviews of rating 5 star elite user only
            if(len(row['review_date'].split('/')[2]) == 4):   ##year 2016 format
                date_val= datetime.strptime(row['review_date'], '%m/%d/%Y').date()
            else:
                date_val= datetime.strptime(row['review_date'], '%d/%m/%y').date()
                
            if(date_val.year not in [2014,2013,2012,2011,2010,2009]):
               continue

            if(row['business_id'] not in final_dict):
                final_dict[row['business_id']] = [date_val.strftime('%m/%d/%y') +" ,##, "+ row['star_rating']+" ,##, "+row['review_text']]
                    
            if(lowest_date_val <  date_val):
                continue
            else:
                lowest_date_val=date_val
                business_id=row['business_id']
                review_text=row['review_text']
                review_rating=row['star_rating']
                del final_dict[row['business_id']]
                final_dict[row['business_id']] = [lowest_date_val.strftime('%m/%d/%y') +" ,##, "+row['star_rating']+" ,##, "+row['review_text']]
                   
    
with open('testcase8_ChicagoPart1_ReviewText_Data.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
    writer = csv.writer(csvwriterfile, dialect='excel')
    writer.writerow(header_row)
    for bid in final_dict:
        if(bid in business_url_info): business_url=business_url_info[bid]   ##If Valid URL exists, then proceed
        else: continue
        sample_review_list=final_dict[bid]
        for text in sample_review_list:
            temp_row=[bid,business_url,text.split(',##,')[0],text.split(',##,')[1],text.split(',##,')[2]]
            writer.writerow(temp_row);
