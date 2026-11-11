import random
import time
def getRandomDate(startDate,endDate):
    print("printing random date between:", startDate ,"and" , endDate)
    randomGenerator=random.random()
    dateformat="%m/%d/%Y"
    startTime=time.mktime(time.strptime(startDate,dateformat))
    endTime=time.mktime(time.strptime(endDate,dateformat))
    randomTime=startTime + randomGenerator * (endTime-startTime)
    randomDate=time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
print("Random Date =", getRandomDate("6/27/2016","11/10/2026"))