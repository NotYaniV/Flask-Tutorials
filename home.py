from flask import Flask,url_for,redirect

app = Flask(__name__)

# home page
@app.route("/")
def home():
    return "HELLO PYTHON PAGE <h1>HELLO</h1>"


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




