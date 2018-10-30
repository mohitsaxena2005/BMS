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
        header=['movieId','movieNameFromUrl','movieNameProcessed','fetchDateTime']
        with open(fileName, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(header)
            for key,value in movieData.items():
                writer.writerow(list(value))
    
    def WriteFirstLevelDetailsToCSV(self,movieInfo,datetimeStamp):
        fileName = 'movieInfo_' + str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        header=['movieId','movieName','movieNameFromUrl','movieHeartRatingPercent','numOfVotes','critics_rating','user_rating','fetchDateTime','genre','language','movieUrl']
        with open(fileName, 'w',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(header)
            for row in movieInfo:
                writer.writerow(list(row))


    def WriteVenueList(self, venueInfoList, datetimeStamp):
        fileName = 'venueInfo_' +  str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        header=['VenueId','VenueFullName','VenueRegion','VenueSubRegionName','VenueSubRegionId','VenueLatitude','VenueLongitude','VenueAllowSales',
        'IsVenueApp','IsNewCinema','IsFoodSalesAvailable','IsMultiplex','MessageType','IsFullSeatLayoutAvailable','IsMticketAccepted','HasCOD','HasCOP',
        'FetchDateTime']
        with open(fileName, 'w',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(header)
            for row in venueInfoList:
                writer.writerow(list(row))

    def WriteShowTimeInfoList(self, showTimeInfoList, datetimeStamp):
        fileName = 'showTimeInfo_' +  str(datetimeStamp).replace(' ','').replace(':','_') + '.csv'
        header=['multiplexId','multiplexName','availableSeatsPercent','fetchDateTime','seatClass','seatPrice','seatAvailabilityText','showTime','cutOffTime',
        'showTimeType','fetchDateTime','isAtmosEnabled']
        with open(fileName, 'w',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(header)
            for row in showTimeInfoList:
                writer.writerow(list(row))