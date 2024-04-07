import os
from datetime import timedelta, datetime

class CalculatorClass:
    def __init__(self, WORK_DAYS, WORK_HOURS, holiday_sdk):
        self.WORK_HOURS = WORK_HOURS
        self.WORK_DAYS = WORK_DAYS
        self.holiday_sdk = holiday_sdk
        pass
    
    def _is_weekday(self,due_date):
        return due_date.weekday() in self.WORK_DAYS

    def _is_workhours(self,due_date):
        return due_date.hour in self.WORK_HOURS

    def _is_work(self,due_date):
        return self._is_workhours(due_date) and self._is_weekday(due_date) and not self.holiday_sdk.is_holiday(due_date) 

    def calculate_due_date(self, start_date, sla):
        due_date=start_date
        while True:
            if self._is_work(due_date):
                if sla == 0: 
                    return due_date
                else:
                    sla-=1
            due_date+=timedelta(hours=1)