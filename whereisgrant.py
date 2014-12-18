from gevent import monkey 
from flask import Flask, render_template, url_for, copy_current_request_context
from flask.ext.socketio import SocketIO, emit
from random import random
from time import sleep
from threading import Thread, Event
import tweepy

## Locals 
from fetch import Twitter  

__author__ = "Grant McGovern"

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000

socketio = SocketIO(application)

thread = Thread()
thread_stop_event = Event()
 
class RandomThread(Thread):
    def __init__(self):
        self.delay = 6
        super(RandomThread, self).__init__()
 
 	## Find Tweets every X amount of seconds
    def tweetFinder(self):
        print "Finding Tweets..."

        while not thread_stop_event.isSet():
        	twit = Twitter()
        	twit.login()
        	cityName = twit.getUserTweets()
        	print cityName
        	socketio.emit('newnumber', {'number': cityName}, namespace='/test')
        	sleep(self.delay)
 
    def run(self):
        self.tweetFinder()

@application.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread objects
    print "We're working"
    global thread
    print('Client connected')

    if not thread.isAlive():
 		print "Starting Thread"
 		thread = RandomThread()
 		thread.start()

if __name__ == '__main__':
	socketio.run(application)
