from app import app
from views import home

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0", debug=True)
