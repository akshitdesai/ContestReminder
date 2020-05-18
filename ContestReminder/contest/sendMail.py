# python code to send email without attachement
# required imports
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def sendMail(toaddr,string,subject):
	# setting up the details
    fromaddr = "contestreminder1@gmail.com"

    pwd = "1Contest#Reminder"

    #toaddr = "smailydenes@gmail.com"

    receiver = "Entusiastic coder"

	    

	# instance of MIMEMultipart 

    msg = MIMEMultipart() 



	# storing the senders email address 

    msg['From'] = fromaddr 



	# storing the receivers email address 

    msg['To'] = toaddr 



	# storing the subject 

    msg['Subject'] = subject



	# string to store the body of the mail 

    body = string


	# attach the body with the msg instance 

    msg.attach(MIMEText(body, 'plain')) 




	# instance of MIMEBase and named as p 

    p = MIMEBase('application', 'octet-stream') 



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

    #print(receiver+"  Done")


	# terminating the session 

    s.quit()