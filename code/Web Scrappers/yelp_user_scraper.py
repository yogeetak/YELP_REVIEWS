import sys
import csv
import re
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from bs4 import BeautifulSoup 

user_ids_dict = ['THzkBtmO_F2NKynsAb_ECw','TARYDgo1f3sZqqb3hwFolw','U-nR7ND8CDN2x8ia73CH2Q','2wzBYj-J0xQ2RWD46cDI5w']
users_count = 0

## Read User ID data from file
##with open('joliet_part7.csv','rU') as readfile:
##  reader = csv.reader(readfile)
##  for row in reader:
##    user_ids_dict[row[0]] = [row[2]]
##    users_count += 1

writefile = open('user_data.csv','w')
writer = csv.writer(writefile)

users_processed_count = 0
user_basic_url="https://www.yelp.com/user_details?userid="

for u_id in user_ids_dict: 
  user_url=user_basic_url.strip()+u_id
  
  try:
    page_html = urlopen(user_url)
    
  except urllib.HTTPError as e:
    checksLogger.error('URLError = ' + str(e.code))
    
  except urllib.URLError as e:
    checksLogger.error('URLError = ' + str(e.reason))
    
  except httplib.HTTPException as e:
    checksLogger.error('HTTPException')
    
  except Exception:
    import traceback
    checksLogger.error('generic exception: ' + traceback.format_exc())

  soup = BeautifulSoup(page_html,"html.parser")

  if soup.find("div","error-wrap") or not soup.find("div","user-profile_container"): 
    print("Cannot confirm User Account Loading Page: %s", u_id)
    break

  else: #(indent all below)
    #get user_name
    user_name_div = soup.findAll("div","user-profile_info arrange_unit")
    user_name = user_name_div[0].contents[1].string
    print(user_name)

    #get user_location
    user_location=soup.find("h3","user-location alternate").string
    print(user_location)
    
    #get user_tagline if any
    if(user_name_div[0].find('p','user-tagline')):
      user_tagline=user_name_div[0].find('p','user-tagline').string
    else:
        user_tagline=''
    print(user_tagline)

    #get number of friends
    info_list = soup.findAll("ul","user-passport-stats")
    friend_list_class = [tag.find("li","friend-count") for tag in info_list]
    friend_list_tag = [tag.find("strong") for tag in friend_list_class]
    friend_count=friend_list_tag[0].text
    print(friend_count)

    #get number of reviews written
    review_list_class = [tag.find("li","review-count") for tag in info_list]
    review_list_tag = [tag.find("strong") for tag in review_list_class]
    review_count=review_list_tag[0].text
    print(review_count)

    #get number of photos posted
    photo_list_class = [tag.find("li","photo-count") for tag in info_list]
    photo_list_tag = [tag.find("strong") for tag in photo_list_class]
    photo_count=photo_list_tag[0].text
    print(photo_count)

    #get rating distribution
    about_li=soup.findAll("div","user-details-overview_sidebar")
    rating_table=[tag.find("table","histogram histogram--alternating") for tag in about_li]

    five_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--1") for row in rating_table]
    five_start_count=five_star_tabl_cols[0].find('td','histogram_count').string
    print(five_start_count)
    
    four_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--2") for row in rating_table]
    four_start_count=four_star_tabl_cols[0].find('td','histogram_count').string
    print(four_start_count)
    
    three_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--3") for row in rating_table]
    three_start_count=three_star_tabl_cols[0].find('td','histogram_count').string
    print(three_start_count)

    two_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--4") for row in rating_table]
    two_start_count=two_star_tabl_cols[0].find('td','histogram_count').string
    print(two_start_count)
    
    one_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--5") for row in rating_table]
    one_start_count=one_star_tabl_cols[0].find('td','histogram_count').string
    print(one_start_count)

    ##get review votes
    useful_votes_list=soup.find("span","icon icon--18-useful-outline icon--size-18 u-space-r1")
    useful_review_count=useful_votes_list.parent.find("strong").text
    print("useful_review_count : %s",useful_review_count)
    
    funny_votes_list=soup.find("span","icon icon--18-funny-outline icon--size-18 u-space-r1")
    funny_review_count=funny_votes_list.parent.find("strong").text
    print("funny_review_count : %s",funny_review_count)

    cool_votes_list=soup.find("span","icon icon--18-cool-outline icon--size-18 u-space-r1")
    cool_review_count=cool_votes_list.parent.find("strong").text
    print("cool_review_count : %s",cool_review_count)

    ##get stats
    stats_list=soup.find(text='Stats').findNext('ul','ylist ylist--condensed')
    li=stats_list.findAll("li")
    items= [i.text.strip() for i in li]
    stats_dict={}
    for i in items:
      stats_dict[i.split('\n')[0].strip()]=i.split('\n')[1].strip()
    print(stats_dict)
    
    ##get total number of compliments
    pattern=re.compile('[\d+] Compliment')
    compliments_str=soup.find(string=pattern)
    if compliments_str:
      compliments_number=int(compliments_str.split(' ')[0])
    else:
      compliments_number=0
    print("compliments:",compliments_number)
    
    #get any other details yelping since,etc
    yelping_since_list=soup.find(text='Yelping Since')
    yelping_since=yelping_since_list.findNext('p').text
    print("yelping_since:", yelping_since)

    other_info_list=yelping_since_list.parent.parent.parent
    all_li=other_info_list.findAll("li")
    all_items= [i.text.strip() for i in all_li]
    other_info_dict={}
    for i in all_items:
      other_info_dict[i.split('\n')[0].strip()]=i.split('\n')[1].strip()
    print(other_info_dict)
    
    #elite since
    elite_status_count=0
    elite_since_list=soup.find("a","badge-bar")
    if elite_since_list:
      elite_status_count=len(elite_since_list.findAll("span"))
    print("elite_status_count:",elite_status_count)

    #view more graphs location distribution

user_url1="https://www.yelp.com/user_details_more_graphs_jquery/2wzBYj-J0xQ2RWD46cDI5w"
page_html1 = urlopen(user_url1)
soup1 = BeautifulSoup(page_html1,"html.parser")
print(soup1.prettify())
     
##      #CONSTRUCT USER ROWS - SEND EACH ROW TO file
#       review_data_row = []
##        review_data_row.extend([b_id,user_names[i],user_ids[i],user_cities[i],user_elite_statuses[i],user_has_pics[i],user_checkins[i],user_friend_counts[i],user_review_counts[i],review_ids[i],review_star_ratings[i],review_dates[i],review_texts[i]])
##        review_data_array = numpy.asarray(review_data_row)
##        writer.writerow(review_data_array)
###[string.encode('utf-8','xmlcharrefreplace') for string in review_data_row]
##
##  businesses_processed_count += 1

#close the writefile
writefile.close()


  


