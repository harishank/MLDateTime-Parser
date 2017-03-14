# MLDateTime-Parser
Machine Learning based DateTime string parsing library designed to parse dates and time  from text strings
#Features
Generic Parsing of realtive dates in English like 'today', 'tomorrow', day after tomorrow', noon', 'midday'.
Extensive Test coverage

#Dependencies
MLdateparser relies on following libraries in some ways:
Scikit-learn for classification
dateutil’s module relativedelta for its freshness parser.
pytz module 
numpy
tzlocal to reliably get local timezone.

#Supported languages
English

#Testcases:
Initially this version supports 98 strings and have testcases.py file to test all the strings


#Demo:

>>>import MLDateTimeParser
>>>import MLDateTime as dt
>>>dt.parse("now").
>>>dt.parse("today").
>>>dt.parse("eod")
>>>dt.parse("tomorrow")
>>>dt.parse("day after tomorrow")
>>>dt.parse("day before yesterday")
>>>dt.parse("eom")
>>>dt.parse("1 o\'clock")
