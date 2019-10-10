def convertTime(time):
    #add a 0 if string is not long enough
    if len(time) < 6:
        newTime = '0' + time
        return newTime
    else:
        return time

def convertDate(date):
    # add a 0 if string is not long enough
    if len(date) < 8:
        newDate = '0' + date
        return formatDate(newDate)
    else:
        return formatDate(date)

def formatDate(str):
    #re-order the date format
    year = str[4:8]
    month = str[2:4]
    day = str[:2]
    date = (year + month + day)
    return date
