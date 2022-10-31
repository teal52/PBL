import datetime


def get_timer():
    now = datetime.datetime.now()

    hour = f'{now.hour:02}'
    minute = f'{now.minute:02}'
    second = f'{now.second:02}'

    now_text={
        "hour":hour,
        "minute":minute,
        "second":second,
    }
    return now_text