from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/0ab383a1d3ed3d18b384")
    return render_template("index.html", posts=response.json())


@app.route("/read/<title>/<subtitle>/<id>")
def read_blog(id, title, subtitle):
    response = requests.get(f"https://api.npoint.io/0ab383a1d3ed3d18b384/{id}")
    json = response.json()
    print(json)
    return render_template("post.html", title=title, subtitle=subtitle, body=json["body"])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return f"<h1>{request.form['username']}</h1><h2>{request.form['password']}</h2>"
    else:
        return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
