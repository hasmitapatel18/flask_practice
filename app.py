from flask import Flask, render_template, request, session
from flask_session import Session
import datetime
app = Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


@app.route('/hasmita')
def hasmita():
    return "Hello Hasmita!"


@app.route('/<string:name>')
def helloname(name):
    return f"Hello, {name.capitalize()}!"


@app.route('/bye')
def bye():
    headline="Goodbye!"
    return render_template("index.html", headline=headline)


@app.route('/newyear')
def newyear():
    now=datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", new_year=new_year)


@app.route('/listnames')
def listnames():
    names=['Alice', 'Bob', 'Charlie']
    return render_template("listnames.html", names=names)

@app.route('/')
def index():
    headline="Hello World!"
    return render_template("index.html", headline=headline)

@app.route('/second')
def second():

    return render_template("secondpage.html")

@app.route('/forminput')
def forminput():

    return render_template("forminput.html")


@app.route('/formoutput', methods=["GET", "POST"])
def formoutput():
    if request.method=="GET":
        return "please fill in form"
    else:
        # ie if method=POST
        # name=input field name in forminput.html
        get_name = request.form.get("name")
        return render_template("formoutput.html", get_name=get_name)


@app.route('/addnotes', methods=["GET", "POST"])
def notespage():
    # if there are no notes initialize an empty list. notes=list
    if session.get("notes") is None:
        session["notes"]= []
    if request.method=="POST":
        # note = user input (ie has posted) note and get it
        note = request.form.get('note')
        # append user note that (has been got) to session notes list
        session["notes"].append(note)
        # render webpage and list of notes
    return render_template('addnotes.html', notes=session["notes"])
