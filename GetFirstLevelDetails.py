import requests
from bs4 import BeautifulSoup
from PatternMatching import RegularExpressionExtractions
from Models import MovieNameAndId
from Models import MovieInfo

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
    
    def GetUrlOfMoviesFromMovieInfoList(self):
        for movie in self.movieInfoList:
            mInfo = MovieInfo()
            mInfo.movieId = movie.movieId
            mInfo.movieName = movie.movieNameProcessed
            mInfo.movieName = movie.movieNameProcessed


