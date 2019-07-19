# hamsafar

## create virtual env

    python3 -m venv .env

    source .env/bin/activate

    pip install -r requirements.txt

## build project

    python manage.py makemigrations

    python manage.py migrate

## run project

    python manage.py runserver

## APIes in project

###create user 
    url : /api/v1/profile/\?format\=json (POST)

        {
            "profile": {
                "user": {
                    "username": "akbar",
                    "password": "Taba79ALi"
                },
                "first_name": "seyed ali",
                "last_name": "taba",
                "cash": 0
            }
        }

        response :

        {
            "response": 200
        }

### get my user info
    url : /api/v1/profile/\?format\=json (GET)

        response : 

        {
            "profile": {
                "id": 1,
                "user": {
                    "username": "ali"
                },
                "first_name": "seyed ali",
                "last_name": "taba",
                "cash": 0
            }
        }

### create request
    url : /api/v1/request/\?format\=json (POST)

        {
            "request": 
                {
                    "lat": "0.0000000000000",
                    "long": "0.0000000000000",
                    "status": "pending"
                }
        }

        response : 

        {
            "response": 200
        }

###get my requests 
    url : /api/v1/request/\?format\=json (GET)

        response :

        {
            "requests": [
                {
                    "id": 1,
                    "user": {
                        "username": "ali"
                    },
                    "lat": "0.0000000000000",
                    "long": "0.0000000000000",
                    "status": "pending"
                },
                {
                    "id": 2,
                    "user": {
                        "username": "ali"
                    },
                    "lat": "0.0000000000000",
                    "long": "0.0000000000000",
                    "status": "accepted"
                }
            ]
        }
###get last request
    url : /api/v1/request/last/\?format\=json (GET)
        response:

            {
                "request": {
                    "id": 1,
                    "user": {
                        "username": "ali"
                    },
                    "start_lat": "23.2321320000000",
                    "start_long": "32.2132000000000",
                    "end_lat": "2.0000000000000",
                    "end_long": "2.0000000000000",
                    "status": "accepted"
                }
            }


###get my nearby persons
    url : /api/v1/find-near/\?format\=json (GET)

        response: 

        {
            "requests": [
                {
                    "id": 1,
                    "user": {
                        "username": "ali"
                    },
                    "lat": "0.0000000000000",
                    "long": "0.0000000000000",
                    "status": "accepted"
                },
                {
                    "id": 2,
                    "user": {
                        "username": "ali"
                    },
                    "lat": "0.0000000000000",
                    "long": "0.0000000000000",
                    "status": "accepted"
                }
        }
    
###accept nearby persons
    url : /api/v1/find-near/\?format\=json (POST)  [ this request change status person requests to accepted ]

        response:

        {
            "response": 200
        }


###how to use token
    
        recieve token => /api/token (POST)

            {
                "username":"ali"
                "password":"1234"
            }

            response:

            {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFsaSIsImV4cCI6MTU2NjEwMTc3NCwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU2MzUwOTc3NH0.aVxoW8EooXcdwdF9gaJa2qJDbo6o2VJWYU43RNOrcZM"
            }

        how to use authencitation => in your headerfile you must set this :
            Authorization: JWT <your token>

            