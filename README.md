# abhidjango
#requirement-
	<h3>1#) python3</h3>
	<h3>2#)django</h3>
	<h3>3#)postgres (change setting in setting.py like dbname,password)</h3>


TO run server -
$docker-compose up

#first time run
1-$docker exec <web-container-id> bash
	|
	|_
	  #python3 manage.py migrate
	  #python3 manage.py createsuperuser
 now add new user entry and datatable entry in http://0.0.0.0/8000/admin

2-open http://0.0.0.0/8000/login
