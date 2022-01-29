from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/reciever")
def rec():
    return render_template('receiver.html')

@app.route("/server")
def ser():
    return render_template('server.html')



#to go to the virtualenv: source venv/Scripts/activate
#to deactivate: deactivate
