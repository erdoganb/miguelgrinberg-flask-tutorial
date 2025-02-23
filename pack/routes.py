from pack import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel reyiz'}
    return render_template('index.html', title="Home", user=user)

@app.route('/time')
def time():
    import datetime
    import calendar
    now = datetime.datetime.now()

    date_text = f"{now.day, calendar.month_name[now.month], now.year}"
    time_text = now.hour

    return f"Date is: {date_text, time_text}" 