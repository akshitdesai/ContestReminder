from django.shortcuts import render
from django.contrib.auth import authenticate
from contest.models import user
from contest.saveuser import *
from contest.otpGet import *
import contest.sendMail as sm
from random import *
import math
from datetime import *


def index(request):
    return render(request,'index.html')


def loginToregister(request):
    return render(request,'register.html')


def register(request):
    email1 = request.POST.get('email1')
    no1 = request.POST.get('no1')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    lis = request.POST.getlist('contest')

    dict1 = {'codechef' : 0,'codeforces': 0,'hackerearth': 0,'hackerrank':0,'spoj': 0}
    for i in dict1.keys():
        if i in lis:
            dict1[i] = 1
    
    if validatePassword(password1,password2) == False:
        return render(request,'register.html')
    if validateEmail(email1) == False:
        return render(request,'register.html')
    if validateNumber(no1) == False:
        return render(request,'register.html')

    # setting user details
    request.session['lis'] = [email1,password1,no1]
    request.session['dict1'] = dict1
    
    
    # otp generation and send 
    otp = math.floor(random()*1000000)%1000000
    request.session['otp'] = str(otp)
    request.session['email1'] = email1
    temptime = datetime.now().replace(microsecond=0)
    
    request.session['syear'] = temptime.year
    request.session['smonth'] = temptime.month
    request.session['sday'] = temptime.day
    request.session['shour'] = temptime.hour
    request.session['sminute'] = temptime.minute
    request.session['ssecond'] = temptime.second

    otpstring = 'Your verification otp is:' + str(otp)
    subject = 'Email Verification'
    sm.sendMail(email1,otpstring,subject)
    return render(request,'otpVerify.html')


def otpverify(request):
    otp1 = request.session['otp']
    otp2 = request.POST.get('otp')

    etime = datetime.now().replace(microsecond=0)
    stime = getStime(request)
    delta = math.floor((etime - stime).total_seconds())
    if otp1 != otp2 or delta > 60:
        user.objects.filter(email=request.session['email1']).delete()
        return render(request,'register.html')

    lis = request.session['lis']
    dict1 = request.session['dict1']
    
    # save user
    user1 = user(email=lis[0],codechef=dict1['codechef'],codeforces=dict1['codeforces'],hackerearth=dict1['hackerearth'],hackerrank=dict1['hackerrank'],spoj=dict1['spoj'],password=lis[1],no=lis[2])
    user1.save()

    # deleting session variables
    del request.session['syear']
    del request.session['smonth']
    del request.session['sday']
    del request.session['shour']
    del request.session['sminute']
    del request.session['ssecond']
    del request.session['email1']
    del request.session['lis']
    del request.session['dict1']
    return render(request,'index.html')


def login(request):
    email1 = request.POST.get('email1')
    password1 = request.POST.get('password1')
    test2=None
    test1=True
    try:
        test2 = user.objects.get(email=email1)
    except:
        test1 = False
    print(test1)
    if test1 == True:
        test1 = (test2.password == password1)
    if test1 == False:     
        return render(request,'index.html')
    else:
        request.session['logged']=True
        request.session['email']=email1
        return render(request,'profile.html',{'data':test2})


def update(request):
    user1 = user.objects.get(email=request.session['email'])
    lis = request.POST.getlist('contest')
    
    dict1 = {'codechef' : 0,'codeforces': 0,'hackerearth': 0,'hackerrank':0,'spoj': 0}
    for i in dict1.keys():
        if i in lis:
            dict1[i] = 1

    user.objects.filter(email=request.session['email']).update(codechef=dict1['codechef'],codeforces=dict1['codeforces'],hackerearth=dict1['hackerearth'],hackerrank=dict1['hackerrank'],spoj=dict1['spoj'])
    data = user.objects.get(email=request.session['email'])
    return render(request,'profile.html',{'data':data})


def logout(request):
    request.session['logged'] = False
    del request.session['email']
    return render(request,'index.html')


def delete(request):
    user.objects.filter(email=request.session['email']).delete()
    del request.session['email']
    return render(request,'register.html')
