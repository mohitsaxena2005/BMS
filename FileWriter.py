import csv

class FileWriter:
    # def WriteScapeBMSFirstTimeFileForListOfMovies(self,movieData,datetimeStamp):
    #     fileName = 'movieData_' + str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
    #     with open(fileName, 'w') as csvFile:
    #         writer = csv.writer(csvFile)
    #         for row in movieData:
    #             writer.writerow(list(row))

    def WriteScapeBMSFirstTimeFileForListOfMovies(self,movieData,datetimeStamp):
        fileName = 'movieData_' + str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        with open(fileName, 'w') as csvFile:
            writer = csv.writer(csvFile)
            for key,value in movieData.items():
                writer.writerow(list(value))
    
    def WriteFirstLevelDetailsToCSV(self,movieInfo,datetimeStamp):
        fileName = 'movieInfo_' + str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        with open(fileName, 'w') as csvFile:
            writer = csv.writer(csvFile)
            for row in movieInfo:
                writer.writerow(list(row))


