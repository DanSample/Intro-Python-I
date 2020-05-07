"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def print_cal(month=None, year=None):
  if month is None and year is None:
    year, month = [datetime.now().year, datetime.now().month]
    calendar.prmonth(year,month)
  elif year is None:
    year = datetime.now().year
    calendar.prmonth(year, month)
  else:
    calendar.prmonth(year, month)
  

def process_msg():
    usage_msg = "\nNAME\n\t14_cal.py -- a simple calendar tool\n\n"
    usage_msg += "USAGE\n\tpython 14_cal.py [month [year]]\n\n"
    usage_msg += "DESCRIPTION\n\t"
    desc = """If no arguments are passed, the current month's calendar will 
        be printed. If one argument is passed, the corresponding month 
        will be printed for the current year. If two arguments are 
        passed, then the month for given month and year will be printed.\n"""
    usage_msg += desc
    print(usage_msg)
    exit(1)

def process_args(*args):
  script_name, *args = sys.argv
  if not args:
    print_cal()
  elif len(args) == 1:
    month = int(args[0])
    print_cal(month)
  elif len(args) == 2:
    month, year = map(int, args)
    print_cal(year, month)
  else:
    process_msg()    


if __name__ == "__main__":
    process_args(*sys.argv)