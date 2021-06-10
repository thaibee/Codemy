from django.shortcuts import render
import calendar
from datetime import datetime
YEAR_NOW = datetime.now().year
MONTH_NOW = datetime.now().strftime('%B')

def home(request, year = YEAR_NOW, month = MONTH_NOW):

    name = 'Andrey'
    month = month.title()
    month_n = list(calendar.month_name).index(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month_n)
    time_now = datetime.now().strftime('%I:%M:%p')
    return render(request, 'home/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'time_now': time_now,
        'year_now': YEAR_NOW
    })
