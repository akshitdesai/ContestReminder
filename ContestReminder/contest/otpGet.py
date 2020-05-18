from datetime import *

def getStime(request):
    year = request.session['syear']
    month = request.session['smonth']
    day = request.session['sday']    
    d = date(year,month,day)

    hour = request.session['shour']   
    minute = request.session['sminute']    
    second = request.session['ssecond']    
    t = time(hour,minute,second)

    stime = datetime.combine(d,t)
    return stime