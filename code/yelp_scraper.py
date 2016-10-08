''' TODO: -need to append business id to each review row
          -write loop for going to next page (want 10 pages per business)
             --need to check whether each business has at least 10 pages
'''
#!/usr/bin/python
'''import psycopg2 #db interface
import sys'''
import socket
import csv
import urllib2
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup

'''
#CONNECT TO DB---------------------------------------------------
con = None
try:
  con = psycopg2.connect(database='test_db',user='postgres')
  cur = con.cursor()
#----------------------------------------------------------------
'''

#SCRAPE DATA
with open('business_urls_Run1.csv','rU') as readfile:
  reader = csv.reader(readfile)
  for row in reader:
    businesses_dict = {} #populate from API
    url_list = []
    url_list.extend([str(row[2])])
    businesses_dict.update({str(row[0]):url_list})

for b_id,urls in businesses_dict.iteritems(): #expand business urls, getting each page of 20 reviews
  urls.extend([urls[0] + '?start=%d' % i for i in range(20,120,20)])

writefile = open('reviews_data.csv', 'wb')
writer = csv.writer(writefile)

#Soup = BeautifulSoup.BeautifulSoup

for business_id,url in businesses_dict.iteritems():
  for review_page in url:
    page_html = urllib2.urlopen(url).read()
    soup = Soup(page_html)

    if soup.find("div","error-wrap") or not soup.find("div","review review--with-sidebar"): #check if page is valid
      break

    else: #(indent all below)
      #get user_names list
      names = soup.findAll("meta",attrs={"itemprop":"author"})
      user_names = [name['content'] for name in names] #final user_names list
  
      #get user_ids list
      just_review_uids = soup.findAll("li","user-name")
      just_review_uids_strings = [str(element) for element in just_review_uids]
      parse_uids_left = [x.split("userid=")[1] for x in just_review_uids_strings]   
      user_ids = [y.split("\"")[0] for y in parse_uids_left] #final user_ids list

      #get user_cities list
      tagged_locations = soup.findAll("li","user-location responsive-hidden-small")
      user_cities = [location.text for location in tagged_locations] #final user_cities list
  
      #get user elite status list
      reviews_list = soup.findAll("div",attrs={"itemprop":"review"})
      elite_tags = [tag.find("li","is-elite responsive-small-display-inline-block") for tag in reviews_list]
      user_elite_statuses = [0 if status == None else 1 for status in elite_tags] #final user_elite_statuses list, elite status = 1, not elite = 0

      #get user pics yes/no list
      names_list = soup.findAll("meta",attrs={"itemprop":"author"})
      names_list_text = [name['content'] for name in names_list]
      anchor_tag = soup.find("div","review-sidebar")
      img_tags_list = [str(anchor_tag.findNext("img",attrs={"alt":name})) for name in names_list_text]
      split_strings = [tag.split('src="')[1] for tag in img_tags_list]
      img_url_list = [tag.split('"') for tag in split_strings]
      user_has_pics = [0 if string == 'https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/aa0937a60f33/assets/img/default_avatars/user_60_square.png' else 1 for string in split_strings_2] #final user_has_pics list: has photo = 1, no photo = 0
    
      #get user friend counts
      friends_tag = soup.findAll("li","friend-count responsive-small-display-inline-block")
      user_friend_counts = [count.text.split("friend")[0] for count in friends_tag] #final ufc list
  
      #get user review counts
      reviews_count_tag = soup.findAll("li","review-count responsive-small-display-inline-block")
      review_counts = [rcount.text.split("review")[0] for rcount in reviews_count_tag] 
      user_review_counts = review_counts[1:] #final user_review_counts list
  
      #get review ids
      tagged_review_ids = [tag.find("div","data-review-id") for tag in reviews_list]
      split_review_ids = [str(review).split('data-review-id="'[1] for review in reviews_list)]
      review_ids = [review.split('"')[0] for review in split_review_ids] #final review_ids list
   
      #get review star ratings
      ratings = soup.findAll("meta",attrs={"itemprop":"ratingValue"})
      review_star_ratings = [rated['content'] for rated in ratings] #final star rating list
  
      #get review_dates list
      dates_list = soup.findAll("meta",attrs={"itemprop":"datePublished"})
      review_dates = [date['content'] for date in dates_list] #final publish dates list
  
      #get review_texts list
      bodies_of_reviews = soup.findAll("p",attrs={"itemprop":"description"}) 
      review_texts = [rev.text for rev in bodies_of_reviews] #final list of review text/body
  
      #CONSTRUCT REVIEW ROWS - SEND EACH ROW TO DB
      for i in range(0,19):
        review_data_row = []
        review_data_row.extend([business_id,user_names[i],user_ids[i],user_cities[i],user_elite_statuses[i],user_has_pics[i],user_friend_counts[i],user_review_counts[i],review_ids[i],review_star_ratings[i],review_dates[i],review_texts[i]])
        writer.writerow(review_data_row)

#close the writefile
writefile.close()

'''    
        #SEND DATA TO DB
        cur.execute("CREATE TABLE test_table(Column1 VARCHAR(10), Column2 VARCHAR(10))")
        cur.execute("INSERT INTO test_table VALUES('test1','testing1')")
        con.commit()

#CONNECT TO DB: CATCH ERRORS---------------------------------------------------------------------
except psycopg2.DatabaseError, e:
  if con:
    con.rollback()

  print 'Error %s' % e
  sys.exit(1)
#-------------------------------------------------------------------------------------------------

#CLOSE DB-----------------------------------------------------------------------------------------
finally:
  if con:
    con.close()
#-------------------------------------------------------------------------------------------------

'''


  


