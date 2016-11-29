#!/usr/bin/env python

import csv

unique_bizlist = []
writefile = open('naperville_urls_unique.csv','wb')
writer = csv.writer(writefile)

with open('naperville.csv') as csvfile:
  readfile = csv.reader(csvfile)
  readfile.next()
  for row in readfile:
    print row[0]
    if row[0] in unique_bizlist:
      continue
    else:
      unique_bizlist.append(row[0])
      writer.writerow(row)

writefile.close()



