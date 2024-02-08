


def datecheck(filesall, StartDate, EndDate):   #返回符合日期的数组
    #strs = [s for s in strs1 if s != ""]
    
    files = [int(s) for s in filesall if s.isdigit()]          #筛选数据
    
    dates = [d for d in files if (StartDate <= d <= EndDate) ]  #日期确认
    
    datestr = [str(d) for d in dates ]
    if datestr :
        return datestr
    else:
        return None


def GenPath(p1,p2):
    p = p1+"/"+p2
    return p
