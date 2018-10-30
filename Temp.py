import datetime as dt
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print("Executing job...")
    print(dt.datetime.now())

scheduler = BlockingScheduler()
scheduler.add_job(job,'interval', seconds=10)
scheduler.start()

# tim = dt.datetime.now()
# #timestamp = tim.strftime('%Y') + '_'+ tim.strftime('%d') +'_'+tim.strftime('%m') +'_'+tim.strftime('%H')
# x = tim.strftime('%M')
# print(type(x))

# y = int(x)

# def GetMinutePart(minutePart):
#     if minutePart <15:
#         return 0
#     if 15<=minutePart <30:
#         return 15
#     if 30<=minutePart <45:
#         return 30
#     if 45<=minutePart <59:
#         return 45


# #fetchDate = dt.datetime(int(tim.strftime('%Y')),int(tim.strftime('%m')),int(tim.strftime('%d')),int(tim.strftime('%H')),GetMinutePart(y))
# print(tim.strftime('%Y') + tim.strftime('%m') + tim.strftime('%d'))
# #print(tim.strftime('%Y'))
# #print(fetchDate)