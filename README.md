# Sibdev test

##### To run project

1. Clone the repo:
```
  git clone https://github.com/khava/sibdev_test.git
```
2. Go to backend folder
3. Run a command from terminal:
```
 docker-compose build
```
4. Run a command from terminal:
``` 
docker-compose up
```
5. Now you can access the app at 'http://localhost:8000/'

To access the admin panel, you need to create a superuser, for this run command:
```
docker-compose run web python3 manage.py createsuperuser
```

