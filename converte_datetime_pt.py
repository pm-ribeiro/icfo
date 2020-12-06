# Créditos
# https://gist.github.com/turicas/8832723

# coding: utf-8

import datetime

MONTHS = {
            'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,  'mai': 5,  'jun': 6,
            'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12
        }
FULL_MONTHS = {
                'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
                'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
                'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12
            }

def parse_pt_date(date_string):
    '''Parses a date-time string and return datetime object
        The format is like this:
        'Seg, 21 Out 2013 22:14:36 -0200'
    '''
    date_info = date_string.lower().split()
    if date_info.count('de') == 2 or len(date_info) == 3:
        if ',' in date_info[0]:
            date_string = date_string.split(',')[1]
        date_info = date_string.lower().replace('de ', '').split()
        day, month_pt, year = date_info
        if len(month_pt) == 3:
            month = MONTHS[month_pt]
        else:
            month = FULL_MONTHS[month_pt]
        date_iso = '{}-{:02d}-{:02d}'.format(year, int(month), int(day))
        date_object = datetime.datetime.strptime(date_iso, '%Y-%m-%d')
        return date_object
    else:
        _, day, month_pt, year, hour_minute_second, offset = date_info

        if offset.lower() == 'gmt':
            offset = '+0000'
        offset_signal = int(offset[0] + '1')
        offset_hours = int(offset[1:3])
        offset_minutes = int(offset[3:5])
        total_offset_seconds = offset_signal * (offset_hours * 3600 +
                                                offset_minutes * 60)
        offset_in_days = total_offset_seconds / (3600.0 * 24)

        month = MONTHS[month_pt]
        datetime_iso = '{}-{:02d}-{:02d}T{}'.format(year, month, int(day),
                hour_minute_second)
        datetime_object = datetime.datetime.strptime(datetime_iso,
                '%Y-%m-%dT%H:%M:%S')
        return datetime_object - datetime.timedelta(offset_in_days)

# TESTS
# if __name__ == '__main__':
#     assert parse_pt_date('Seg, 21 Out 2013 21:14:36 -0200') == \
#             datetime.datetime(2013, 10, 21, 23, 14, 36)

#     assert parse_pt_date(u'terça-feira, 9 de outubro de 2012') == \
#             datetime.datetime(2012, 10, 9, 0, 0, 0)

#     assert parse_pt_date(u'Ter, 31 Jul 2012 16:54:00 GMT') == \
#             datetime.datetime(2012, 7, 31, 16, 54, 0)

#     assert parse_pt_date('23 Abr 2008') == \
#             datetime.datetime(2008, 4, 23, 0, 0, 0)

#     assert parse_pt_date('23 de Dezembro de 2013') == \
#             datetime.datetime(2013, 12, 23, 0, 0, 0)
