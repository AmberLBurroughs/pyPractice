# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#
def isLeapYear(year):
    # from Wikipedia:
    #   if year modulo 400 is 0 then
    #       is_leap_year
    #   else if year modulo 100 is 0 then
    #       not_leap_year
    #   else if year modulo 4 is 0 then
    #       is_leap_year
    #   else
    #       not_leap_year
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

    isLeapYear(2000)
    isLeapYear(2016)
    isLeapYear(2120)



def daysInMonth(year, month):
    if month in (1,3,5,7,8,10,12)
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30
    return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    year, month, day = year1, month1, day1
    days = 0
    while year < year2 or month < month2 or day < day2
        year, month, day = nextDay(year, month, day)
        days += 1
    return days
def mytest():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 10, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    print 'test finished.'

mytest()

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

