class MyTime:
    def __init__(self, *args):
        if not args:
            self.hours, self.minutes, self.seconds = [0, 0, 0]
        elif len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        elif len(args) == 1:
            if isinstance(args[0], str):
                self.hours, self.minutes, self.seconds = map(int, args[0].split('-'))
            elif isinstance(args[0], MyTime):
                self.hours, self.minutes, self.seconds = args[0].hours, args[0].minutes, args[0].seconds

    def __eq__(self, other):
        return all([
            self.hours == other.hours,
            self.minutes == other.minutes,
            self.seconds == other.seconds,
        ])

    def time_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, seconds):
        hours = seconds // 3600
        minutes = seconds // 60 % 60
        seconds = seconds % 60
        return hours, minutes, seconds

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.time_to_seconds() < other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __le__(self, other):
        return self.time_to_seconds() <= other.time_to_seconds()

    def __ge__(self, other):
        return self.time_to_seconds() >= other.time_to_seconds()

    def __add__(self, other):
        total_seconds = self.time_to_seconds() + other.time_to_seconds()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        total_seconds = self.time_to_seconds() - other.time_to_seconds()
        if total_seconds < 0:
            return MyTime()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __mul__(self, number):
        total_seconds = self.time_to_seconds() * number
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __str__(self):
        return f'{self.hours}-{self.minutes}-{self.seconds}'