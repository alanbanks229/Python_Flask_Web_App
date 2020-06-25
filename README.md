# Python_Flask_Web_App

This is my very first web application implementing the usage of Flask web framework.

To make this website work properly make sure you.
pip install (flask, pytz, urllib, random and datetime)
I'm pretty sure flask is actually the only thing that needs to be imported on your machine.
Everything else should be installed by default.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

This is a basic application with two routes ('/') and ('/other/')

The launch page will display math trivia, fetched from Numbers API which is free to fetch from.
To render new Trivia you have to refresh the page, hopefully down the line I'll find a way to make it
fetch and not reset the server

The '/other' page displays clickable anchor tags (made to look like 'div' tags) and will redirect a user to
some of my favorite pages on the internet! As of now there are only 3 links, but they will render in a random order
so you won't know what card leads to what until you click on it :)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Reflection:
Starting off with flask was quite the struggle, coming from a ReactJS and JS mindset. However I found aspects of it very
similar to writing frontend code with ruby ERB or (eRUBY) by embedding Ruby code in an HTML document.
