from flask import Flask, request

app = Flask(__name__)

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
    return f"<p>Pressed button #1!</p> <p>You have now pressed it {stats["button_1"]} time(s).</p>"

    # return "<p></p>"