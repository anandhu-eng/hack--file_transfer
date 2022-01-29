from flask import Flask, render_template,request
import transfer

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/reciever")
def rec():
    return render_template('receiver.html')

@app.route("/server")
def ser():
    devices=["asus","dell","apple","hp"]
    return render_template('server.html', devices=devices, name="anandhu")


@app.route("/serverShare", methods=['POST'])
def sShare():
    file=request.files["File Input"]
    print (file.filename)
    transfer.server_start()
    transfer.server_wait_for_client_to_connect()
    transfer.server_send_file(file)

    
@app.route("/recSide", methods=['POST'])
def recSide():
    file=request.form["Filesave"]
    print (file)
    transfer.client_start()
    transfer.client_recieve_file(file)


#to go to the virtualenv: source venv/Scripts/activate
#to deactivate: deactivate
