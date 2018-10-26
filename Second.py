import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId

import io
from lxml import html
import re


r = requests.get(url='https://in.bookmyshow.com/national-capital-region-ncr/movies/badhaai-ho/ET00068588')
soup = BeautifulSoup(r.content,"lxml")

# PercentOfHeart
x = soup.find('span', {'class':'__percentage'})
#print(x.text.replace('%',''))


# Number of votes
x = soup.find('div', {'class':'__votes'})
#print(int(x.text.replace('votes','').replace(',','').strip()))



# critic rating
x = soup.find('div', {'class':'critic-rating'})
y = x.find('ul', {'class':'rating-stars'})
print(float(y['data-value']))

x = soup.find('div', {'class':'user-rating'})

#y = x.find('span', {'class':'__rating'})
y = x.find('ul', {'class':'rating-stars'})


# User rating
#print(y['data-value'])

# Language
x = soup.find('a', {'class':'__language'})
#print(x.text)

x = soup.find_all('span', {'itemprop':'genre'})
genreList=[]
for i in x:
    genreList.append(i['content'])


