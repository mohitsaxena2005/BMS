import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId, MovieInfo


import io
from lxml import html
import re

class GetFirstLevelDetails:

    seedUrl = None
    firstScrapeMovieList = []
    movieInfoList = []
    def __init__(self, seedUrl, movieInfoList):
        self.seedUrl = seedUrl
        self.firstScrapeMovieList = movieInfoList
        self.GetUrlOfMoviesFromMovieInfoList()
        
    
    def GetUrlOfMoviesFromMovieInfoList(self):
        for key, movie in self.firstScrapeMovieList.items():
            mInfo = MovieInfo()
            mInfo.movieId = movie.movieId
            mInfo.movieName = movie.movieNameProcessed
            mInfo.movieNameFromUrl = movie.movieNameFromUrl
            mInfo.fetchDateTime = movie.fetchDateTime
            mInfo.movieUrl = self.seedUrl + mInfo.movieNameFromUrl + '/'+ mInfo.movieId
            self.movieInfoList.append(mInfo)

    def FillInMovieInfoDetails(self):
        for info in self.movieInfoList:
            r = requests.get(info.movieUrl)
            #print(info.movieUrl)
            soup = BeautifulSoup(r.content,"lxml")
            info.movieHeartRatingPercent = self.GetPercentOfHeart(soup)
            info.numOfVotes = self.GetNumberOfVotes(soup)
            info.critics_rating = self.GetCriticRating(soup)
            info.user_rating = self.GetUserRating(soup)
            info.language = self.GetLanguage(soup)
            info.genre = self.GetGenreList(soup)
        return self.movieInfoList


    def GetPercentOfHeart(self, bSoup):
        try:
            x = bSoup.find('span', {'class':'__percentage'})
            return x.text.replace('%','')
        except:
            return None
        
        

    def GetNumberOfVotes(self, bSoup):
        try:
            x=int(bSoup.find('div', {'class':'__votes'}).text.replace('votes','').replace(',','').strip())
            return x
        except:
            return None

    def GetCriticRating(self, bSoup):
        try:
            x = bSoup.find('div', {'class':'critic-rating'})
            y = x.find('ul', {'class':'rating-stars'})
            return float(y['data-value'])
        except:
            return None

    def GetUserRating(self, bSoup):
        try:
            x = bSoup.find('div', {'class':'user-rating'})
            y = x.find('ul', {'class':'rating-stars'})
            return float(y['data-value'])
        except:
            return None

    def GetLanguage(self, bSoup):
        try:
            x= bSoup.find('a', {'class':'__language'}).text
            return x
        except:
            return None

    def GetGenreList(self, bSoup):
        try:
            x = bSoup.find_all('span', {'itemprop':'genre'})
            genreList=[]
            for i in x:
                genreList.append(i['content'])
            return genreList
        except:
            return None