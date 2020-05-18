import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from email.mime.image import MIMEImage

todaysContests = list()
def extractor():
    #extract Todays Contests from json file and append it to list

    todaysContests.clear()
    data = requests.get(url="https://www.stopstalk.com/contests.json")
    data = data.json()
    upcoming_contest = data['upcoming']
    #print(upcoming_contest)
    today = datetime.datetime.now()
    dateToday = str(today.strftime("%d"))+" "+str(today.strftime("%b"))
    contestsCnt = 0
    for contest in upcoming_contest:
        if(contest['StartTime'][5:11]=="25 Apr"):
            contest_details = {
                'Name' : contest['Name'],
                'StartDate' : str(today.strftime("%d"))+" "+str(today.strftime("%B"))+","+str(today.strftime("%Y")),
                'StartTime' : contest['StartTime'][-5:],
                'Duration' : contest['Duration'],
                'Host' : contest['Platform'],
                'contestLink' : contest['url']
            }
            todaysContests.append(contest_details)
            contestsCnt += 1
    if(contestsCnt == 0):
        print("No contests Today!!")

def inHour(contestStartTime):
    #Check if contest is within an hour or not
    
    time1 = datetime.datetime.now()
    time2 = time1 + datetime.timedelta(hours=8,minutes=30)

    time1 = time1.time()
    time2 = time2.time()

    StartTime = datetime.datetime.strptime(contestStartTime,'%H:%M:%S').time()

    if StartTime>time1 and StartTime <= time2:
        return True
    else:
        return False
    
def sendMail(content):
    #send message to everyone in Database
    
    fromaddr = "codestromer@gmail.com"
    toaddr = "akshitdesai@yahoo.com"
    x=0

    # Define these once; use them twice!

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Contest Reminder'
    msgRoot['From'] = fromaddr
    msgRoot['To'] = toaddr
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Hello coders! Are you all set for upcoming contest?')
    msgAlternative.attach(msgText)

    # Reading HTML file for styling
    body = ""
    with open('mail.html', 'r' , encoding="utf8") as file:
        body = file.read()

    body += '<h1 style="top: 0px; font-size:30px">' + content['Name'] + '</h1>'
    body += '<p style="font-size:17px"><span style="color:green;"> Date 📅: </span>'+ content['StartDate'] + '</p>'
    body += '<p style="font-size:17px"><span style="color:green;"> Time ⏰: </span>'+ content['StartTime'] + '</p>'
    body += '<p style="font-size:17px"><span style="color:green;"> Duration ⌛️: </span>'+ content['Duration'] + '</p>'
    body += '<a class="btn1" href="'+ content['contestLink'] + '" style="text-decoration:none">Contest Link</a>'
    if(content['Host'] == 'CODEFORCES'):
        body += '<a class="btn1" href="'+ content['regLink'] + '" style="text-decoration:none">Registration Link</a>'
    
    body2 = ""
    with open('mail2.html', 'r' , encoding="utf8") as file:
        body2 = file.read()

    body += body2

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(body, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    hostlogopath ="pic/"
    if(content['Host'] == "CODEFORCES"):
        hostlogopath += 'codeforces.png'
    elif(content['Host'] == "CODECHEF"):
        hostlogopath += 'codechef.png'
    elif(content['Host'] == "HACKEREARTH"):
        hostlogopath += 'hackerearth.png'
    elif(content['Host'] == "HACKERRANK"):
        hostlogopath += 'hackerrank.png'
    elif(content['Host'] == "SPOJ"):
         hostlogopath += 'spoj.jfif'


    fp = open(hostlogopath, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr,"Harikrushna123") 

    # Converts the Multipart msg into a string 
    text = msgRoot.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    x+=1
    # terminating the session 
    s.quit()
    print(x)

def createContent(contest_details):
    #Create HTML msg for contest Reminder

    time = ""
    if int(contest_details['StartTime'][0:2])>=12:
        if(int(contest_details['StartTime'][0:2]) ==12):
            time = contest_details['StartTime']+" PM"
        else:
            time = str(int(contest_details['StartTime'][0:2])-12)+(contest_details['StartTime'][2:])+" PM"
    else:
        time = contest_details['StartTime']+" AM"
    
    detailMsg = {
        'Name' : contest_details['Name'],
        'StartDate' : contest_details['StartDate'],
        'StartTime' : time ,
        'Duration' : contest_details['Duration'],
        'Host' : contest_details['Host'],
        'contestLink' : contest_details['contestLink']
    }

    if(contest_details['Host']=="CODEFORCES"):
        detailMsg['regLink'] =  "https://codeforces.com/contestRegistration/" + contest_details['contestLink'].split('/')[-1]
        
    return detailMsg

def initMail(Mailcontests):
    #Traverse for every contest for Reminer

    for contest in Mailcontests:
        content = createContent(contest)
        sendMail(content)
        todaysContests.remove(contest)

def sendReminder():
    #Send Mail to Recepient for every contest before an hour

    sendRemain = []
    for contest in todaysContests:
        contestStartTime = contest['StartTime']+":00"
        if(inHour(contestStartTime)):
            sendRemain.append(contest)
    initMail(sendRemain)



extractor()

sendReminder()