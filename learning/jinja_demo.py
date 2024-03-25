from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    rand_num = random.randint(0, 10)
    return render_template("index.html", num=rand_num, copyright_year=dt.now().year)


def get_gender_for(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()["gender"]


@app.route('/guess/<name>')
def guess(name):
    capitalized_name = str.capitalize(name)
    gender = get_gender_for(name)
    age = get_age_for(name)
    return render_template("agify.html", name=capitalized_name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print (num)
    response = requests.get("https://api.npoint.io/1f647dd9834403573153")
    return render_template("blog.html", posts=response.json())


def get_age_for(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]
    return age


if __name__ == "__main__":
    app.run(debug=True)
