#!/usr/bin/env python
#get the unscraped urls

import csv

scraped_bizlist = []
bizlist = []

writefile = open('Seattle_part11.csv','wb')
writer = csv.writer(writefile)

#NEW CODE BETWEEN THESE COMMENTS

with open('Seattle_reviews_part10.csv') as csvfile1:
  readfile = csv.reader(csvfile1)
  for row in readfile:
    if row[0] in scraped_bizlist:
      continue
    else:
      print row[0]
      scraped_bizlist.append(row[0])
#___________________________________

'''with open('elgin_scraped.csv') as csvfile:
  readfile1 = csv.reader(csvfile)
  for row in readfile1:
    bizname = row
    scraped_bizlist.extend(bizname) '''

bizcount = 0

with open('Seattle_part10.csv') as csvfile2:
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




