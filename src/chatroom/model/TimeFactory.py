from datetime import datetime


class TimeFactory:
    Now = lambda: datetime.now()
