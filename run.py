from app import app

if __name__ == '__main__':
    from views import home
    app.run(port=8000, host="0.0.0.0", debug=True)
