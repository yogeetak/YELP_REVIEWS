from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import csv
import sys
##auth = Oauth1Authenticator(
##    consumer_key= "",
##    consumer_secret="",
##    token= "",
##    token_secret= ""
##)


client = Client(auth)
page = 0
business_id_dict=[]
header_row=['business_id','business_name','business_url','business_rating','business_categories','business_locationaddress','business_country','business_city','business_statecode','business_zipcode','business_reviewcount','is_claimed','snippet_text','offset']
 
with open('business_urls.csv', 'w',encoding='utf8',newline='') as csvfile:  
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(header_row)

    ##calling YELP SEARCH API
    response = client.search(location="chicago",categories="restaurants",term="restaurants", offset=0)

    ##temp_offset_val=page * page_size
    temp_offset_val=0
    for business in response.businesses:
        temp_row=[]
        if(business.id in business_id_dict):
                continue;
        ##writing to csv file
        ##cleaning URL to take only busisness ID
        url=business.url.split('?')[0];
        temp_row=[business.id,business.name,url,business.rating,business.categories,business.location.address,business.location.country_code,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,business.is_claimed,business.snippet_text,temp_offset_val]
        writer.writerow(temp_row);
            
    while response:
        page += 1
        response = client.search(location="chicago", categories="restaurants",term="restaurants", offset=page)
        temp_offset_val=page 
        for business in response.businesses:
            temp_row=[]
            if(business.id in business_id_dict):
                continue;
            
            ##writing to csv file
            url=business.url.split('?')[0];
            temp_row=[business.id,business.name,url,business.rating,business.categories,business.location.address,business.location.country_code,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,business.is_claimed,business.snippet_text,temp_offset_val]
            writer.writerow(temp_row);

