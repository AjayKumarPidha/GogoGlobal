
## Run Project  ##

0. move to project root folder


1. Create and activate a virtualenv (Python 3)
```bash
pipenv --python 3 shell
pip install virtualenv


Create Virtual Environment command : virtualenv Venv

Activate virtual environment:-
windows os :  Venv/Scripts/activate
linux os :  source Venv/bin/activate


```
2. Install requirements
```bash
pipenv install
```
3. Create a MySQL database
```sql
CREATE DATABASE chat CHARACTER SET utf8;
```
4. Start Redis Server
```bash
redis-server
```

5. Init database
```bash
./manage.py migrate
```
6. Run tests
```bash
./manage.py test
```

7. Create admin user
```bash
python manage.py createsuperuser
```

8. Run development server
```bash
./manage.py runserver
```

To override default settings, create a local_settings.py file in the chat folder.

Message prefetch config (load last n messages):
```python
MESSAGES_TO_LOAD = 15
```