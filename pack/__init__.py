
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "you-will-never-guess-oh-yes!"

from pack import routes