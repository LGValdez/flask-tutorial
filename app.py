from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session
from model.user.user import USER_LIST
from model.user.user_tools import search_user, get_userdata

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)


def get_kwargs(**values):
    kwargs = {}
    for key in values:
        kwargs[key] = values[key]
    return kwargs

@app.route("/")
def home():
    kwargs = get_kwargs(data={"current": "home"})
    return render_template("index.html", **kwargs)

@app.route("/contacts")
def contacts():
    kwargs = get_kwargs(data={
        "current": "contacts",
        "contacts": USER_LIST
    })
    return render_template("contacts/contacts.html", **kwargs)

@app.route("/login", methods=["POST", "GET"])
def login():
    data = {"current": "login"}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = search_user(username, password)
        if user_id:
            session.permanent = True
            session["user_id"] = user_id
            return redirect(url_for("profile"))
        else:
            data["failed"] = True
    kwargs = get_kwargs(data=data)
    return render_template("login/login.html", **kwargs)

@app.route("/profile")
def profile():
    if "user_id" in session:
        kwargs = get_kwargs(data={
            "current": "profile",
            "user": get_userdata(session["user_id"]),
            })
        return render_template("profile/profile.html", **kwargs)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
