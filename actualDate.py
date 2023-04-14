from datetime import datetime


class CurrentDate:
  
    def __init__(self,):
        self.weakDayList = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.monthNameList = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

    def getYear(self):
        currentYear = int(datetime.now().strftime('%Y'))
        return currentYear
    def getDayNumber(self):
        currentDay = int(datetime.now().strftime('%d'))
        return currentDay
    def getDayName(self):
        dayName=datetime.now().strftime('%A')
        return dayName
    def getMonthNumber(self):
        currentMonthNumber = int(datetime.now().strftime('%m'))
        return currentMonthNumber
    def getMonthName(self):
        numberMont = self.getMonthNumber() 
        currentMonth = self.monthNameList[numberMont]
        return currentMonth
