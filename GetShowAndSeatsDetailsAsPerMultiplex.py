from Helpers import HelperFunctions
import requests
from bs4 import BeautifulSoup
import io
from lxml import html
from Models import ShowVenueInfo, MovieShowTimeInfo
import json

class GetShowSeatsMultiPlexDetails:
    movieInfoList = None
    fetchDateTime=None
    bookTicketUrl=None
    venueList=None
    showTimeInfoList=None

    def __init__(self, mInfo,fetchDateTime, bookTicketUrl):
        self.fetchDateTime = fetchDateTime
        self.movieInfoList =mInfo
        self.bookTicketUrl = bookTicketUrl
        self.venueList = []
        self.showTimeInfoList=[]

    def GetTheUrlForBookTicketsForMovie(self, movieName, movieId):
        dateTimePart=HelperFunctions().GetDateAsYYYYMMDDFormat(self.fetchDateTime)
        return self.bookTicketUrl.format(movieName, movieId, dateTimePart)

        

    def FillIntheShowAndMultiPlexDetails(self):
        for info in self.movieInfoList:
            #print(info.movieName, info.movieId)
            url = self.GetTheUrlForBookTicketsForMovie(info.movieNameFromUrl, info.movieId)
            print(url)
            r = requests.get(url)
            soup = BeautifulSoup(r.content,"lxml")
            x = soup.find('section', {'class':'phpShowtimes showtimes'})
            z = x.find_all('li', {'class' :'list'})
            for i in z:
                info = self.FillVenueList(i)
                self.FillShowTimeList(i,info)
                break

               
    def FillVenueList(self, venueDetails):
        vInfo = ShowVenueInfo()
        vInfo.VenueFullName = venueDetails['data-name']
        vInfo.VenueId = venueDetails['data-id']
        vInfo.VenueSubRegionName = venueDetails['data-sub-region-id']
        vInfo.VenueSubRegionId = venueDetails['data-sub-region-name']
        vInfo.VenueLatitude = venueDetails['data-lat']
        vInfo.VenueLongitude = venueDetails['data-lng']
        vInfo.VenueAllowSales = venueDetails['data-allow-sales']
        vInfo.IsVenueApp = venueDetails['data-venue-app']
        vInfo.IsNewCinema = venueDetails['data-is-new-cinema']
        vInfo.IsFoodSalesAvailable = venueDetails['data-is-food-sales']
        vInfo.IsMultiplex = venueDetails['data-is-multiplex']
        vInfo.MessageType = venueDetails['data-message-type']
        vInfo.IsFullSeatLayoutAvailable = venueDetails['data-is-full-seat-layout']
        vInfo.IsMticketAccepted = venueDetails['data-has-mticket']
        vInfo.HasCOD = venueDetails['data-has-cod']
        vInfo.HasCOP = venueDetails['data-has-cop']
        vInfo.FetchDateTime = self.fetchDateTime

        self.venueList.append(vInfo)
        return vInfo

    def FillShowTimeList(self, venueTimeInfo,vInfo):
            a = venueTimeInfo.find('div', {'class' : 'body'})
            for b in a:
                try:
                    if b['data-online'] == 'Y':
                        c=b.find_all('a')
                        movieShowTimeInfo = MovieShowTimeInfo()
                        movieShowTimeInfo.multiplexName = vInfo.VenueFullName
                        movieShowTimeInfo.multiplexId = vInfo.VenueId
                        movieShowTimeInfo.fetchDateTime = vInfo.FetchDateTime
                        movieShowTimeInfo.availableSeatsPercent = c[0]['data-seats-percent']
                        movieShowTimeInfo.showTimeCode = c[0]['data-showtime-code']
                        movieShowTimeInfo.isAtmosEnabled = c[0]['data-is-atmos-enabled']
                        movieShowTimeInfo.showTime = c[0]['data-date-time']
                        movieShowTimeInfo.cutOffTime = c[0]['data-cut-off-date-time']
                        movieShowTimeInfo.showTimeType = c[0]['data-showtime-filter-index']
                        
                        d=json.loads(c[0]['data-cat-popup'])
                        for e in d:
                            movieShowTimeInfo.seatPrice=e['price']
                            movieShowTimeInfo.seatClass=e['desc']
                            movieShowTimeInfo.seatAvailabilityText=e['availabilityText']
                            self.showTimeInfoList.append(movieShowTimeInfo)
                except:
                        None