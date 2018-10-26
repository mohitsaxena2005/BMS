import re

class RegularExpressionExtractions:

    def ExtractMovieNameAndIdFromUrl(self,l):
        matchObj=re.match('/national-capital-region-ncr/movies/(.*)/(.*)', l,re.M | re.I)
        if matchObj :
            return (matchObj.group(1), matchObj.group(2))
        