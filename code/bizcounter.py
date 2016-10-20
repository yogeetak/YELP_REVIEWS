#!/usr/bin/env python

import csv

bizlist = []

with open('reviews_data_upto_stella-barra-pizzeria-chicago.csv') as csvfile:
  readCSV = csv.reader(csvfile)
  for row in readCSV:
    business = row[0]
    if business in bizlist:
      continue
    else:
      bizlist.append(row[0])

print bizlist
print len(bizlist)
