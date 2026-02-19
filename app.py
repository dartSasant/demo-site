from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dev-secret-key-12345'

csrf = CSRFProtect(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "admission"

mysql = MySQL(app)

class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    parent_name = StringField("Parent Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    grade = IntegerField("Grade", validators=[DataRequired()])
    address = TextAreaField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit Application")

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/admission", methods=["GET", "POST"])
def admission():
    form = RegistrationForm()

    if form.validate_on_submit():
        full_name = form.full_name.data
        parent_name = form.parent_name.data     
        grade = form.grade.data
        address = form.address.data
        phone = form.phone.data
        dob = form.dob.data
        email = form.email.data

        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO school (full_name, parent_name, grade, address, phone, dob, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (full_name, parent_name, grade, address, phone, dob, email))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for("admission"))
        except Exception as e:
            return f"Database Error: {e}"

    return render_template("admission.html", form=form)

@app.route('/gallary')
def gallary():
    return render_template("gallery.html")

@app.route('/newsLetter')
def newsLetter():
    return render_template("newsLetter.html")

@app.route('/notice')
def notice():
    return render_template("notice.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)