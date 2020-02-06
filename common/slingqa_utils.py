import datetime

class utils:
    def __init__(self):
        print("Initializing utils")

    def get_timestamp(self):
        now = datetime.datetime.now()
        now = str(now)
        year = now[:4]
        month = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minute = now[14:16]
        sec = now[17:19]

        time_string = year + '.' + month + '.' + day + '_' + hour + '.' + minute + '.' + sec
        # print time_string
        return time_string
