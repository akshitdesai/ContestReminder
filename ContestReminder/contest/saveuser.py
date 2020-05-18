from contest.models import user
import requests

def validateEmail(email1):
    # test1 = requests.get('https://api.trumail.io/v2/lookups/json?email='+email1).json()
    test2 = False
    try:
        temp = user.objects.get(email=email1)
    except:
        test2 = True
    return (test2 == True)

def validatePassword(password1,password2):
    return password1 == password2

def validateNumber(no1):
    return len(no1) == 10

def saveUser(user1):
    user1.save()
    return True
