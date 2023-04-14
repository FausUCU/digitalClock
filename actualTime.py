from datetime import datetime
class Time:
    def getHour():
        currentTime = datetime.now().strftime('%H')
        return currentTime
    def getMinute():
        currentTime = datetime.now().strftime('%M')
        return currentTime
    def getSecond():
        currentTime = datetime.now().strftime('%S')
        return currentTime
