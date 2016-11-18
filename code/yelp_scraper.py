#!/usr/bin/python
#import psycopg2 #db interface
import numpy
import sys
import socket
import csv
import urllib2
from BeautifulSoup import BeautifulSoup
reload(sys)   #Hacky fix: beware--this needs to be investigated further before reusing script!
sys.setdefaultencoding('utf-8') #Hacky fix

'''
#CONNECT TO DB---------------------------------------------------
con = None
try:
  con = psycopg2.connect(database='test_db',user='postgres')
  cur = con.cursor()
#----------------------------------------------------------------
'''

#SCRAPE DATA
businesses_dict = {}
businesses_count = 0

with open('joliet_part7.csv','rU') as readfile:
  reader = csv.reader(readfile)
  for row in reader:
    businesses_dict[row[0]] = [row[2]]
    businesses_count += 1

writefile = open('joliet_reviews_part7.csv','w')
writer = csv.writer(writefile)

businesses_processed_count = 0

for b_id in businesses_dict: #expand business urls, getting each page of 20 reviews
  print "\n--------------Progress: {0} / {1} businesses scraped.-------------\n".format(businesses_processed_count,businesses_count)
  print b_id
  businesses_dict[b_id].extend([businesses_dict[b_id][0] + '?start=%d' % i for i in range(20,100,20)])
  print businesses_dict[b_id]

  for review_page in businesses_dict[b_id]:
    print review_page
    try:
      page_html = urllib2.urlopen(review_page).read()
    except urllib2.HTTPError, e:
      checksLogger.error('URLError = ' + str(e.code))
    except urllib2.URLError, e:
      checksLogger.error('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
      checksLogger.error('HTTPException')
    except Exception:
      import traceback
      checksLogger.error('generic exception: ' + traceback.format_exc())

    soup = BeautifulSoup(page_html)

    if soup.find("div","error-wrap") or not soup.find("div","review review--with-sidebar"): #check if page is valid
      break

    else: #(indent all below)
      #get user_names list
      names = soup.findAll("meta",attrs={"itemprop":"author"})
      user_names = [name['content'] for name in names] #final user_names list

      #get review count per page
      review_count = len(user_names)
  
      #get user_ids list
      just_review_uids = soup.findAll("li","user-name")
      just_review_uids_strings = [str(element) for element in just_review_uids]
      parse_uids_left = [x.split("userid=")[1] for x in just_review_uids_strings]   
      user_ids = [y.split("\"")[0] for y in parse_uids_left] #final user_ids list

      #get user_cities list
      tagged_locations = soup.findAll("li","user-location responsive-hidden-small")
      user_cities = [location.text for location in tagged_locations] #final user_cities list
  
      #get user elite status list
      reviews_list = soup.findAll("div","review-sidebar-content")
      reviews_list = reviews_list[1:]
      elite_tags = [tag.find("li","is-elite responsive-small-display-inline-block") for tag in reviews_list] 
      user_elite_statuses_bool = [0 if status == None else 1 for status in elite_tags] 
      user_elite_statuses = [str(x) for x in user_elite_statuses_bool] #final user_elite_statuses list, elite status = 1, not elite = 0

      #get check-ins
      review_content_list = soup.findAll("div","review-content")
      checkins_tags = [tag.find("span","icon icon--18-check-in icon--size-18 u-space-r-half") for tag in review_content_list]
      user_checkins_bool = [0 if checkin == None else 1 for checkin in checkins_tags] 
      user_checkins = [str(x) for x in user_checkins_bool] #final user_checkins list

      #get user pics yes/no list 
      names_list = soup.findAll("meta",attrs={"itemprop":"author"})
      names_list_text = [name['content'] for name in names_list]
      anchor_tag = soup.find("div","review-sidebar")
      img_tags_list = [str(anchor_tag.findNext("img",attrs={"alt":name})) for name in names_list_text]
      split_strings = [tag.split('src="')[1] for tag in img_tags_list]
      img_url_list = [tag.split('"') for tag in split_strings]
      user_has_pics_bool = [0 if string == 'https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/aa0937a60f33/assets/img/default_avatars/user_60_square.png' else 1 for string in img_url_list]
      user_has_pics = [str(x) for x in user_has_pics_bool] #final user_has_pics list: has photo = 1, no photo = 0
    
      #get user friend counts
      friends_tag = soup.findAll("li","friend-count responsive-small-display-inline-block")
      user_friend_counts = [count.text.split("friend")[0] for count in friends_tag] #final ufc list
  
      #get user review counts
      reviews_count_tag = soup.findAll("li","review-count responsive-small-display-inline-block")
      review_counts = [rcount.text.split("review")[0] for rcount in reviews_count_tag] 
      user_review_counts = review_counts[1:] #final user_review_counts list
  
      #get review ids
      reviews_listed = soup.findAll("div","review review--with-sidebar")
      reviews_listed = reviews_listed[1:]
      split_review_ids = [str(review).split('data-review-id="')[1] for review in reviews_listed]
      review_ids = [review.split('"')[0] for review in split_review_ids] #final review_ids list
   
      #get review star ratings
      reviews_content_list = soup.findAll("div",attrs={"itemprop":"review"})
      ratings_list = [tag.find("meta",attrs={"itemprop":"ratingValue"}) for tag in reviews_content_list]
      review_star_ratings = [rated['content'] for rated in ratings_list] #final star rating list
  
      #get review_dates list
      dates_list = soup.findAll("meta",attrs={"itemprop":"datePublished"})
      review_dates = [date['content'] for date in dates_list] #final publish dates list
  
      #get review_texts list
      bodies_of_reviews = soup.findAll("p",attrs={"itemprop":"description"}) 
      review_texts = [rev.text for rev in bodies_of_reviews] #final list of review text/body
  
      #CONSTRUCT REVIEW ROWS - SEND EACH ROW TO DB
      for i in range(0,review_count - 1):
        review_data_row = []
        review_data_row.extend([b_id,user_names[i],user_ids[i],user_cities[i],user_elite_statuses[i],user_has_pics[i],user_checkins[i],user_friend_counts[i],user_review_counts[i],review_ids[i],review_star_ratings[i],review_dates[i],review_texts[i]])
        review_data_array = numpy.asarray(review_data_row)
        writer.writerow(review_data_array)
#[string.encode('utf-8','xmlcharrefreplace') for string in review_data_row]

  businesses_processed_count += 1

#close the writefile
writefile.close()


''' ROW HEADINGS: <Business ID, Username, User ID, User City, Elite Status Y/N?, Has Pic Y/N?, Checkins, User Friend Count, User Review Count, Review ID, Review Star Rating, Review Date, Review Text>




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


  


