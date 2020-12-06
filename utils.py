import re
from dateutil.parser import parse
import converte_datetime_pt
import datetime


def is_date(date_string):
  isDDMMYYYY = False
  ptBr = False

  #DD/MM/YYYY
  try :
    day,month,year = date_string.split('/')
    datetime.datetime(int(year),int(month),int(day))
    isDDMMYYYY = True
  except ValueError :
    isDDMMYYYY = False

  try:
    converte_datetime_pt.parse_pt_date(date_string)
    ptBr = True
  except ValueError :
    ptBr = False

  # se algum for verdade
  if(isDDMMYYYY or ptBr):
    return True
  else:
    return False


def is_time(token):
  '''
    Return whether the string can be interpreted as time.
    :param string: str, string to check for time
    '''
  time_12_hour_pattern = (r'^[01]?[0-9]:([0-5][0-9]:)?([0-5][0-9])$') # OK
  time_hms_pattern = (r'^([0-9]+[hH])?([0-9]+(M|m(in)*))?([0-9]+(S|s(eg)*))?$')
  if(
      re.search(time_12_hour_pattern, token) or
      re.search(time_hms_pattern, token)
    ):
    return True
  else:
    return False


# Tests - Status: OK
# print('Is time:', is_time('12h30min'))
# print('Is date:', is_date('21/01/2020'))
# print('Is date:', is_date('21 de maio de 2020'))