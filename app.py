from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask('app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SECRET_KEY'] = 'ImU4MjczZmdlsfkfe98rfdFhMzkZWUzMT'
db = SQLAlchemy(app)



