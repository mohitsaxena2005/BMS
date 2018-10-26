import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId

import io
from lxml import html
import re
import json

r = requests.get(url='https://in.bookmyshow.com/buytickets/badhaai-ho-national-capital-region-ncr/movie-ncr-ET00068588-MT/20181025')
soup = BeautifulSoup(r.content,"lxml")
x = soup.find('section', {'class':'phpShowtimes showtimes'})

# y = x.find('ul', {'id':'venuelist'})

# z = y.find_all('li', {'class' :'list'})
# print(z)
z = x.find_all('li', {'class' :'list'})
for i in z:
    # Capture the Multiplex details over here and store it in file.
    print(i['data-name'])
    a = i.find('div', {'class' : 'body'})
    #print(a)
    for b in a:
        try:
            if b['data-online'] == 'Y':
                c=b.find_all('a')
                print(c[0]['data-seats-percent'])
                d=json.loads(c[0]['data-cat-popup'])
                print(d)
                for e in d:
                    print(e['price'])
                    print(e['desc'])
                    print(e['availabilityText'])
                    
                break
        except:
                None
    break
    

    
    # for b in a:
    #     if b['data-online'] == 'Y':
    #         print(b)
    #         # Get all the data over here
    #         c=b.find('a')
    #         print(c['data-seats-percent'])


