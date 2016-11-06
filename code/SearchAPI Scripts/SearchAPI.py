from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import csv
import sys
auth = Oauth1Authenticator(
    consumer_key= "",
    consumer_secret="",
    token= "",
    token_secret= "-TVs"
)
client = Client(auth)
page = 0
business_id_dict={}
header_row=['business_id','business_name','business_url','business_rating','business_categories','business_locationaddress','business_country','business_city','business_statecode','business_zipcode','business_reviewcount','is_claimed','snippet_text','offset']
 
<<<<<<< Updated upstream:code/SearchAPI Scripts/SearchAPI.py
with open('chicago_irishpubs_categories.csv', 'w',encoding='utf8',newline='') as csvfile:  
=======
with open('joliet.csv', 'w',encoding='utf8',newline='') as csvfile:  
>>>>>>> Stashed changes:code/SearchAPI.py
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(header_row)

    ##calling YELP SEARCH API
<<<<<<< Updated upstream:code/SearchAPI Scripts/SearchAPI.py
    response = client.search(location="chicago",categories="restaurants",term="irish,pubs", offset=0)
=======
    response = client.search(location="joliet",categories="restaurants",term="restaurants", offset=0)
>>>>>>> Stashed changes:code/SearchAPI.py
    temp_offset_val=0
    for business in response.businesses:
        temp_row=[]
        if(business.id in business_id_dict):
            continue;
        business_id_dict[business.id]=business.name
        ##writing to csv file
        ##cleaning URL to take only busisness ID
        url=business.url.split('?')[0];
        temp_row=[business.id,business.name,url,business.rating,business.categories,business.location.address,business.location.country_code,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,business.is_claimed,business.snippet_text,temp_offset_val]
        writer.writerow(temp_row);
            
    while response:
        page += 1
<<<<<<< Updated upstream:code/SearchAPI Scripts/SearchAPI.py
        response = client.search(location="chicago", categories="restaurants",term="irish,pubs", offset=page)
=======
        response = client.search(location="joliet", categories="restaurants",term="restaurants", offset=page)
>>>>>>> Stashed changes:code/SearchAPI.py
        temp_offset_val=page 
        for business in response.businesses:
            temp_row=[]
            if(business.id in business_id_dict):
                continue;
            business_id_dict[business.id]=business.name
            ##writing to csv file
            url=business.url.split('?')[0];
            temp_row=[business.id,business.name,url,business.rating,business.categories,business.location.address,business.location.country_code,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,business.is_claimed,business.snippet_text,temp_offset_val]
            writer.writerow(temp_row);
    for i in business_id_dict:
        print(i)
