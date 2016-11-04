import csv
business_url_info={} ##Dictionary of Business Names and URL's
final_dict={}
header_row=['business_id','business_url','review_rating','formed_review_text']

with open('C://Users//ykutta2//Desktop//YELP_REVIEWS//SearchAPI results//chicago.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        business_url_info[row['business_id']]=row['business_url']
   
with open('C://Users//ykutta2//Desktop//YELP_REVIEWS//code//data//ready_data//CHICAGO_part1.csv', 'r',encoding='utf8',newline='') as csvreaderfile:
    reader = csv.DictReader(csvreaderfile)

    with open('testcase1_reviewdata.csv', 'w',encoding='utf8',newline='') as csvwriterfile:
         writer = csv.writer(csvwriterfile, dialect='excel')
         writer.writerow(header_row)
         unique_business_id=''
         for row in reader:
             if(row['business_id']== unique_business_id ):
                 if(row['elite_status']== '1' and len(review_text) <= 1000):
                     review_text=review_text + row['review_text'].split('.')[0]
                 
             else:
                 review_text=''
                 unique_business_id=row['business_id']
                 business_id=row['business_id']
                 if(business_id  in business_url_info): business_url=business_url_info[business_id]
                 else: business_url=''
                 review_rating=row['star_rating']
                 if(review_text == ''):final_review_text=row['review_text']
                 else: final_review_text=review_text.split('.')[0]
                 temp_row=[business_id,business_url,review_rating,final_review_text]
                 writer.writerow(temp_row);
            
            
           
           
        
