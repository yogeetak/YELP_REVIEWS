#!/usr/bin/env python

import csv
import numpy

bizcount = 0
scraped_bizlist = []
writefile = open('naperville_urls_unique.csv','wb')
writer = csv.writer(writefile)

with open('naperville.csv') as csvfile:
  readfile = csv.reader(csvfile)
  reader.next()
  for row in csvfile:
    #split_row = row.split(",")
    if row[0] in scraped_bizlist:
      continue
    else:
      scraped_bizlist.append(row[0])

print scraped_bizlist

with open('chicago.csv') as csvfile2:
  reader = csv.reader(csvfile2)
  reader.next()
  for row in reader:
    if row[0] in scraped_bizlist:
      continue
    else:
      #rowlist = [''.join(data) for data in row]
      rowlist_array = numpy.asarray(row)
      writer.writerow(row)
      bizcount += 1



