class MovieNameAndId:
    movieNameFromUrl=''
    movieId=''
    movieNameProcessed=''
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
 

class MovieDataOnHourlyBasis:
    movieName=None
    movieHeartRatingPercent=None
    numOfVotes=None
    critics_rating=None
    user_rating=None
    fetchDateTime = None


    