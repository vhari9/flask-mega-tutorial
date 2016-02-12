## What is this?

Working out the [Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
for fun and giggles. 

Actually, I already know how to spawn a Flask web app just fine. Am working out 
the above said tutorial because: the 
[Flaskr](http://github.com/sindhus/flaskr) the hobby project I have 
uses libraries like [Flask-lastuser](http://github.com/hasgeek/flask-lastuser) 
which takes care of user management...which is not a bad thing *but* I want to 
write code to do user management naively or using other libraries as well. Eh! or maybe I just like spawning toy Flask apps and hence the repo!

Note: Some stuff like configuration and the entry point to the app 
(`runserver.py`) is the way I like my project to be organised. The tutorial 
may or may not follow the same.

## How to run this locally?

1. Clone this repo
    $ git clone git@github.com:sindhus/flask-mega-tutorial.git

2. Change into the directory...
    $ cd flask-mega-tutorial

3. Setup and enter the [Virtual environment](docs.python-guide.org/en/latest/dev/virtualenvs/)
    $ virtualenv -p `which python2` ma  && source ma/bin/activate

4. Install project requirements
    $ pip install -r requirements.txt

5. Run the app!
    $ python runserver.py
