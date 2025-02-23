from pack import app
from flask import render_template, flash, redirect
from pack.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel reyiz'} 
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/time')
def time():
    import datetime
    import calendar
    now = datetime.datetime.now()

    date_text = now.day, calendar.month_name[now.month], now.year
    time_text = now.hour, now.minute
    datetime = {'date' :date_text, 'time' :time_text}

    return render_template ("time.html", title="Date-Time", datetime=datetime)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect ('/index')
    else:
        print("ggwp")
    return render_template('login.html', title="Sign in!", form=form)