from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

class User():
    def __init__(self, **data):
        self.name = data.get("name", "")
        self.mobile = data.get("mobile", "")
        self.is_admin = data.get("is_admin", False)

@app.route("/")
def home():
    gabo = User(name="Gabo",
                mobile=60792029,
                is_admin=True)
    danny = User(name="Danny",
                 mobile=7511,
                 is_admin=False)
    oliver = User(name="Oliver")
    users = [gabo, danny, oliver]
    xargs = {
        "users": users
    }
    return render_template("index.html", **xargs)

if __name__ == "__main__":
    app.run()
