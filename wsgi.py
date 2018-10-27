from app import app as application
from views import home

if __name__ == '__main__':
    application.run(port=8000, host="0.0.0.0", debug=True)
