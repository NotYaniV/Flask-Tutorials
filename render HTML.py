from flask import Flask,url_for,redirect,render_template

app = Flask(__name__)

# home page
@app.route("/<content>")
def home(content):
    #return render_template("index.html",content=content,r=67)
    #return render_template("index.html" )
    return render_template("index.html", content= ['fname', 'sname', "lname"])

# Getting the name through the link
@app.route("/<name>")
def user(name):
    return f"Hello {name}" 

# redirecting
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin")) 


if __name__ == '__main__':
    app.run()




