# Django File Upload Tutorial

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

Code example used in the tutorial series on Django File Upload.

Watch it on YouTube: [Django 2.1 File Upload](https://www.youtube.com/playlist?list=PLLxk3TkuAYnpm24Ma1XenNeq1oxxRcYFT)

Subscribe to my YouTube channel: [youtube.com/VitorFreitas](https://www.youtube.com/VitorFreitas?sub_confirmation=1)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/django-upload-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

to apply the migrations of databse on heroku 
use this command 
```bash
heroku run python manage.py migrate
```
to see heroku databse you must have 
**psql shell**
to run this database you must need to enter these cardinalities
## Server [localhost]: ec2-54-175-243-75.compute-1.amazonaws.com
## Database [postgres]: dek16c60l0bgec
## Port [5432]: 5432
## Username [postgres]: vigqhvgcugbrih
## Password for user vigqhvgcugbrih:7ff8e5deb2a509d49106c5e2e61024a56b67c070b06ba7ad579d77453c47dcb8






## License

The source code is released under the [MIT License](https://github.com/sibtc/django-upload-example/blob/master/LICENSE).