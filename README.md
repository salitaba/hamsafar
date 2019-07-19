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