from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import csv
import sys
auth = Oauth1Authenticator(
    consumer_key= "RvGtzG-WzFOhufGfqqb7lw",
    consumer_secret="t1RMgbQSEQmZotZDlsgfHrUBDg4",
    token= "XVqzdbhJ4qxBzQUvUMRYs1p5q5QdZ54x",
    token_secret= "_dHVkCcc5gerUWGu6faJMyQ-TVs"
)
client = Client(auth)
page = 0
business_id_dict=[]
page_size = 20
header_row=['business_id','business_name','business_url','business_rating','business_locationaddress','business_city','business_statecode','business_zipcode','business_reviewcount','offset','page']
 
with open('business_urls.csv', 'w',encoding='utf8',newline='') as csvfile:  
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(header_row)

    ##calling YELP SEARCH API
    ##response = client.search(location="chicago",categories="restaurants", limit=page_size, offset=page * page_size)
    response = client.search(location="chicago",categories="restaurants", limit=page_size, offset=0)

    ##temp_offset_val=page * page_size
    temp_offset_val=0
    for business in response.businesses:
            temp_row=[]
            if(business.id in business_id_dict):
                continue;
            
            ##writing to csv file
            temp_row=[business.id,business.name,business.url,business.rating,business.location.address,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,temp_offset_val,page]
            writer.writerow(temp_row);
            
    while response:
        page += 1
        ##response = client.search(location="chicago", categories="restaurants", limit=page_size, offset=page * page_size)
        response = client.search(location="chicago", categories="restaurants", offset=page)
        ##temp_offset_val=page * page_size
        temp_offset_val=page 
        for business in response.businesses:
            temp_row=[]
            if(business.id in business_id_dict):
                continue;
            
            ##writing to csv file
            temp_row=[business.id,business.name,business.url,business.rating,business.location.address,business.location.city,business.location.state_code,business.location.postal_code,business.review_count,temp_offset_val,page]
            writer.writerow(temp_row);

