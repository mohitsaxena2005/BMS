
from ScrapeBMSFirstTime import GetMovieNameAndIdList
from FileWriter import FileWriter
from GetFirstLevelDetails import GetFirstLevelDetails
from GetShowAndSeatsDetailsAsPerMultiplex import GetShowSeatsMultiPlexDetails
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime as dt



def DriveScrape():
    seedUrl = 'https://in.bookmyshow.com/national-capital-region-ncr/movies/'
    bookTicketsUrl = 'https://in.bookmyshow.com/buytickets/{}-national-capital-region-ncr/movie-ncr-{}-MT/{}'
    #bookTicketsUrl = 'https://in.bookmyshow.com/buytickets/{movieNameFromUrl}-national-capital-region-ncr/movie-ncr-{MovieId}}-MT/{TodaysDate}'
    l = GetMovieNameAndIdList(seedUrl)
    x= l.GetList()

    fw = FileWriter()
    fw.WriteScapeBMSFirstTimeFileForListOfMovies(x[0],x[1])

    details = GetFirstLevelDetails(seedUrl, x[0])
    movieInfoList = details.FillInMovieInfoDetails()


    fw = FileWriter()
    fw.WriteFirstLevelDetailsToCSV(movieInfoList,x[1])

    showDetails = GetShowSeatsMultiPlexDetails(movieInfoList, x[1],bookTicketsUrl)
    venueAndShowTimeInfoLists = showDetails.FillIntheShowAndMultiPlexDetails()

    fw = FileWriter()
    fw.WriteVenueList(venueAndShowTimeInfoLists[0],x[1])
    fw.WriteShowTimeInfoList(venueAndShowTimeInfoLists[1],x[1])


scheduler = BlockingScheduler()
scheduler.add_job(DriveScrape,'interval', minutes=20)
scheduler.start()




# for i in x:
#     print(i.movieId)
#     print(i.movieNameFromUrl)
#     print(i.movieNameProcessed)
#     print(i.fetchDateTimes)

