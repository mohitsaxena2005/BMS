import datetime as dt

class HelperFunctions:


    def GetMinutePart(self,minutePart):
        if minutePart <15:
            return 0
        if 15<=minutePart <30:
            return 15
        if 30<=minutePart <45:
            return 30
        if 45<=minutePart <59:
            return 45

    def GetFetchDateTime(self):
        tim = dt.datetime.now()
        x = int(tim.strftime('%M'))
        return dt.datetime(int(tim.strftime('%Y')),int(tim.strftime('%m')),int(tim.strftime('%d')),int(tim.strftime('%H')),self.GetMinutePart(x))
        

