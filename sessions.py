from flask import Flask,url_for,redirect
from flask import render_template,request,session

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5) # store the permanent data for 5 min
# home page
@app.route("/")
def home():
    #return render_template("index.html",content=content,r=67)
    #return render_template("index.html" )
    return render_template("index.html",content="testing")


# sessions are temporary only when user uses the site or log in
# next time the user logs in session data is remade and cleaned once logged out

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # by default it is fault
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))  # no need to pass arguments
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login")) 


# Getting the name through the link
@app.route("/user")
def user():
    if "user" in session:  
        user = session["user"]  # getting session info
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

# redirecting
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin")) 


if __name__ == '__main__':
    app.run(debug=True)

