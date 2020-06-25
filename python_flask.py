"""
Jun 24, 2020
python_flask.py
SDEV_300, lab6
Alan Banks

to get css to update on refresh you have to input
command + shift + r
(this will reset browser cache, and update css file in browser.)

In this application I play around with fetch calls to NUMBERS API,
which will create the ordered list of prompts a user will see on the
homepage.
The other navigation link, will be a page that will show CSS anchor cards
that are somewhat dynamic.

"""


from datetime import date, datetime
import random
import urllib.request
import pytz
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    home will be the launch page
    it will return home.html along with a
    parent html file "layout.html"
    """
    today = date.today()
    est = pytz.timezone('America/New_York')
    datetime_est = datetime.now(est)
    #Below is URL where I make a GET request
    url = "http://numbersapi.com/random/math"
    list_of_facts = []
    for counter in range(1, 4):
        print(counter)
        fetch = urllib.request.urlopen(url)
        list_of_facts.append(fetch.read().decode('utf-8'))

    return (
        render_template(
            'home.html',
            randomfacts=list_of_facts,
            DATE=today.strftime("%B %d, %Y"),
            current_minute=datetime_est.strftime("%H:%M")
        )
    )


@app.route('/other/')
def other():
    """
    This method is responsible for rendering our other.html page
    it will return an array of href= values for our anchor tags
    within the other.html template file
    """
    list_of_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/c/inanutshell/videos",
        "https://www.google.com/"
    ]
    random.shuffle(list_of_links)
    return render_template('other.html', cool_links=list_of_links)

if __name__ == '__main__':
    app.run(debug=True)
