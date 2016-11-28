import csv
user_ids_list=[]

with open('/Users/apple/Desktop/YELP_REVIEWS/code/data/ready_data/chicago/Sentiment Analysis/chicago_reviews_part4_dict_sentiment_Data.csv',encoding='ISO-8859-1') as readfile:
  reader = csv.DictReader(readfile)
  for row in reader:
    if row['need_inspection'] == 'YES':
      if row['user_id'] not in user_ids_list:
        user_ids_list.append(row['user_id'])
      else:
        continue

with open('/Users/apple/Desktop/YELP_REVIEWS/code/data/ready_data/chicago/Sentiment Analysis/chicago_reviews_part5_dict_sentiment_Data.csv',encoding='ISO-8859-1') as readfile1:
  reader1 = csv.DictReader(readfile1)
  for row in reader1:
    if row['need_inspection'] == 'YES':
      if row['user_id'] not in user_ids_list:
        user_ids_list.append(row['user_id'])
      else:
        continue

with open('/Users/apple/Desktop/YELP_REVIEWS/code/data/ready_data/chicago/Sentiment Analysis/chicago_reviews_part6_dict_sentiment_Data.csv',encoding='ISO-8859-1') as readfile2:
  reader2 = csv.DictReader(readfile2)
  for row in reader2:
    if row['need_inspection'] == 'YES':
      if row['user_id'] not in user_ids_list:
        user_ids_list.append(row['user_id'])
      else:
        continue


with open('user_ids_chicago_part2.csv', 'w',encoding='ISO-8859-1',newline='') as csvwriterfile:
  writer = csv.writer(csvwriterfile, dialect='excel')
  header_row=["S_No","user_id"]
  writer.writerow(header_row)
  count=1
  for i in user_ids_list:
    temp = [count,i]
    writer.writerow(temp)
    count=count+1

  


