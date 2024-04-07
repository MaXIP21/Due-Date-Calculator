from datetime import datetime, timedelta

class DateCaluclatorClass:
    def __init__(self, CURRENT_DATE=datetime.today()):
        self.CURRENT_DATE=CURRENT_DATE
        pass
    
    @classmethod
    def year_delta(self, years):
        """
        Calculate year delta from the current year
        """
        return self.input_date.year+years
    
    @classmethod
    def shift_left(self, MONTH_LIST):
        """
        Shifts date list left with one step
        """
        return MONTH_LIST[1:]+MONTH_LIST[:1]
    
    @classmethod    
    def shift_right(self, MONTH_LIST):
        """
        Shifts date list right with one step
        """
        return MONTH_LIST[-1:]+MONTH_LIST[:-1]
    
    @classmethod 
    def roll_date(self, MONTH_LIST, STEPS):
        """
        Shifting the month list left or right also calculates the year offset and returns it as year delta.
        """
        YEAR_DELTA=0
        for iterations in range(abs(STEPS)):
            if(STEPS < 0):
                if MONTH_LIST[0] == 1:
                    YEAR_DELTA-=1
                MONTH_LIST=self.shift_right(MONTH_LIST)
            elif(STEPS > 0):
                if MONTH_LIST[0] == 12:
                    YEAR_DELTA+=1
                MONTH_LIST=self.shift_left(MONTH_LIST)
        return MONTH_LIST, YEAR_DELTA
    
    @classmethod
    def get_ordered_month_list(self):
        """
        Sets up month list to start with the current month
        """
        MONTHS=[1,2,3,4,5,6,7,8,9,10,11,12]
        n=MONTHS.index(self.input_date.month)
        return MONTHS[n:]+MONTHS[:n]
        
    @classmethod
    def calculateDelta(self, month_offset):
        """
        Calculate delta from the input date
        """
        CURRENT_LIST=self.get_ordered_month_list()
        MONTH_LIST, YEAR_DELTA = self.roll_date(CURRENT_LIST, month_offset)
        return MONTH_LIST[0], self.year_delta(YEAR_DELTA)
    
    @classmethod
    def set_input_date(self, start_date):
        """
        Set the date give in the arguments as the input date of the Class.
        """
        self.input_date=start_date
        
    @classmethod
    def get_previous_month(self, month_offset, start_date):
        """
        Returns the previous month in datetime Object, also takes care about the year changes.
        """
        CALCULATED_MONTH, CALCULATED_YEAR =self.calculateDelta(month_offset)
        return start_date.replace(year=CALCULATED_YEAR, month=CALCULATED_MONTH)
    
    @classmethod
    def get_day_of_current_week(self, start_date, weekday):
        DOW = {'MON':0, 'TUE':1, 'WED':2, 'THU':3, 'FRI':4, 'SAT':5, 'SUN':6 }
        return start_date - timedelta(days=start_date.weekday()+DOW[weekday])
    
    def calculate_target_date(
        self, 
        start_date, 
        day_offset, 
        week_offset, 
        month_offset, 
        hour_offset = 0, 
        minute_offset = 0, 
        second_offset = 0, 
        day_of_week = None,
        return_type=datetime
    ):
        while True:
            try:
                self.set_input_date(start_date)
                start_date=self.get_previous_month(month_offset, start_date)
                
                if day_of_week != None:
                    #print(start_date)
                    start_date=self.get_day_of_current_week(start_date, day_of_week)
                    #print(start_date)
                if return_type=="timestamp" or return_type=="unixtime":
                    return (
                        start_date+timedelta(
                            days=day_offset, 
                            weeks=week_offset, 
                            hours=hour_offset, 
                            minutes=minute_offset, 
                            seconds=second_offset
                        )
                    ).timestamp()
                else:
                    return start_date+timedelta(
                        days=day_offset, 
                        weeks=week_offset, 
                        hours=hour_offset, 
                        minutes=minute_offset, 
                        seconds=second_offset
                    )
            except ValueError as e:
                start_date=start_date-timedelta(days=1)
    
    
        