from unicodedata import name

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


if __name__ == "__main__":
    dir(app.run)
    app.run(host='0.0.0.0', port=5000)