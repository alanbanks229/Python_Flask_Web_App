"""
Jun 24, 2020
python_flask.py
SDEV_300, lab6
Alan Banks

In this application I play around with fetch calls to NUMBERS API,
which will create the ordered list of prompts a user will see on the
homepage.

The other navigation link, will be a page that will show CSS anchor cards
that are somewhat dynamic.


# Update Jun 27: Found another way to update HH:MM:SS without page refresh
# Now using Javascript to render HH:MM:SS format. Because of this there is
# no need to pass datetime_est to home.html, line 62

"""


from datetime import date
import random
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    home will be the launch page
    it will return home.html along with a
    parent html file "layout.html"
    """
    #today will serve as our basis to achieve the textual day format
    today = date.today()

    #below serves as a way for program to receive EST time
    # est = pytz.timezone('America/New_York')
    # datetime_est = datetime.now(est)

    #Below is the URL where I'll make fetch calls (GET requests)
    url = "http://numbersapi.com/random/math"

    #list_of_facts will contain trivia facts from url
    list_of_facts = []

    #adding 3 random facts to our Array, 'list_of_facts'
    for counter in range(1, 4):
        print(counter)
        fetch = urllib.request.urlopen(url)
        list_of_facts.append(fetch.read().decode('utf-8'))

    #passing in 2 variables which will be used in 'home.html'
    return (
        render_template(
            'home.html',
            randomfacts=list_of_facts,
            DATE=today.strftime("%B %d, %Y"),
            # current_minute=datetime_est.strftime("%H:%M")
        )
    )

#declaring our second route in this program
@app.route('/other/')
def other():
    """
    This method is responsible for rendering our other.html page
    It will return an array of values we will use for our anchor tags
    specifically for the  <a href= /> values.
    """
    list_of_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/c/inanutshell/videos",
        "https://www.google.com/"
    ]
    # shuffling the links to contribute to the "mystery/guessing"
    # on the other.html page
    random.shuffle(list_of_links)
    return render_template('other.html', cool_links=list_of_links)

if __name__ == '__main__':
    app.run(debug=True)
