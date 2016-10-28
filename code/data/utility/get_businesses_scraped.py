#!/usr/bin/env python
#Here we open the file storing the reviews we just scraped. The write file will contain the business urls that we were able to scrape in this run before failure. We will use these urls in the get_new_business_urls_list.py script. This will give use the new business_urls.csv list.

import csv

bizlist = []
writefile = open('business_urls_past_88.csv','wb')
writer = csv.writer(writefile)

with open('reviews_data_through_88.csv') as csvfile:
  readfile = csv.reader(csvfile)
  for row in readfile:
    if row[0] not in bizlist:
      print row[0]
      bizlist.append(row[0])
      writer.writerow([''.join(row[0])])
    else:
      continue

writefile.close()




