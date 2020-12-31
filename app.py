from flask import Flask, redirect, url_for, render_template, request
from model.user.user import USER_LIST
from model.user.user_tools import search_user, get_userdata

app = Flask(__name__)

@app.route("/")
def home():
    data = {"current": "home"}
    kwargs = {"data": data}
    return render_template("index.html", **kwargs)

@app.route("/contacts")
def contacts():
    data = {
        "current": "contacts",
        "contacts": USER_LIST
    }
    kwargs = {"data": data}
    return render_template("contacts/contacts.html", **kwargs)

@app.route("/login", methods=["POST", "GET"])
def login():
    data = {"current": "login"}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = search_user(username, password)
        if user_id:
            return redirect(url_for("profile", user_id=user_id))
        else:
            data["failed"] = True
    kwargs = {"data": data}
    return render_template("login/login.html", **kwargs)

@app.route("/profile/<user_id>")
def profile(user_id):
    data = {"user": get_userdata(user_id)}
    kwargs = {"data": data}
    return render_template("profile/profile.html", **kwargs)

if __name__ == "__main__":
    app.run(debug=True)
