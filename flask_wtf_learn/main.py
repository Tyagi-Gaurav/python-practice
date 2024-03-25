from flask import Flask, render_template, request

from LoginForm import LoginForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        if loginForm.matches_credentials():
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=loginForm)


if __name__ == '__main__':
    app.run(debug=True)
