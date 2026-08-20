from datetime import datetime

from datetime import datetime


class Time:
    @staticmethod
    def get_day():
        return datetime.now().day

    @staticmethod
    def get_month():
        return datetime.now().month

    @staticmethod
    def get_year():
        return datetime.now().year

    @staticmethod
    def get_hour():
        return datetime.now().hour

    @staticmethod
    def get_minute():
        return datetime.now().minute

    @staticmethod
    def get_second():
        return datetime.now().second

    @staticmethod
    def get_date():
        return datetime.now().strftime("%d/%m/%Y")

    @staticmethod
    def get_time():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def get_datetime():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    def get_weekday():
        return datetime.now().weekday()