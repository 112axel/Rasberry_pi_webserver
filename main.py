from flask import Flask, render_template
from flask_socketio import SocketIO,send
import psutil

app = Flask(__name__)
app.config["SECRET_KEY"] = "test" #better password needed
socketio = SocketIO(app,cors_allowed_origins = "*")




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

    return render_template("chat.html")


@socketio.on("message")
def handle_msg(msg):
    print("Message: " + msg)
    send(msg,broadcast = True)

    
if __name__ == '__main__':
    socketio.run(app,host = "0.0.0.0",debug = False,port = 80)

    #app.run(debug=False, port=80, host='0.0.0.0')