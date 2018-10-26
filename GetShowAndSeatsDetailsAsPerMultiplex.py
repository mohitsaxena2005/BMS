from Helpers import HelperFunctions
import requests
from bs4 import BeautifulSoup
import io
from lxml import html

class GetShowSeatsMultiPlexDetails:
    movieInfoList = None
    fetchDateTime=None
    bookTicketUrl=None

    def __init__(self, mInfo,fetchDateTime, bookTicketUrl):
        self.fetchDateTime = fetchDateTime
        self.movieInfoList =mInfo


    def GetTheUrlForBookTicketsForMovie(self, movieName, movieId):
        dateTimePart=HelperFunctions().GetDateAsYYYYMMDDFormat(self.fetchDateTime)
        return self.bookTicketUrl.format(movieName, movieId, dateTimePart)

        

    def FillIntheShowAndMultiPlexDetails(self):
        for info in self.movieInfoList:
            url = self.GetTheUrlForBookTicketsForMovie(info.movieName, info.movieName)
            r = requests.get(url)
            soup = BeautifulSoup(r.content,"lxml")
