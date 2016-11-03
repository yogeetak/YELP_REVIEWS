#!/usr/bin/env python
#Here we open the file storing the reviews we just scraped. The write file will contain the business urls that we were able to scrape in this run before failure. We will use these urls in the get_new_business_urls_list.py script. This will give use the new business_urls.csv list.

import csv

bizlist = []
writefile = open('naperville_businesses_scraped_list.csv','wb')
writer = csv.writer(writefile)

with open('naperville_p1.csv') as csvfile:
  readfile = csv.reader(csvfile)
  for row in readfile:
    if row[0] in bizlist:
      continue
    else:
      print row[0]
      bizlist.append(row[0])
      writer.writerow([''.join(row[0])])

writefile.close()




