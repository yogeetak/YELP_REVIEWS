#!/usr/bin/env python
#prune redundant business urls

import csv

bizlist = []
writefile = open('business_urls.csv','wb')
writer = csv.writer(writefile)

with open('business_urls_all.csv') as csvfile:
  readfile = csv.reader(csvfile)
  readfile.next()
  for row in readfile:
    business = row[0]
    if business in bizlist:
      continue
    else:
      bizlist.append(row[0])
      writer.writerow(row)

print len(bizlist)

writefile.close()




