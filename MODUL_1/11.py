def apakahKabisat(n):
    if n%4==0:
        if n%100==0 and n%400==0:
            return True
        elif n%100==0 and n%400!=0:
            return False
        return True
    return False
