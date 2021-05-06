from flask import Flask, render_template
from flask_socketio import SocketIO,send #4.3.2
import psutil
import re

import db_handler as db

app = Flask(__name__)
app.config["SECRET_KEY"] = "test" #better password needed
socketio = SocketIO(app,cors_allowed_origins = "*")


def valid_ip_addresses():
    """find all network interfaces that are on the local network"""
    temp = []

    for i in psutil.net_if_addrs().items():
        for j in i[1]:
            if re.match(r"192\.168\..+\..+",j[1]):
                temp.append(j[1])
            
    return temp

def picker(choise_list):

    if len(choise_list) == 1:
        return choise_list[0]

    for n,i in enumerate(choise_list):
        print(str(n+1)+":"+i)
        
    return choise_list[int(input("Type in mumber based on waht option you want to chose: "))-1]

socket_ip_address = picker(valid_ip_addresses())

@app.route('/')
def index():
    return 'Hello worlds'

"""
@app.route("/recipe")
def recipe_page():
    return render_template("recipes.html",users = test)
"""


@app.route("/status")
def status():
    
    return render_template("status.html",temp = psutil.disk_usage("C:")[0])

@app.route("/chat")
def chat_page():
    
    return render_template("chat.html",ip_address = socket_ip_address)


@socketio.on("message")
def handle_msg(msg):
    print("Message: " + msg)
    send(msg,broadcast = True)


#config




    
if __name__ == '__main__':
    socketio.run(app,host = "0.0.0.0",debug = False,port = 80)
    
    #app.run(debug=False, port=80, host='0.0.0.0')