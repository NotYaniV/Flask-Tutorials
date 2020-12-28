from flask import Flask,url_for,redirect,render_template,request

app = Flask(__name__)

# home page
@app.route("/")
def home():
    #return render_template("index.html",content=content,r=67)
    #return render_template("index.html" )
    return render_template("index.html",content="testing")


@app.route("/login",methods=["POST", "GET"])
def  login():
    if request.method == "POST":
        usr = request.form["nm"]
        return redirect(url_for("user",name=usr))
    else:
        return render_template("login.html")

# Getting the name through the link
@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name} <h1>" 

# redirecting
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin")) 


if __name__ == '__main__':
    app.run(debug=True)

