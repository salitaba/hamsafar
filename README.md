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

    -> create user :  /api/v1/profile (POST)

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

    -> get my user info : /api/v1/profile (GET)

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

    -> create request : /api/v1/request (POST)

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

    -> get my requests : /api/v1/request (GET)

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

    -> get my nearby persons: /api/v1/find-near (GET)

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
    
    -> accept nearby persons: /api/v1/find-near (POST)  [ this request change status person requests to accepted ]

        response:

        {
            "response": 200
        }


    -> how to use token
    
        recieve token => /api/token (POST)

            {
                "username":"ali"
                "password":"1234"
            }

            response:

            {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFsaSIsImV4cCI6MTU2NjEwMTc3NCwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU2MzUwOTc3NH0.aVxoW8EooXcdwdF9gaJa2qJDbo6o2VJWYU43RNOrcZM"
            }

        authencitation => in your headerfile you must set this :

            