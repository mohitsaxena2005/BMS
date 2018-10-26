import csv

class FileWriter:
    def WriteScapeBMSFirstTimeFileForListOfMovies(self,movieData,datetimeStamp):
        fileName = 'movieData_' + str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        with open(fileName, 'w') as csvFile:
            writer = csv.writer(csvFile)
            for row in movieData:
                writer.writerow(list(row))


