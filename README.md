[![CircleCI](https://circleci.com/gh/fokinpv/loan-service.svg?style=svg)](https://circleci.com/gh/fokinpv/loan-service)
[![codecov](https://codecov.io/gh/fokinpv/loan-service/branch/master/graph/badge.svg)](https://codecov.io/gh/fokinpv/loan-service)

# Toy Loan Simulator

This service is simulating loan processing.

## Requirments

 - Python >= 3.7

`Makefile` can be used to run few simple commands like `requirements`,
`run`, `lint`.

`pip-tools` is using to manage requirements

```sh
(venv) $ pip install pip-tools
```

## Run

 There are few options to run application.

 - First option is to use virtual enviroment.

 Install requirements.
 ```sh
 (venv) $ make install
 ```
 Run application.
 ```sh
 (venv) $ make run
 ```
 - To run it with `docker`
 ```sh
 $ docker build -t loan-service .
 $ docker run -it -p 8000:8000 loan-service
 ```
 - This app has deployment at Heroku https://loan-service.herokuapp.com/docs
