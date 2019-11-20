#/bin/bash
docker build -t test-task .
docker run -di --name task -p 8000:8000 test-task
docker exec -di task python manage.py collectstatic
docker exec -t task python manage.py makemigrations 
docker exec -t task python manage.py migrate
docker exec -ti task python manage.py createsuperuser 
docker exec -ti task python manage.py runserver 0.0.0.0:8000
