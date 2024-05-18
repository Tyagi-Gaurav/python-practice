import flask
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_login import LoginManager, login_required, login_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug import security
from werkzeug.security import check_password_hash

from user import User

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret-key-goes-here'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pwd_hash = security.generate_password_hash(request.form.get("password"))
        new_user = User(email=request.form.get("email"),
                        password=pwd_hash,
                        name=request.form.get("name"))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets", name=request.form.get("name")))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            passwords_match = check_password_hash(password=request.form.get("password"), pwhash=user.password)
            print(f"pwd match: {passwords_match}")
            if passwords_match is True:
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                return render_template("login.html", error="Invalid Credentials")
        else:
            return render_template("login.html", error="Invalid Credentials")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", user_name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    redirect(url_for("home"))


@app.route('/download')
def download():
    return send_from_directory(app.static_folder, "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
