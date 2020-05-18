# python code to send email without attachement
# required imports
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def sendmail(toaddr,content):
	# setting up the details
	fromaddr = "contestreminder1@gmail.com"

	pwd = "1Contest#Reminder"
	x=0

	# toaddr = ["ultrautsav@gmail.com","asb.cp.62@gmail.com"]

	receiver = "Entusiastic coder"

	    

	# instance of MIMEMultipart 

	msg = MIMEMultipart() 



	# storing the senders email address 

	msg['From'] = fromaddr 



	# storing the receivers email address 

	msg['To'] = ', '.join(toaddr) 



	# storing the subject 

	msg['Subject'] = "Reminder for Upcoming Event"

	msg.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msg.attach(msgAlternative)

	msgText = MIMEText('Hello coders! Are you all set for upcoming contest?')
	msgAlternative.attach(msgText)
	# string to store the body of the mail 

	body = ""
	with open('mail.html', 'r' , encoding="utf8") as file:
		body = file.read()
	
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
	msg.attach(msgImage)

	# creates SMTP session 

	s= smtplib.SMTP('smtp.gmail.com:587')



	# start TLS for security 

	s.starttls() 



	# Authentication 

	s.login(fromaddr,pwd) 



	# Converts the Multipart msg into a string 

	text = msg.as_string() 



	# sending the mail 

	s.sendmail(fromaddr, toaddr, text) 
	x+=1
	print(receiver+"  Done")


	# terminating the session 

	s.quit()

