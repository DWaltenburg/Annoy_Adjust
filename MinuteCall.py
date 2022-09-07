from time import gmtime, strftime


def get_minute():
    minute = strftime("%M", gmtime())
    convMin = int(minute)
    if convMin == 0:
        convMin = 1

    volVal = -convMin
    return volVal
