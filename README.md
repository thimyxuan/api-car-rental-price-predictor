## Clone

```$ git clone git@github.com:thimyxuan/api-car-rental-price-predictor.git```

## Stack technique

- Python
- Numpy
- Pandas
- Sklearn
- Joblib
- FastAPI

## Objet

Ceci est l'API de prédiction des prix de location du projet Getaround.

Ele est déployée à l'adresse suivante : <a href="https://fastapi-getaround-7a9ad465e3fa.herokuapp.com/" target="_blank">https://fastapi-getaround-7a9ad465e3fa.herokuapp.com/</a>

Vous pouvez retrouver l'ensemble du projet Getaround dans <a href="https://github.com/thimyxuan/car-rental-delay-analysis" target="_blank">ce repository</a>.

## Déploiement en local

Créer l'image Docker :  

```$ docker build . -t fastapi_env```

Créer le container Docker :  

```$ docker run -it -v "$(pwd):/app" -p 4000:4000 fastapi_env```

## Déploiement avec Heroku

Assurez-vous d'être connecté à vos comptes Docker et Heroku :    

```$ heroku login```

```$ docker login --username=<your username> --password=$(heroku auth:token) registry.heroku.com```

```$ heroku create YOUR_APP_NAME```

```$ heroku container:push web -a YOUR_APP_NAME```

```$ heroku container:release web -a YOUR_APP_NAME```

```$ heroku open -a YOUR_APP_NAME```