import csv
import re
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from bs4 import BeautifulSoup


def load_Users_Dict():
  user_ids_list=[]
  ##Read User ID data from file
  ##with open('/Users/apple/Desktop/YELP_REVIEWS/code/data/user_data_to_scrape/user_ids_chicago_part1.csv',encoding='ISO-8859-1') as readfile:
  with open('user_ids_chicago_part1.csv',encoding='ISO-8859-1') as readfile:
    reader = csv.DictReader(readfile)
    for row in reader:
      user_ids_list.append(row['user_id'])
      
  return user_ids_list


def load_url(url_Text):
  try:
    page_html = urlopen(url_Text)
    
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

  return soup


def main():
  match="!@#$%^&*()[]{},:/<>?\|`~-=_+"
  users_count = 0
  users_processed_count = 1
  already_scrapped_list=[]
  user_basic_url="https://www.yelp.com/user_details?userid="
  review_url="https://www.yelp.com/user_details_reviews_self?"
  header_row=['user_id','user_name','user_location','user_tagline','friend_count','review_count','photo_count','five_start_count','four_start_count',
              'three_start_count','two_start_count','one_start_count','useful_review_count','funny_review_count','cool_review_count','stats_dict',
              'compliments_number','yelping_since','other_info_dict','elite_status_count','user_cities_dict','user_city_count']


  with open('user_data.csv', 'w',encoding='utf-8',newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerow(header_row)
    #user_ids_dict=["mRArfi2eu17IkBy9eGvB9A"]
    user_ids_dict=load_Users_Dict()
    users_count=len(user_ids_dict)

    for u_id in user_ids_dict:
      try:
        user_tagline=''
        five_start_count=0
        four_start_count=0
        three_start_count=0
        two_start_count=0
        one_start_count=0
        useful_review_count=0
        funny_review_count=0
        cool_review_count=0
        all_user_cities={}
        user_city_count=0
        stats_dict={}
        
        if u_id in already_scrapped_list:
          continue
        
        user_url=user_basic_url.strip()+u_id
        soup = load_url(user_url)

        if not soup:
          continue

        if soup.find("div","error-wrap") or not soup.find("div","user-profile_container"): 
          print("Cannot confirm User Account Loading Page: %s", u_id)
          print(user_url)
          continue

        else:
          
          #print(user_url)
          print("T\n--------------Total Users: {0}--------- Users_current_processed_count: {1}".format(users_count,users_processed_count))
          
          #get user_name
          user_name_div = soup.findAll("div","user-profile_info arrange_unit")
          user_name = user_name_div[0].contents[1].string
          user_name=user_name.translate ({ord(c): " " for c in match})
          user_name=user_name.replace('"','')
          er_name=user_name.replace("'",'')
          #print(user_name)

          #get user_location
          user_location=soup.find("h3","user-location alternate").string
          #print(user_location)
          
          #get user_tagline if any
          if(user_name_div[0].find('p','user-tagline')):
            user_tagline=user_name_div[0].find('p','user-tagline').string
            user_tagline=user_tagline.translate ({ord(c): " " for c in match})
            user_tagline=user_tagline.replace('"','')
            user_tagline=user_tagline.replace("'",'')
          #print(user_tagline)

          #get number of friends
          info_list = soup.findAll("ul","user-passport-stats")
          friend_list_class = [tag.find("li","friend-count") for tag in info_list]
          friend_list_tag = [tag.find("strong") for tag in friend_list_class]
          friend_count=friend_list_tag[0].text
          #print("Total Number of Friends: ",friend_count)

          #get number of reviews written
          review_list_class = [tag.find("li","review-count") for tag in info_list]
          review_list_tag = [tag.find("strong") for tag in review_list_class]
          review_count=review_list_tag[0].text
          #print("Total Number of Reviews: ",review_count)

          #get number of photos posted
          photo_list_class = [tag.find("li","photo-count") for tag in info_list]
          photo_list_tag = [tag.find("strong") for tag in photo_list_class]
          photo_count=photo_list_tag[0].text
          #print("Total Number of Photos: ",photo_count)

          #get rating distribution  (if any)
          rating=soup.find(text='Rating Distribution')
          #print("Rating Distribution")
          if rating:
            about_li=soup.findAll("div","user-details-overview_sidebar")
            rating_table=[tag.find("table","histogram histogram--alternating") for tag in about_li]

            five_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--1") for row in rating_table]
            if five_star_tabl_cols:
              five_start_count=five_star_tabl_cols[0].find('td','histogram_count').string
            #print(five_start_count)
            
            four_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--2") for row in rating_table]
            if four_star_tabl_cols:
              four_start_count=four_star_tabl_cols[0].find('td','histogram_count').string
            #print(four_start_count)
            
            three_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--3") for row in rating_table]
            if three_star_tabl_cols:
              three_start_count=three_star_tabl_cols[0].find('td','histogram_count').string
            #print(three_start_count)

            two_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--4") for row in rating_table]
            if two_star_tabl_cols:
              two_start_count=two_star_tabl_cols[0].find('td','histogram_count').string
            #print(two_start_count)
            
            one_star_tabl_cols = [row.find('tr',"histogram_row histogram_row--5") for row in rating_table]
            if one_star_tabl_cols:
              one_start_count=one_star_tabl_cols[0].find('td','histogram_count').string
            #print(one_start_count)

          ##get review votes  (if any)
          votes=soup.find(text='Review Votes')
          if votes:
            useful_votes_list=soup.find("span","icon icon--18-useful-outline icon--size-18 u-space-r1")
            if useful_votes_list:
              useful_review_count=useful_votes_list.parent.find("strong").text
            #print("useful_review_count : ",useful_review_count)
            
            funny_votes_list=soup.find("span","icon icon--18-funny-outline icon--size-18 u-space-r1")
            if funny_votes_list:
              funny_review_count=funny_votes_list.parent.find("strong").text
            #print("funny_review_count : ",funny_review_count)

            cool_votes_list=soup.find("span","icon icon--18-cool-outline icon--size-18 u-space-r1")
            if cool_votes_list:
               cool_review_count=cool_votes_list.parent.find("strong").text
            #print("cool_review_count : ",cool_review_count)

          ##get stats (if any)
          stats=soup.find(text='Stats')
          if stats:
            stats_list=stats.findNext('ul','ylist ylist--condensed')
            li=stats_list.findAll("li")
            items= [i.text.strip() for i in li]
            for i in items:
              stats_dict[i.split('\n')[0].strip()]=i.split('\n')[1].strip()
            #print(stats_dict)
          
          ##get total number of compliments (if any)
          pattern=re.compile('[\d+] Compliment')
          compliments_str=soup.find(string=pattern)
          if compliments_str:
            compliments_number=int(compliments_str.split(' ')[0])
          else:
            compliments_number=0
          #print("compliments:",compliments_number)
          
          #get any other details yelping since,etc
          yelping_since_list=soup.find(text='Yelping Since')
          yelping_since=yelping_since_list.findNext('p').text
          #print("yelping_since:", yelping_since)

          other_info_list=yelping_since_list.parent.parent.parent
          all_li=other_info_list.findAll("li")
          all_items= [i.text.strip() for i in all_li]
          other_info_dict={}
          for i in all_items:
            i=i.translate ({ord(c): " " for c in match})
            other_info_dict[i.split('\n')[0].strip()]=i.split('\n')[1].strip()
          #print(other_info_dict)
          
          #elite since
          elite_status_count=0
          elite_since_list=soup.find("a","badge-bar")
          if elite_since_list:
            elite_status_count=len(elite_since_list.findAll("span"))
          #print("elite_status_count:",elite_status_count)

          #Loading User Review Page
          url_review_list=[review_url.strip()+"userid="+u_id+"&rec_pagestart=%d" % i for i in range(0,150,10)]
          for url in url_review_list:
            review_soup=load_url(url)
                                     
            if review_soup.findAll("p",{"class":"arrange_unit arrange_unit--fill"}):
              #print("No More Reviews to scrape")
              #print()
              break
            location=review_soup.findAll("address")
            for loc in location:
              if "," not in loc.text:
                continue
              bis_state_name=loc.text.strip().split(',')[1].strip()[:2]
              if bis_state_name in all_user_cities:
                temp_val=int(all_user_cities[bis_state_name]) + 1
                all_user_cities[bis_state_name] = temp_val
              else:
                all_user_cities[bis_state_name] = 1

          #print(all_user_cities)
            
          ##CONSTRUCT USER ROWS - SEND EACH ROW TO file

          review_data_row = [u_id,user_name,user_location,user_tagline,friend_count,review_count,photo_count,five_start_count,four_start_count,
                            three_start_count,two_start_count,one_start_count,useful_review_count,funny_review_count,cool_review_count,stats_dict,
                            compliments_number,yelping_since,other_info_dict,elite_status_count,all_user_cities,len(all_user_cities)]
          writer.writerow(review_data_row)
          already_scrapped_list.append(u_id)
          users_processed_count=users_processed_count+1
      except:
        print("Exception Occured in user_id: ", u_id)
        print(user_url)
        print()
        pass

    
if __name__ == '__main__':
    main()

  


