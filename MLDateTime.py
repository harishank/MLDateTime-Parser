# -*- coding: utf-8 -*-
"""
    File name: MLDateTime.py
    Author: Harishankar Chinnathambi
    Created on: Sun Mar 12 15:36:17 2017
    Python Version:2.7.12

"""


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import DateParser as dp


bigram_vectorizer = CountVectorizer(ngram_range=(1,2), 
                                    token_pattern=r'\b\w+\b', min_df=0)

corpus = ['now', 'today', 'eod', 'tomorrow', 'day after tomorrow', 'yesterday\
', 'day before yesterday', 'eom', 'next few days', 'next month', 'next year','\
last month', 'last year', 'this year', 'first quarter', 'second quarter', 'thi\
rd quarter', 'fourth quarter', 'a week ago', 'one week ago', 'current week', '\
coming week', 'last week', 'next week', 'noon', 'midday', 'in a couple of hour\
s', 'in a few hours', 'half an hour', 'in about half an hour', 'morning', 'eve\
ning', 'lunch','night', 'in 24 hours', 'in 24 hrs', 'after lunch', 'in one hou\
r', 'in an hour', '15 minutes from now', 'in 1 hour','harish', '1 am', '2 am', 
'3 am', '4 am', '5 am', '6 am', '7 am', '8 am', '9 am', '10 am', '11 am', '12 \
am', '1 pm', '2 pm', '3 pm', '4 pm', '5 pm', '6 pm', '7 pm', '8 pm', '9 pm', '\
10 pm', '11 pm', '12 pm','sunday', 'monday', 'tuesday', 'wednesday', 'thursday\
', 'friday', 'saturday', 'XXXXVVVVVV', 'january', 'february', 'march', 'april',
'may', 'june', 'july', 'august', 'september', 'october', 'november','december',
'1 o\'clock', '2 o\'clock', '3 o\'clock', '4 o\'clock', '5 o\'clock', '6 o\'cl\
ock', '7 o\'clock', '8 o\'clock', '9 o\'clock', '10 o\'clock', '11 o\'clock', 
'12 o\'clock']
print len(corpus)

X_2 = bigram_vectorizer.fit_transform(corpus).toarray()
np.save("Trainmatrix", X_2)


def parse(text):
    text=text.lower()
    test = bigram_vectorizer.transform([text])
    tst = test.toarray()
    decision = cosine_similarity(tst, X_2)
    n = 0
    for i in range(len(decision[0])):
        if decision[0][i] > 0.7:
            n = i
    #print n
    datestring=datetimeformat(n)
    return datestring
    

def datetimeformat(n):
    date_obj = dp.DateString()
    time_obj = dp.TimeString()
    res = "supports only date time strings"   
    if n == 0:
        res_date = date_obj.to_day()
        res_time = time_obj.time1()
        res = (res_date, res_time)
        
    elif  n == 1 or n == 2 or n == 13:
        res = date_obj.to_day()
    elif n == 3 or n == 34 or n == 35:
        res_date= date_obj.tmrw(days=1)
        res_time = time_obj.time1()
        res = (res_date, res_time)
    elif n == 4:
        res= date_obj.tmrw(days=2)
    elif n == 5:
        res= date_obj.ystr(days=1)
    elif n == 6:
        res= date_obj.ystr(days=2)
    elif n == 7:
        res= date_obj.eom()
    elif n == 8:
        res= date_obj.format1(days=3)
    elif n == 9:
        res= date_obj.format2()
    elif n == 10:
        res= date_obj.format3()
    elif n == 11:
        res= date_obj.format4()
    elif n == 12:
        res= date_obj.format5()
    elif n == 14:
        res= date_obj.format6()
    elif n == 15:
        res= date_obj.format7()
    elif n == 16:
        res= date_obj.format8()
    elif n == 17:
        res= date_obj.format9()
    elif n == 18 or n == 19 or n == 22:
        res= date_obj.format10()
    elif n == 20:
        res= date_obj.format11()
    elif n == 23 or n == 21:
        res= date_obj.format12()
    elif n == 24 or n == 25:
        res= time_obj.format13()
    elif n == 26 or n == 27:
        res=time_obj.format14()
    elif n == 28 or n == 29:
        res= time_obj.format15()
    elif n == 30:
        res= time_obj.format16()
    elif n == 31:
        res= time_obj.format17()
    elif n == 32:
        res= time_obj.format18()
    elif n == 33:
        res= time_obj.format19()
    elif n == 36:
        res= time_obj.format20()
    elif n == 37 or n == 38 or n == 40:
        res= time_obj.time2()
    elif n == 39:
        res= time_obj.format39()
    elif n == 42:
        res= time_obj.format22('1am')
    elif n == 43:
        res= time_obj.format22('2am')
    elif n == 44:
        res= time_obj.format22('3am')
    elif n == 45:
        res= time_obj.format22('4am')
    elif n == 46:
        res= time_obj.format22('5am')
    elif n == 47:
        res= time_obj.format22('6am')
    elif n == 48:
        res= time_obj.format22('7am')
    elif n == 49:
        res= time_obj.format22('8am')
    elif n == 50 or n == 94:
        res= time_obj.format22('9am')
    elif n == 51 or n == 95:
        res= time_obj.format22('10am')
    elif n == 52 or n == 96:
        res= time_obj.format22('11am')
    elif n == 53:
        res= time_obj.format22('12am')
    elif n == 54 or n == 86:
        res= time_obj.format22('1pm')
    elif n == 55 or n == 87:
        res= time_obj.format22('2pm')
    elif n == 56 or n == 88:
        res= time_obj.format22('3pm')
    elif n == 57 or n == 89:
        res= time_obj.format22('4pm')
    elif n == 58 or n == 90:
        res= time_obj.format22('5pm')
    elif n == 59 or n == 91:
        res= time_obj.format22('6pm')
    elif n == 60 or n == 92:
        res= time_obj.format22('7pm')
    elif n == 61 or n == 93:
        res= time_obj.format22('8pm')
    elif n == 62 or n == 94:
        res= time_obj.format22('9pm')
    elif n == 63:
        res= time_obj.format22('10pm')
    elif n == 64:
        res= time_obj.format22('11pm')
    elif n == 65 or n == 97:
        res= time_obj.format22('12pm')
    elif n == 66:
        res= date_obj.format23(6)
    elif n == 67:
        res= date_obj.format23(0)
    elif n == 68:
        res= date_obj.format23(1)
    elif n == 69:
        res= date_obj.format23(2)
    elif n == 70:
        res= date_obj.format23(3)
    elif n == 71:
        res= date_obj.format23(4)
    elif n == 72:
        res= date_obj.format23(5)
    elif n == 74: 
        res= date_obj.format21(1)
    elif n == 75:
        res= date_obj.format21(2)
    elif n == 76:
        res= date_obj.format21(3)
    elif n == 77:
        res= date_obj.format21(4)
    elif n == 78:
        res= date_obj.format21(5)
    elif n == 79:
        res= date_obj.format21(6)
    elif n == 80:
        res= date_obj.format21(7)
    elif n == 81:
        res= date_obj.format21(8)
    elif n == 82:
        res= date_obj.format21(9)
    elif n == 83:
        res= date_obj.format21(10)
    elif n == 84:
        res= date_obj.format21(11)
    elif n == 85:
        res= date_obj.format21(12)   
    return res
    
