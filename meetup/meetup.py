import calendar
from datetime import date


def _day_of_the_week_to_index(day_of_the_week):
    """Convert weekday in string format to index, e.g. Monday to 0"""
    _day_abbr = list(calendar.day_abbr)
    return _day_abbr.index(day_of_the_week[:3])


def _ordinal_to_index(ordinal):
    """Convert ordinal number to index."""
    if ordinal == '1st':
        idx = 0
    elif ordinal == '2nd':
        idx = 1
    elif ordinal == '3rd':
        idx = 2
    elif ordinal == '4th':
        idx = 3
    elif ordinal == '5th':
        idx = 4
    elif ordinal == 'last':
        idx = -1
    else:
        raise ValueError("Invalid date descriptor.")

    return idx


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_of_the_week, which):
    # Now we have day_of_the_weeky in int, e.g. "Monday" is 0
    weekday = _day_of_the_week_to_index(day_of_the_week)

    if which == 'teenth':
        # Get the weekdays from 13th to 19th
        teenth_weekdays = []
        for day in range(13, 20):
            teenth_weekdays.append(date(year, month, day).weekday())

        result_day = 13 + teenth_weekdays.index(weekday)
    else:
        mc = calendar.monthcalendar(year, month)

        # Get a column of days with the same day of the week
        weekday_column = [mc[week][weekday]
                          for week in range(len(mc))
                          if mc[week][weekday] != 0]

        try:
            result_day = weekday_column[_ordinal_to_index(which)]
        except IndexError:
            raise MeetupDayException("Nonexistent date.")
        except ValueError:
            raise MeetupDayException("Invalid date descriptor.")

    return date(year, month, result_day)
