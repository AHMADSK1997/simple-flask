# MyBitcoin
MyBitcoin is a python Application (Flask Based) thats presents the current Bitcoin price in USD and calculating the average price for the last 10 minutes, its get the data from API:

https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10


## Running MyBitcoin locally
MyBitcoin is a [Python](https://www.python.org/) application built using [Flask](https://palletsprojects.com/p/flask/). You can build and run it from the command line:


```
git clone https://github.com/AHMADSK1997/simple-flask.git
cd simple-flask
pip install -r requirements.txt
python main.py
```

You can then access MyBitcoin here: http://127.0.0.1:5000/

<img width="1042" alt="MyBitcoin-screenshot" src="https://imgur.com/moYQMm2.png">

## Build application using docker

```
$ git clone https://github.com/AHMADSK1997/simple-flask.git
$ docker build -t hw-app .
```
## Run the container
```
$ docker run -it -d -p 5000:5000 hw-app .
```
Now visit http://localhost:5000

## pushes the generated Docker image to Docker Hub
```
$ docker tag hw-app ahmadsk/hw-app
$ docker push ahmadsk/hw-app
```
Note: you will use your username on docker hub and you should be logind using  ```$ docker login ```