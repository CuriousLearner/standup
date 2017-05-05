# standup
Automating standups; one task at a time!


### Installation

To set up local environment for the project, please follow these steps:

- Create virtualenv and activate it:

```bash
$ virtualenv venv && source venv/bin/activate
```

- Now install dependencies:

```bash
$ pip install -r requirements.txt
```

- Set up `SECRET_KEY` and `ORGANIZATION_NAME` as env variables

```bash
(venv) $ export SECRET_KEY='c)sd34%#--329@#$*^49mm#$%j34234!#$j)yr3=%4e*'
(venv) $ export ORGANIZATION_DOMAIN='localhost.com'
```

- From inside `src` directory, run server by:

```bash
(venv) $ python manage.py runserver
```

The app is up and running at [localhost:8000](http://127.0.0.1:8000)
