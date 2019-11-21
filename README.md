## Django login application

To run in a docker container `bash build_and_run.sh`

Otherwise it's recommended to 
`pip install virtualenv`, then to
cd to a parent directory of an application
```
virtualenv .
source bin/activate
cd source
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
python manage.py runserver [OPTIONAL IP:PORT]
```