from flask import Flask, render_template
import os

app = Flask(__name__)

picfolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picfolder

@app.route("/")
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg')
    return render_template("index.html", user_image = pic1)



@app.route("/index")
def index1():
    return "Abulele"

app.run()