# -*- coding: utf-8 -*-
"""
    File name: Dateparser.py
    Author: Harishankar Chinnathambi
    Created on: Sun Mar 12 15:36:17 2017
    Python Version:2.7.12

"""
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
import calendar


class DateString:

    def __init__(self):
        self.mydate = datetime.now()

    def dateformat(self):
        mydate=self.mydate
        #mydate = self.mydate.replace(tzinfo=pytz.utc)
        #mydate = mydate.astimezone(pytz.timezone)
        return mydate

    def to_day(self):
        mydate1 = self.dateformat()
        mydate = mydate1.strftime('%Y-%m-%d')
        return mydate
        
    def tmrw(self, days):
        mydate = self.dateformat()
        mydate = mydate + dt.timedelta(days)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def ystr(self, days):
        mydate = self.dateformat()
        mydate = mydate - dt.timedelta(days)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def eom(self):
        mydate = self.dateformat()
        year = mydate.year
        month = mydate.month
        end = calendar.monthrange(year, month)
        end_day = end[1]
        mydate = str(datetime(year, month, end_day))
        mydate = mydate[:10]
        return mydate
        
    def format1(self, days):
        mydate = self.dateformat()
        mydate1 = mydate + dt.timedelta(days)
        mydate = mydate + dt.timedelta(1)
        mydate = mydate.strftime('%Y-%m-%d')
        mydate1 = mydate1.strftime('%Y-%m-%d')
        return mydate, mydate1
          
    def format2(self):
        mydate = self.dateformat()
        mydate = mydate + relativedelta(months=1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
       
    def format3(self):
        mydate = self.dateformat()
        mydate = mydate + relativedelta(years=1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate

    def format4(self):
        mydate = self.dateformat()
        mydate = mydate - relativedelta(months=1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def format5(self):
        mydate = self.dateformat()
        mydate = mydate - relativedelta(years=1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
       
    def format6(self):
        mydate = self.dateformat()
        year = mydate.year
        mydate = datetime(year, 1, 1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate

    def format7(self):
        mydate = self.dateformat()
        year = mydate.year
        mydate = datetime(year, 4, 1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def format8(self):
        mydate = self.dateformat()
        year = mydate.year
        mydate = datetime(year, 7, 1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def format9(self):
        mydate = self.dateformat()
        year = mydate.year
        mydate = datetime(year, 10, 1)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
    
    def format10(self):
        mydate = self.dateformat()
        mydate = mydate - relativedelta(days=7)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
        
    def format11(self):
        mydate = self.dateformat()
        weekday = mydate.weekday()
        mydate1 = mydate - dt.timedelta(days=weekday)
        mydate = mydate1.strftime('%Y-%m-%d')
        return mydate
        
    def format12(self):
        mydate = self.dateformat()
        weekday = mydate.weekday()
        mydate1 = mydate - dt.timedelta(days=weekday)
        mydate = mydate1 + dt.timedelta(days=7)
        mydate = mydate.strftime('%Y-%m-%d')
        return mydate
               
    def format21(self, month):
        mydate = self.dateformat()
        year = mydate.year
        date1 = mydate.day
        mydate1 = datetime(year, month, date1)
        mydate1 = mydate1.strftime('%Y-%m-%d')
        return mydate1
                     
    def format23(self, dayvalue):
        mydate = self.dateformat()
        weekday = mydate.weekday()
        mydate1 = mydate - dt.timedelta(days=weekday)
        mydate2 = mydate1+dt.timedelta(dayvalue)
        mydate2 = mydate2.strftime('%Y-%m-%d')
        return mydate2
        
        
class TimeString(DateString):
    
    def __init__(self):
        self.mydate = datetime.utcnow()
        
    def time_0(self):
        mydate1 = self.dateformat()
        mytime = '{:%H:%M:%S}'.format(mydate1)
        return mytime
    
    def time1(self):
        mydate1 = self.dateformat()
        mytime = '{:%H:%M:%S}'.format(mydate1)
        return mytime
        
    def time2(self):
        mydate1 = self.dateformat()
        mytime = mydate1 + dt.timedelta(hours=1)
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime
        
    def format13(self):
        time = "12pm"
        mytime = datetime.strptime(time, '%I%p')
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime
                 
    def format14(self):
        mydate = self.dateformat()
        mytime = mydate + dt.timedelta(hours=2)
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime
        
    def format15(self):
        mydate = self.dateformat()
        mytime = mydate + dt.timedelta(minutes=30)
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime        

    def format39(self):
        mydate = self.dateformat()
        mytime = mydate + dt.timedelta(minutes=15)
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime
        
    def format16(self):
        mytime1 = "6:00:00"
        mytime2 = "12:00:00"
        return mytime1, mytime2
        
    def format17(self):
        mytime1 = "18:00:00"
        mytime2 = "00:00:00"
        return mytime1, mytime2
        
    def format18(self):
        mytime1 = "12:00:00"
        mytime2 = "14:00:00"
        return mytime1, mytime2
        
    def format19(self):
        mytime1 = "20:00:00"
        mytime2 = "00:00:00"
        return mytime1, mytime2
    
    def format20(self):
        mytime1 = '13:00:00'
        mytime2 = '17:00:00'
        return mytime1, mytime2
        
    def format22(self, time):
        mytime = datetime.strptime(time, '%I%p')
        mytime = '{:%H:%M:%S}'.format(mytime)
        return mytime