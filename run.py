from app import app
from views import home
from os import system

if __name__ == '__main__':
    system('uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi')
