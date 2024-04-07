import unittest
from ddt import  ddt, data, file_data, unpack
import datetime
import calculate_due_date as dd
from datetime import timedelta, datetime
from unittest.mock import MagicMock

THIS_WEEK_MONDAY = datetime.today() - timedelta(days=datetime.today().weekday())
THIS_WEEK_MONDAY = THIS_WEEK_MONDAY.replace(hour=0, minute=0, second=0, microsecond=0)

MONDAY, TUESDAY, WEDNESDAY, FRIDAY = 0, 1, 2, 4
WEEK_0, WEEK_1, WEEK_2 = 0, 1, 2

WORK_DAYS = [0,1,2,3,4]
WORK_HOURS= [9,10,11,12,13,14,15,16]

def get_time(week, day, hour, minute):
    days = week * 7 + day
    return THIS_WEEK_MONDAY + timedelta(days=days, hours=hour, minutes=minute)
    
@ddt
class TestDueDateCalculator(unittest.TestCase):
    @unpack
    @data(
        {
            'test_case': 'Turnaround time is zero, due date is submit time',
            'submit_time': get_time(WEEK_0, MONDAY, 9, 0),
            'turnaround_time': 0,
            'expected_due_date': get_time(WEEK_0, MONDAY, 9, 0)
        },
        {
            'test_case': 'Turnaround time is one hour, due date is submit time plus one hour',
            'submit_time': get_time(WEEK_0, MONDAY, 9, 0),
            'turnaround_time': 1,
            'expected_due_date': get_time(WEEK_0, MONDAY, 10, 0)
        },
        {
            'test_case': 'Turnaround time one hour due date is the next day 10 am',
            'submit_time': get_time(WEEK_0, MONDAY, 16, 0),
            'turnaround_time': 1,
            'expected_due_date': get_time(WEEK_0, TUESDAY, 9, 0)
        },
        {
            'test_case': 'Turnaround time one hour due date is the next week monday 10 am',
            'submit_time': get_time(WEEK_0, FRIDAY, 17, 0),
            'turnaround_time': 1,
            'expected_due_date': get_time(WEEK_1, MONDAY, 10, 0)
        },
        {
            'test_case': 'Turnaround time one hour due date is the same day 10 am',
            'submit_time': get_time(WEEK_0, MONDAY, 7, 0),
            'turnaround_time': 1,
            'expected_due_date': get_time(WEEK_0, MONDAY, 10, 0)
        },
        {
            'test_case': 'Turnaround time eighteen hours due date is two weeks later monday 9 am',
            'submit_time': get_time(WEEK_0, MONDAY, 9, 0),
            'turnaround_time': 80,
            'expected_due_date': get_time(WEEK_2, MONDAY, 9, 0)
        }
     )
    
    def test_due_date_calculation(self, test_case, submit_time, turnaround_time, expected_due_date):
        holiday_sdk_mock = MagicMock()
        holiday_sdk_mock.is_holiday.return_value = False
        myCalculator = dd.CalculatorClass(WORK_DAYS, WORK_HOURS, holiday_sdk_mock)
        due_date = myCalculator.calculate_due_date(submit_time, turnaround_time)
        self.assertEqual(expected_due_date, due_date, msg=test_case)
        
    def test_due_date_calculator_is_configurable(self):
        holiday_sdk_mock = MagicMock()
        holiday_sdk_mock.is_holiday.return_value = False
        myCalculator = dd.CalculatorClass([0], [2,3], holiday_sdk_mock)
        due_date = myCalculator.calculate_due_date(get_time(WEEK_0, MONDAY, 0, 0), 4)
        self.assertEqual(get_time(WEEK_2, MONDAY, 2, 0), due_date)
        
    def test_due_date_calculator_is_not_holiday(self):
        holiday_sdk_mock = MagicMock()
        holiday_sdk_mock.is_holiday.return_value = False
        myCalculator = dd.CalculatorClass(WORK_DAYS, WORK_HOURS, holiday_sdk_mock)
        due_date = myCalculator.calculate_due_date(get_time(WEEK_0, MONDAY, 12, 0), 0)
        self.assertEqual(get_time(WEEK_0, MONDAY, 12, 0), due_date)
        holiday_sdk_mock.is_holiday.assert_called_with(get_time(WEEK_0, MONDAY, 12, 0))
    
    def test_due_date_calculator_is_holiday(self):
        holiday_sdk_mock = MagicMock()
        holiday_sdk_mock.is_holiday.side_effect = [True, True, False]
        myCalculator = dd.CalculatorClass(WORK_DAYS, [9], holiday_sdk_mock)
        due_date = myCalculator.calculate_due_date(get_time(WEEK_0, MONDAY, 9, 0), 0)
        self.assertEqual(get_time(WEEK_0, WEDNESDAY, 9, 0), due_date)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)