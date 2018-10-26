
from ScrapeBMSFirstTime import GetMovieNameAndIdList
from FileWriter import FileWriter
from GetFirstLevelDetails import GetFirstLevelDetails
seedUrl = 'https://in.bookmyshow.com/national-capital-region-ncr/movies/'
#bookTicketsUrl = 'https://in.bookmyshow.com/buytickets/{}-national-capital-region-ncr/movie-ncr-{}}-MT/{}'
bookTicketsUrl = 'https://in.bookmyshow.com/buytickets/{movieNameFromUrl}-national-capital-region-ncr/movie-ncr-{MovieId}}-MT/{TodaysDate}'
l = GetMovieNameAndIdList(seedUrl)
x= l.GetList()
#print(x)


# for i in x:
#     print(str(i[1]))
# fw = FileWriter()
# fw.WriteScapeBMSFirstTimeFileForListOfMovies(x[0],x[1])

details = GetFirstLevelDetails(seedUrl, x[0])
movieInfoList = details.FillInMovieInfoDetails()

fw = FileWriter()
fw.WriteFirstLevelDetailsToCSV(movieInfoList,x[1])






# for i in x:
#     print(i.movieId)
#     print(i.movieNameFromUrl)
#     print(i.movieNameProcessed)
#     print(i.fetchDateTimes)

