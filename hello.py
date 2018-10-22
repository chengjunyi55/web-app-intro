import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key='w98fw9ef8hwe98fhwef'

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("render_main"))

@app.route("/page1")
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET', 'POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET', 'POST'])
def renderPage3():
    session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')

@app.route("/ctof")
def render_ctof():
    return render_template("ctof.html")

@app.route("/ftoc")
def render_ftoc():
    return render_template("ftoc.html")

@app.route("/mtokm")
def render_mtokm():
    return render_template("mtokm.html")

@app.route("/ftoc_result")
def render_ftoc_result():
    try:
        ftemp_result = float(request.args["fTemp"])
        ctemp_result = ftoc(ftemp_result)
        return render_template("ftoc_result.html", fTemp=ftemp_result, cTemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route("/ctof_result")
def render_ctof_result():
    try:
        ctemp_result = float(request.args["cTemp"])
        ftemp_result = ctof(ctemp_result)
        return render_template("ctof_result.html", cTemp=ctemp_result, fTemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route("/mtokm_result")
def render_mtokm_result():
    try:
        miles_result = float(request.args["Miles"])
        kms_result = mtokm(miles_result)
        return render_template("mtokm_result.html", Miles=miles_result, Kms=kms_result)
    except ValueError:
        return "Sorry: something went wrong."

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

def ctof(ctemp):
    return ctemp*1.8+32.0

def mtokm(miles):
   return miles*1.609344

if __name__ == "__main__":
    app.run(debug=True, port=54321)
