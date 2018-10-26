import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId
from Helpers import HelperFunctions

import io
from lxml import html
import re


class GetMovieNameAndIdList:
        bmsUrl =''

        def __init__(self,bms):
            self.bmsUrl = bms
            print(self.bmsUrl)

        #bms = 'https://in.bookmyshow.com/national-capital-region-ncr/movies'

    
        def GetList(self):
            r = requests.get(url=self.bmsUrl)
            webpage = html.fromstring(r.content)
            pattern = re.compile('.national-capital-region-ncr/movies.')
            nowShowingMovieList = []
            regExpressionExtractions=RegularExpressionExtractions()
            helperFuncs = HelperFunctions()
            fetchDateTime = helperFuncs.GetFetchDateTime()
            for element, attribute, link, pos in webpage.iterlinks():
                if not pattern.match(link):
                  continue
                tup = regExpressionExtractions.ExtractMovieNameAndIdFromUrl(str(link))
                if tup is not None:
                    #print(str(link))
                    movieNameAndId = MovieNameAndId(tup[0],tup[1],fetchDateTime)
                    nowShowingMovieList.append(movieNameAndId)
            
            return (nowShowingMovieList, fetchDateTime)



