## Clone

```$ git clone git@github.com:thimyxuan/api-car-rental-price-predictor.git```

# Objet

Ceci est l'API de prédiction des prix de location du [projet Getaround](https://github.com/thimyxuan/car-rental-delay-analysis).

Ele est déployée à l'adresse suvante : 
[https://api-getaround-58fb6b190f83.herokuapp.com/](https://api-getaround-58fb6b190f83.herokuapp.com/)

# Déploiement en local

Créer l'image Docker
$ docker build . -t fastapi_env

Créer le container Docker
$ docker run -it -v "$(pwd):/app" -p 4000:4000 fastapi_env

# Déploiement avec Heroku

Assurez-vous d'être connecté à votre compte Docker et Heroku : 

$ heroku login

$ docker login --username=<your username> --password=$(heroku auth:token) registry.heroku.com

$ heroku create YOUR_APP_NAME

$ heroku container:push web -a YOUR_APP_NAME

$ heroku container:release web -a YOUR_APP_NAME

$ heroku open -a YOUR_APP_NAME

## Stack technique

- Python
- Numpy
- Pandas
- Sklearn
- Joblib
- FastAPI