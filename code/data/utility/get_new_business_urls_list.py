#!/usr/bin/env python
#get the unscraped urls

import csv

scraped_bizlist = []
bizlist = []

writefile = open('currently_unscraped_business_urls.csv','wb')
writer = csv.writer(writefile)

with open('business_urls_past_88.csv') as csvfile:
  readfile1 = csv.reader(csvfile)
  for row in readfile1:
    bizname = row[0]
    scraped_bizlist.append(bizname)

with open('burls.csv') as csvfile2:
  readfile2 = csv.reader(csvfile2)
  for row in readfile2:
    bizlist.append(row)

bizcount = 0

for business_data in bizlist:
  business_name = business_data[0]
  print business_name
  if business_name in scraped_bizlist:
    continue
  else:
    writer.writerow(business_data)
    bizcount += 1

print bizcount

writefile.close()




