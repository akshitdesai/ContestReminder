import threading 
import time
import requests
import datetime
from MySQLdb import *
from test import *
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
		if(contest['StartTime'][5:11]=='19 Apr'):
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
	time2 = time1 + datetime.timedelta(hours=6,minutes=00)

	time1 = time1.time()
	time2 = time2.time()

	StartTime = datetime.datetime.strptime(contestStartTime,'%H:%M:%S').time()

	if StartTime>time1 and StartTime <= time2:
		return True
	else:
		return False
    
def sendMail(content,contest):
    #send message to everyone in Database
	con = None
	try:
		con = connect(host='localhost',user='root',password='5656',db='ContestReminder')
	except:
		print('Error! retry after sometime')
	cursor = con.cursor()
	platform = contest['Host']
	cursor.execute('select * from contest_user where '+platform+'=1;')
	mailList = []
	for record in cursor.fetchall():
		mailList.append(record[1])
	print(content)
	print("-------")
	print(contest)
	sendmail(mailList,contest)

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
    
	detailMsg = ""
	detailMsg += contest_details['Name'] + '\n'
	detailMsg += 'Start Time : ' + time + '\n'
	detailMsg += 'Duration : ' + contest_details['Duration'] + '\n'
	detailMsg += 'Platform : ' + contest_details['Host'] + '\n'
	detailMsg += 'Link : ' + contest_details['contestLink'] + '\n'

	if(contest_details['Host']=="CODEFORCES"):
		detailMsg += 'Registration Link : https://codeforces.com/contestRegistration/' + contest_details['contestLink'].split('/')[-1] + '\n'
	return detailMsg

def initMail(Mailcontests):
    #Traverse for every contest for Reminer

	for contest in Mailcontests:
		content = createContent(contest)
		sendMail(content,contest)
		todaysContests.remove(contest)

def sendReminder():
    #Send Mail to Recepient for every contest before an hour

	sendRemain = []
	for contest in todaysContests:
		contestStartTime = contest['StartTime']+":00"
		if(inHour(contestStartTime)):
			sendRemain.append(contest)
	initMail(sendRemain)



def first():
	while(True):
		extractor()
		time.sleep(86400)
  
def second():
	while(True):
		sendReminder()
		time.sleep(5400) 
  
#contest = {'name':'hackwithInfy','Host':'SPOJ'}
#sendMail('Here We Go',contest)
extractor()
sendReminder()
#if __name__ == "__main__":
#	t1 = threading.Thread(target=first, args=()) 
#	t2 = threading.Thread(target=second, args=()) 
  
    	# starting thread 1 
#	t1.start() 
    	# starting thread 2 
#	t2.start() 
  
    	# wait until thread 1 is completely executed 
#	t1.join() 
   	# wait until thread 2 is completely executed 
#	t2.join() 
  
    	# both threads completely executed 
#	print("Done!") 
