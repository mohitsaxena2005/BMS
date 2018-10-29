import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId

import io
from lxml import html
import re
import json

r = requests.get(url='https://in.bookmyshow.com/buytickets/badhaai-ho-national-capital-region-ncr/movie-ncr-ET00068588-MT/20181029')
soup = BeautifulSoup(r.content,"lxml")
x = soup.find('section', {'class':'phpShowtimes showtimes'})

# y = x.find('ul', {'id':'venuelist'})

# z = y.find_all('li', {'class' :'list'})
# print(z)
z = x.find_all('li', {'class' :'list'})
for i in z:
    # Capture the Multiplex details over here and store it in file.
    print('********************************************************************')
    print(i['data-name']) # Multiplex name - Carnival: Raheja Mall, Gurgaon
    # print(i['data-id'])    # Mutiplex Id - CGCG
    # print(i['data-sub-region-id'])    # Region Id = GURG
    # print(i['data-sub-region-name'])    # Region Id = GURG
    # print(i['data-lat'])    # Latitude
    # print(i['data-lng'])    # Longitude
    # print(i['data-allow-sales'])    # No idea
    # print(i['data-venue-app'])    # No idea
    # print(i['data-is-new-cinema'])    #
    # print(i['data-is-food-sales'])    #
    # print(i['data-is-multiplex'])    #
    # print(i['data-message-type'])    #
    # print(i['data-is-full-seat-layout'])    # No idea
    # print(i['data-has-mticket'])    # M tickets
    # print(i['data-has-cod'])    # No idea
    # print(i['data-has-cop'])    # No idea
    a = i.find('div', {'class' : 'body'})
    #print(a)
    for b in a:
        try:
            if b['data-online'] == 'Y':
                c=b.find_all('a')
                print(c[0]['data-seats-percent'])
                print(c[0]['data-showtime-code'])
                print(c[0]['data-seats-percent'])
                print(c[0]['data-is-atmos-enabled'])
                print(c[0]['data-cut-off-date-time'])
                d=json.loads(c[0]['data-cat-popup'])
                #print(d)
                for e in d:
                    print(e['price'])
                    print(e['desc'])
                    print(e['availabilityText'])
                    
                
        except:
                None
    
    

    
    # for b in a:
    #     if b['data-online'] == 'Y':
    #         print(b)
    #         # Get all the data over here
    #         c=b.find('a')
    #         print(c['data-seats-percent'])


