from flask import Flask, request
from flask_cors import CORS

from controllers.cnc_controller import CNCController

# NOTICE: To run this on Windows you need to run it outside of 
# Docker to let it access the USB port. This means, before running it you 
# need to set up a venv for it as well.
PORT = 'COM3' # for windows 

app = Flask(__name__)
CORS(app)

cnc = CNCController(PORT)

cnc.unlock()
cnc.home()
cnc.set_relative_mode()

move_value = 10

stats = {}
def add_stat(key=""):
    stats[key] = stats.get(key, 0) + 1
    return 0

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/press-button-1", methods=["GET", "POST"])
def handle_button_1():
    if request.method == "GET":
        return show_button_1()
    else:
        return press_button_1()

def show_button_1():
    return f"<p>You have now pressed it {stats.get("button_1", 0)} time(s).</p>"

def press_button_1():
    add_stat("button_1")
    return { "pressed": stats.get("button_1", 0) }

    # return "<p></p>"

@app.route("/press-y-minus", methods=["POST"])
def handle_press_y_minus():
    cnc.move_relative(0, -move_value, 0)
    cnc.wait_until_idle()
    return { "message": f"Going Y{-move_value}" }

@app.route("/press-y-plus", methods=["POST"])
def handle_press_y_plus():
    cnc.move_relative(0, move_value, 0)
    cnc.wait_until_idle()
    return { "message": f"Going Y{move_value}" }

@app.route("/press-x-minus", methods=["POST"])
def handle_press_x_minus():
    cnc.move_relative(-move_value, 0, 0)
    cnc.wait_until_idle()
    return { "message": f"Going X{-move_value}" }

@app.route("/press-x-plus", methods=["POST"])
def handle_press_x_plus():
    cnc.move_relative(move_value, 0, 0)
    cnc.wait_until_idle()
    return { "message": f"Going X{move_value}" }

@app.route("/press-z-plus", methods=["POST"])
def handle_press_z_plus():
    cnc.move_relative(0, 0, move_value)
    cnc.wait_until_idle()
    return { "message": f"Going Z{move_value}" }

@app.route("/press-z-minus", methods=["POST"])
def handle_press_z_minus():
    cnc.move_relative(0, 0, -move_value)
    cnc.wait_until_idle()
    return { "message": f"Going Z{-move_value}" }

@app.route("/press-home", methods=["POST"])
def handle_press_home():
    cnc.home()
    cnc.wait_until_idle()
    return { "message": "Homing." }