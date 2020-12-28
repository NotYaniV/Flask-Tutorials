from flask import *

from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5) # store the permanent data for 5 min
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# User table 
class users(db.Model):  
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name",db.String(100))
    email = db.Column("email",db.String(20))
    
    def __init__(self,name, email):
        self.name = name
        self.email = email
    
# home page
@app.route("/")
def home():
    #return render_template("index.html",content=content,r=67)
    #return render_template("index.html" )
    return render_template("index.html",content="testing")



@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())
# sessions are temporary only when user uses the site or log in
# next time the user logs in session data is remade and cleaned once logged out

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # by default it is fault
        user = request.form["nm"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).first() # looking by name and givs the first result
        '''
        found_user = users.query.filter_by(name=user).delete() # delete only one entry
        for user in found_user:
            user.delete()   # delete all of them                                                   
        '''
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        
        flash("Login successfull")
        return redirect(url_for("user"))  # no need to pass arguments
    else:
        if "user" in session:
            flash("You are logged in already")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/logout")
def logout():
    if "user" in session:  
        user = session["user"]
        flash(f"You have logged out from your session, {user}", "info") # flashing a message
    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login")) 


# Getting the name through the link
@app.route("/user",methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:  
        user = session["user"]  # getting session info
        
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

# redirecting
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin")) 


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

