import datetime, time


class CommonTime():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __gt__(self, r):
        if self.hour > r.hour:
            return True
        elif self.hour == r.hour:
            return self.minute > r.minute
        else:
            return False

    def __eq__(self, r):
        return self.hour == r.hour and self.minute == r.minute

    def __ge__(self, r):
        return self.__gt__(r) or self.__eq__(r)

    def __lt__(self, r):
        return not self.__ge__(r)

    def __le__(self, r):
        return not self.__gt__(r)

    def __ne__(self, r):
        return not self.__eq__(r)

    def __str__(self):
        return "%s:%s" % (self.hour, self.minute)

xu2min_workdays_normal_list = [
    CommonTime(6, 40), CommonTime(7, 0), CommonTime(7, 10),
    CommonTime(7, 30), CommonTime(9, 0), CommonTime(10, 10),
    CommonTime(12, 0,), CommonTime(13, 0), CommonTime(15, 0),
    CommonTime(17, 0), CommonTime(20, 0), CommonTime(21, 30)
]
xu2min_weekends_normal_list = [
    CommonTime(8, 30), CommonTime(13, 30), CommonTime(17, 30)
]
xu2min_workdays_vacation_list = [
    CommonTime(7, 30), CommonTime(8, 30), CommonTime(13, 15),
    CommonTime(16, 30), CommonTime(21, 0)
]
xu2min_weekends_vacation_list = [
    CommonTime(8, 30), CommonTime(17, 30)
]
min2xu_workdays_normal_list = [
    CommonTime(6, 40), CommonTime(8, 0), CommonTime(10, 10),
    CommonTime(12, 15), CommonTime(14, 10), CommonTime(16, 0),
    CommonTime(17, 0), CommonTime(18, 30), CommonTime(20, 40)
]
min2xu_weekends_normal_list = [
    CommonTime(7, 30), CommonTime(12, 30), CommonTime(16, 30)
]
min2xu_workdays_vacation_list = [
    CommonTime(7, 30), CommonTime(12, 15), CommonTime(16, 30),
    CommonTime(17, 30), CommonTime(20, 0)
]
min2xu_weekends_vacation_list = [
    CommonTime(7, 30), CommonTime(16,30)
]
