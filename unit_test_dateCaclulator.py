import unittest
from ddt import ddt, data, unpack, file_data, unpack
from datetime import datetime, timedelta
import datecalculator as datec
import numpy

NEW_YEARS_EVE_THIS_YEAR=datetime.today().replace(2022,1,1,0,0,0,0)
MONTHS=[1,2,3,4,5,6,7,8,9,10,11,12]

## Helper functions
def monthDelta(months):
    n=MONTHS.index(NEW_YEARS_EVE_THIS_YEAR.month)
    CURRENT_LIST=MONTHS[n:]+MONTHS[:n]
    return numpy.roll(CURRENT_LIST,months*-1)[0]

def get_date(months, week, day, hour, minute):
    RETURN_DAY=NEW_YEARS_EVE_THIS_YEAR+timedelta(weeks=week, days=day, hours=hour, minutes=minute)
    return RETURN_DAY.replace(month=monthDelta(months))
    
MONTH1, MONTH2, MONTH3, MONTH4 = 1,2,3,4
WEEK0, WEEK1, WEEK2, WEEK3= 0,1,2,3
DAY0, DAY1, DAY2, DAY3, DAY4, DAY5, DAY6 = 0,1,2,3,4,5,6

@ddt
class datetimeTest(unittest.TestCase):
    @unpack
    @data(
        {
            'test_case':'Return time equals the submitted datetime',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':0,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK0, DAY0, 0, 0)
        }, 
        {
            'test_case':'Return time equals the submitted datetime plus one day',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':1,
            'week_offset':0,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK0, DAY1, 0, 0)
        }, 
        {
            'test_case':'Return time equals the submitted datetime minus one day',
            'current_datetime':get_date(0, WEEK1, DAY0, 0, 0), 
            'day_offset':-1,
            'week_offset':0,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK0, DAY6, 0, 0)
        },
        {
            'test_case':'Return time equals the submitted datetime plus one week',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':1,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK1, DAY0, 0, 0)
        },
        {
            'test_case':'Return time equals the submitted datetime minus one week',
            'current_datetime':get_date(0, WEEK1, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':-1,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK0, DAY0, 0, 0)
        }, 
        {
            'test_case':'Return datetime is two week later submitted time plus fourteen days',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':14,
            'week_offset':0,
            'month_offset':0,
            'expected_datetime':get_date(0, WEEK2, DAY0, 0, 0)
        }, 
        {
            'test_case':'Returned datetime is one month before',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':0,
            'month_offset':-1,
            'expected_datetime':datetime.today().replace(2021,12,1,0,0,0,0)
        }, 
        {
            'test_case':'Returned datetime is one year before',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':-12,
            'expected_datetime':datetime.today().replace(2021,1,1,0,0,0,0)
        }, 
        {
            'test_case':'Returned datetime is two year before parameters -12 months',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':-24,
            'expected_datetime':datetime.today().replace(2020,1,1,0,0,0,0)
        }, 
        {
            'test_case':'Returned datetime is two year before parameters -12 months',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':24,
            'expected_datetime':datetime.today().replace(2024,1,1,0,0,0,0)
        }, 
        {
            'test_case':'Testing leap year',
            'current_datetime':datetime.today().replace(2020,2,29,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':12,
            'expected_datetime':datetime.today().replace(2021,2,28,0,0,0,0)
        }
    )
    def test_date_caluclation(self, current_datetime, expected_datetime, test_case, day_offset, week_offset, month_offset):
        dateCalculator=datec.DateCaluclatorClass()
        targetDate=dateCalculator.calculate_target_date(current_datetime, day_offset, week_offset, month_offset)
        self.assertEqual(expected_datetime, targetDate, msg=test_case)
    
    @unpack
    @data(
        {
            'test_case':'Return time equals the submitted datetime',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':0,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'timestamp',
            'expected_datetime':get_date(0, WEEK0, DAY0, 0, 0).timestamp()
        }, 
        {
            'test_case':'Return time equals the submitted datetime plus one day',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':1,
            'week_offset':0,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK0, DAY1, 0, 0).timestamp()
        }, 
        {
            'test_case':'Return time equals the submitted datetime minus one day',
            'current_datetime':get_date(0, WEEK1, DAY0, 0, 0), 
            'day_offset':-1,
            'week_offset':0,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK0, DAY6, 0, 0).timestamp()
        },
        {
            'test_case':'Return time equals the submitted datetime plus one week',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':1,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK1, DAY0, 0, 0).timestamp()
        },
        {
            'test_case':'Return time equals the submitted datetime minus one week',
            'current_datetime':get_date(0, WEEK1, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':-1,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK0, DAY0, 0, 0).timestamp()
        }, 
        {
            'test_case':'Return datetime is two week later submitted time plus fourteen days',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':14,
            'week_offset':0,
            'month_offset':0,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK2, DAY0, 0, 0).timestamp()
        }, 
        {
            'test_case':'Returned datetime is one month before',
            'current_datetime':get_date(0, WEEK0, DAY0, 0, 0), 
            'day_offset':0,
            'week_offset':0,
            'month_offset':-1,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':datetime.today().replace(2021,12,1,0,0,0,0).timestamp()
        }, 
        {
            'test_case':'Returned datetime is one year before',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':-12,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':datetime.today().replace(2021,1,1,0,0,0,0).timestamp()
        }, 
        {
            'test_case':'Returned datetime is two year before parameters -12 months',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':-24,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':datetime.today().replace(2020,1,1,0,0,0,0).timestamp()
        }, 
        {
            'test_case':'Returned datetime is two year before parameters -12 months',
            'current_datetime':datetime.today().replace(2022,1,1,0,0,0,0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':24,
            'day_of_week': None,
            'return_type':'unixtime',
            'expected_datetime':datetime.today().replace(2024,1,1,0,0,0,0).timestamp()
        },
        {
            'test_case':'Returned datetime the Monday of the same week',
            'current_datetime':get_date(0, WEEK0, DAY1, 0, 0),
            'day_offset':0,
            'week_offset':0,
            'month_offset':0,
            'day_of_week': 'MON', 
            'return_type':'unixtime',
            'expected_datetime':get_date(0, WEEK0, DAY0, 0, 0).timestamp()
        }
    )
    def test_date_caluclation_in_unix_time(self, current_datetime, expected_datetime, test_case, day_offset, week_offset, month_offset, day_of_week, return_type):
        dateCalculator=datec.DateCaluclatorClass()
        targetDate=dateCalculator.calculate_target_date(current_datetime, day_offset, week_offset, month_offset, day_of_week=day_of_week,  return_type=return_type)
        self.assertEqual(expected_datetime, targetDate, msg=test_case)
        
    @file_data('test_data_dict.json')
    def test_calendar_rotation(self, test_case, start_month_list, expected_month_list, shift_value, year_offset):
        dateCalculator=datec.DateCaluclatorClass()
        month_list, target_year_offset = dateCalculator.roll_date(start_month_list, shift_value)
        self.assertEqual(expected_month_list, month_list, msg=test_case)
        self.assertEqual(year_offset, target_year_offset, msg=test_case)
        
    @unpack
    @data(
        {
        'test_case':'Test list shifting left',
        'start_list':[0,1,2,3], 
        'expected_list':[1,2,3,0]
        }
    )
    def test_month_rotation_left(self, test_case, start_list, expected_list):
        dateCalculator=datec.DateCaluclatorClass()
        self.assertEqual(expected_list, dateCalculator.shift_left(start_list), msg=test_case)
    @unpack
    @data(
        {
        'test_case':'Test list shifting right',
        'start_list':[0,1,2,3], 
        'expected_list':[3,0,1,2]
        }
    )
    def test_month_rotation_right(self, test_case, start_list, expected_list):
        dateCalculator=datec.DateCaluclatorClass()
        self.assertEqual(expected_list, dateCalculator.shift_right(start_list), msg=test_case)
    
    @unpack
    @data(
        {
        'test_case':'Test if the correct year is set',
        'set_year':2022,
        'expected_year':2022,
        },
        {
        'test_case':'Test if the correct year is set',
        'set_year':2021,
        'expected_year':2021,
        }
    )
    def test_if_configurable(self, test_case, set_year, expected_year):
        dateCalculator=datec.DateCaluclatorClass()
        dateCalculator.set_input_date(datetime.today().replace(set_year,1,1,0,0,0,0))
        self.assertEqual(expected_year, dateCalculator.year_delta(0), msg="Check if the input_date is configurable")
        
    @unpack
    @data(
        {
        'test_case':'Test yearDelta function, result is the same year',
        'start_year':2022, 
        'result_year':2022,
        'offset':0
        },
        {
        'test_case':'Test yearDelta function, result is minus one year',
        'start_year':2022, 
        'result_year':2021,
        'offset':-1
        },
        {
        'test_case':'Test adding one year, result is plus one year',
        'start_year':2022, 
        'result_year':2023,
        'offset':1
        }
    )
    def test_year_offset(self, test_case, start_year, result_year, offset):
        dateCalculator=datec.DateCaluclatorClass()
        dateCalculator.set_input_date(datetime.today().replace(start_year,1,1,0,0,0,0))
        self.assertEqual(result_year, dateCalculator.year_delta(offset), msg=test_case)
        
if __name__ == '__main__':
    unittest.main()