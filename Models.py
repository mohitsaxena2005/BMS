class MovieNameAndId:
    movieNameFromUrl=None
    movieId=None
    movieNameProcessed=None
    fetchDateTime=None
    #firstTimeAppearanceDate='' Have this column in the DB table when the 
    #lastTimeAppearanceDate=''

    def __init__(self, name, id, fetchTime):
        self.movieId = id
        self.movieNameFromUrl = name
        self.movieNameProcessed = name.replace('-',' ')
        self.fetchDateTime = fetchTime

    def __iter__(self):
        return iter([self.movieId, self.movieNameFromUrl, self.movieNameProcessed, self.fetchDateTime])
 

class MovieInfo:
    movieName=None
    movieNameFromUrl = None
    movieId = None
    movieHeartRatingPercent=None
    numOfVotes=None
    critics_rating=None
    user_rating=None
    fetchDateTime = None
    genre=None
    language=None
    movieUrl=None

    def __iter__(self):
        return iter([self.movieId,self.movieName,self.movieNameFromUrl,self.movieHeartRatingPercent,self.numOfVotes,self.critics_rating,self.user_rating,
        self.fetchDateTime,self.genre,self.language,self.movieUrl])



class ShowVenueInfo:
    VenueFullName=None
    VenueId = None
    VenueRegion=None
    VenueSubRegionName=None
    VenueSubRegionId=None
    VenueLatitude=None
    VenueLongitude=None
    VenueAllowSales=None
    IsVenueApp = None
    IsNewCinema=None
    IsFoodSalesAvailable=None
    IsMultiplex=None
    MessageType=None
    IsFullSeatLayoutAvailable=None
    IsMticketAccepted=None
    HasCOD=None
    HasCOP=None
    FetchDateTime=None

    def __iter__(self):
        return iter([self.VenueId,self.VenueFullName,self.VenueRegion,self.VenueSubRegionName,self.VenueSubRegionId,
        self.VenueLatitude,self.VenueLongitude,self.VenueAllowSales,self.IsVenueApp,self.IsNewCinema,
        self.IsFoodSalesAvailable,self.IsMultiplex,self.MessageType,self.IsFullSeatLayoutAvailable,self.IsMticketAccepted,self.HasCOD,
        self.HasCOP,self.FetchDateTime])


class MovieShowTimeInfo:
    multiplexName=None
    multiplexId=None
    availableSeatsPercent=None
    fetchDateTime=None
    seatClass=None
    seatPrice=None
    seatAvailabilityText=None
    showTime=None
    cutOffTime=None
    showTimeType=None
    fetchDateTime=None
    isAtmosEnabled=None
    
    def __iter__(self):
        return iter([self.multiplexId,self.multiplexName,self.availableSeatsPercent,self.fetchDateTime,self.seatClass,
        self.seatPrice,self.seatAvailabilityText,self.showTime,self.cutOffTime,self.showTimeType,
        self.fetchDateTime,self.isAtmosEnabled])
