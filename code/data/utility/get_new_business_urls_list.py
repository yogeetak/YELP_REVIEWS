#!/usr/bin/env python
#get the unscraped urls

import csv

scraped_bizlist = []
bizlist = []

writefile = open('naperville_to_scrape.csv','wb')
writer = csv.writer(writefile)

with open('naperville_businesses_scraped_list.csv') as csvfile:
  readfile1 = csv.reader(csvfile)
  for row in readfile1:
    bizname = row
    scraped_bizlist.extend(bizname)

bizcount = 0
print scraped_bizlist

with open('naperville_urls_unique.csv') as csvfile2:
  readfile2 = csv.reader(csvfile2)
  for row in readfile2:
    business_name = row[0]
    if business_name in scraped_bizlist:
      continue
    else:
      writer.writerow(row)
      bizcount += 1

print bizcount

writefile.close()




