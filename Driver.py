
from ScrapeBMSFirstTime import GetMovieNameAndIdList
from FileWriter import FileWriter
seedUrl = 'https://in.bookmyshow.com/national-capital-region-ncr/movies/'
l = GetMovieNameAndIdList(seedUrl)
x= l.GetList()
fw = FileWriter()
fw.WriteScapeBMSFirstTimeFileForListOfMovies(x[0],x[1])

# for i in x:
#     print(i.movieId)
#     print(i.movieNameFromUrl)
#     print(i.movieNameProcessed)
#     print(i.fetchDateTimes)

