from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from forms import RegistrationForm
from models import User, db

app = Flask(__name__)
app.config['SECRET_KEY'] = b'5b1aa6a7a0ea7d0b36cd5499146ab901ee959c04ca90531b4025169cf29a73ff'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../mydatabase.db'
db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html', title='Начальная страница')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.user_name.data
        surname = form.user_surname.data
        email = form.email.data
        password = form.password.data
        db.session.add(User(user_name=form.user_name.data, user_surname=form.user_surname.data, email=form.email.data,
                            hashed_psw=form.password.data))
        db.session.commit()
        print('OK')
        print(email, password, name, surname)
    return render_template('register.html', form=form)



@app.cli.command('create_db')
def one_time_run():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)



