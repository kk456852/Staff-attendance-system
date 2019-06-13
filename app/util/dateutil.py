from datetime import date, time, datetime, timedelta


def date_to_datetime(dt: date):
    return datetime(dt.year, dt.month, dt.day)
