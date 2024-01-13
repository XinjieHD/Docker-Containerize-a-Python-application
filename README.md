This repository is to know how to containerize a basic Python application in local host or Docker Playgroud.

1. pip install flask
```
pip install flask
```
2. create the app.py, you can refer my app.py
3. try to run the app.py the default port is 5000
```
python app.py
```
4.create a Docker image built from a Dockerfile, you can refer my Docker.file
5.create the custom Docker image, you can modify the name "my-python-app", but don't omit the .
```
docker build -t my-python-app .
```
6.check the docker image, you should see the one you just built
```
docker image ls
```
7.run the Docker image in port 5001
```
docker run -p 5001:5000 -d my-python-app
```
8.you should be able to run it in port 5001, congrats

