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

class MultiPlexDetails:
    name=None
    id=None
    latitude=None
    longitude=None
    subregion=None
    foodsales=None
    mticket=None
