from re import template
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "pinnochio"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def users():
    print("got user information")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("main.html")




if __name__ == "__main__":
    app.run(debug=True)