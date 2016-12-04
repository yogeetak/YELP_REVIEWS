import csv
import re
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from bs4 import BeautifulSoup



i=0
p=0
#for p in range(1,5):
with open('Seattle.csv',encoding='ISO-8859-1') as readfile:
   reader = csv.DictReader(readfile)
   for row in reader:
      i=i+1

print(i)
      
  

