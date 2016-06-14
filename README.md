
## Oogway

Oogway is an open source server monitoring dashboard that works with the help of Sensu tool. Ooghwa is build using skills like python with Django framework. Javascript with Angularjs framework and Mongodb to store sensu data and sqlite default Db of Django framework

Oogway help us to monitor the remote server and store the data of servers conditions like check_Mem, check_Load, check_disk etc.

## Features

A webbased dashboard for monitoring servers based on you sensu data
Live graphs with indicating colors based on server condition


Prerequisite : First you have to install sensu and python
	
	1. Sensu Installtion : https://sensuapp.org/docs/latest/installation-guide

	2. apt-get install python  

	3. Runing crontab to collect data from sensu
				1. update the url variable in the script with your sensu url 
				2. Enter crontab -e in your ubuntu terminal
				3. Define crontab condition for the script which are in "mongo_save_checks_values"

				for example in crontab define like this:
					*/1 * * * * /bin/python "mongo_save_checks_values/'python_scripts'"


## Installation of Backend code in Ubuntu:

Installtion Step :

	1.  clone the code from git using below url in terminal 
	 	git clone git@github.com:Above-Solutions-India-Ltd/Oogway.git

	2. create virtual environment
		virtualenv monitoring_dashboard

	3. Activate virtualenv from your terminal
		source /monitoring_dashboard/bin/activate

	4. install Django into your virtualenv
		pip install Django==1.8

	5. install corsheaders into your virtualenv
		pip install django-cors-headers

	6. install requests into your virtualenv
		pip install requests

	7. install pymango into your virtualenv
		python -m pip install pymongo

	8. install dateutil parser into your virtualenv
		pip install python-dateutil	

	9. Run the Django Application
		python manage.py runserver


## Installation of Frontend code in Ubuntu:
1. Create a folder in your lamp/xamp
2. Copy the folder "devops" form git clone folder and past it to the folder in lamp/xamp
3. Change the url in /devops/app/js/services/services.js to your sensu url 


## Runing the Application:
	1.Once the url are all updated, we can go lamp/xamp and navigate to our project
	2.We will find the list of project in the form of boxes with colors like Green, orange, red
		colors indicate status of server
			1. Green = good condition
			2. Orange =  warning condition
			3. Red = critical condition
	3. User can click on boxes to check which parameter leads to change in color default should be green
	4. User can also check the parameters graph and find from how long that parameter has changed its status 




## Support

For help with general setup and configuration issues please contact info@above-inc.com


The following distribution are supported:
	1. Ubuntu 14.14
	2. Windows 7
