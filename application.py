from flask import Flask
#from flask import redirect, url_for, request, render_template, abort, flash, get_flashed_messages
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
