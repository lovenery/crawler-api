from datetime import datetime, timedelta
from random import randint

def time():
    # https://docs.python.org/3/library/datetime.html#datetime-objects
    # https://blog.liang2.tw/posts/2015/09/datetime-sqlite/
    now = datetime.utcnow()
    now = now + timedelta(hours=8)
    code = ''
    h = now.hour # 0 <= hour < 24
    m = now.minute # 0 <= minute < 60
    if m <= 15 or m >= 45:
        if h == 1 or h == 13:
            code = '0x1F550'
        elif h == 2 or h == 14:
            code = '0x1F551'
        elif h == 3 or h == 15:
            code = '0x1F552'
        elif h == 4 or h == 16:
            code = '0x1F553'
        elif h == 5 or h == 17:
            code = '0x1F554'
        elif h == 6 or h == 18:
            code = '0x1F555'
        elif h == 7 or h == 19:
            code = '0x1F556'
        elif h == 8 or h == 20:
            code = '0x1F557'
        elif h == 9 or h == 21:
            code = '0x1F558'
        elif h == 10 or h == 22:
            code = '0x1F559'
        elif h == 11 or h == 23:
            code = '0x1F55A'
        elif h == 0 or h == 12:
            code = '0x1F55B'
    else:
        if h == 1 or h == 13:
            code = '0x1F55C'
        elif h == 2 or h == 14:
            code = '0x1F55D'
        elif h == 3 or h == 15:
            code = '0x1F55E'
        elif h == 4 or h == 16:
            code = '0x1F55F'
        elif h == 5 or h == 17:
            code = '0x1F560'
        elif h == 6 or h == 18:
            code = '0x1F561'
        elif h == 7 or h == 19:
            code = '0x1F562'
        elif h == 8 or h == 20:
            code = '0x1F563'
        elif h == 9 or h == 21:
            code = '0x1F564'
        elif h == 10 or h == 22:
            code = '0x1F565'
        elif h == 11 or h == 23:
            code = '0x1F566'
        elif h == 0 or h == 12:
            code = '0x1F567'

    return now, code

def fruit():
    # U+1F345(127813) ~ U+1F353(127827)
    rand = randint(127813, 127827)
    code = hex(rand)
    return code
