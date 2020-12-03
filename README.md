# Contest Reminder

Web app for the user for login, sign up and saving user preference.
According to the preference of users, they will get reminders of contests hosted on CodeChef,  Code-forces, Hacker-earth, Hacker-rank, and SPOJ.

## Screenshots
<p float="left">
  <img src="https://github.com/codestromer/ContestReminder/blob/master/Screenshots/2020-04-18%2012_55_26-Log%20in.png" alt="Web-view" width="600"/>  
  <img src="https://github.com/codestromer/ContestReminder/blob/master/Screenshots/photo_2020-04-18_12-58-30.jpg" alt="Mail-view" height="400"/>
</p>

## Motivation
As a competitive programmer, I always want to participate in every contest I can. But sometimes I forgot and misses the contests.
Some of the platforms send reminders as CF sends reminds before 1 day, HE sends reminders via message.

So I decided to make an app that sends reminder mail(mail with clean design and contest link) uniformly just before an hour or half an hour And also I can change my preferences in between.

## Tech used

* Django
* PostgreSQL (psycopg2)
* Bootstrap

## Installation

* Clone project using git
  * `git clone https://github.com/codestromer/ContestReminder.git`
* [Create Virtual Environment](https://docs.python.org/3/library/venv.html) and activate
* Get into project directory
  * `cd ContestReminder`
* Install requirenments
  * `pip install -r requirements.txt`
* To run Django Project after [applying migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/)
  * `cd contestreminder`
  * `python manage.py runserver`

## Work

**Done till now**
* Login, SignUp, Logout
* Custom Django-Admin Dashboard
* Extract contest Data from [stopstalk API](https://www.stopstalk.com/contests.json)

**Remaining Work**
* Add Bootstrap and Improve design
* Add contributor page using github api
* Add Email verification after Signup
* Change DB to PostgreSQL (Use SQLite for development now)
* Fix send mail script.
* Add [Django crons](https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/) to send mail(every hour) and extract contests from API(every 24 hour)
* Test and Deploy to heroku

## Contributing

* You can join [Whatsapp Group](https://chat.whatsapp.com/K8cEeEJZRFBDZeRijx2Mds)
* As I used this for my own projects and implimented a year back, I know this might not be the perfect approach for all the projects out there. If you have any ideas, just open an issue and tell me what you think.
* If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## Future Scope

* Instead of mail, we can give an option either mail or SMS.
* We can send reminders for the hackathons too. (From Devfolio, Devpost)
* We can start a newsletter and mail a newsletter about new technologies and trends.
* We can merge [Image-genrator](https://github.com/codestromer/contest-image-generator) to this project.(Useful to college coding clubs)

| Mentors |
|---|
| Name | Email |
|---|---|
|Akshit Desai  | akshitdesai2000@gmail.com |
|Omij Mangukiya| ozx1812@gmail.com |
