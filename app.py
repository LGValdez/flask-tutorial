from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

class User():
    def __init__(self, **data):
        self.name = data.get("name", "")
        self.mobile = data.get("mobile", "")
        self.is_admin = data.get("is_admin", False)


gabo = User(name="Gabo",
            mobile=60792029,
            is_admin=True)
danny = User(name="Danny",
             mobile=75115006,
             is_admin=False)
oliver = User(name="Oliver")
user_list = [gabo, danny, oliver]

@app.route("/")
def home():
    kwargs = {
        "current": "home"
    }
    return render_template("index.html", **kwargs)

@app.route("/users")
def users():
    kwargs = {
        "current": "users",
        "users": user_list
    }
    return render_template("users/users.html", **kwargs)

if __name__ == "__main__":
    app.run(debug=True)
