[WhereisGrant](http://whereisgrant.herokuapp.com)
=================
!['Site Preview'](http://i1158.photobucket.com/albums/p618/g12mcgov/Screenshot2014-12-18154627.png)
============

What is it?
============
A live tracker to show where I'm at on a map. Inspired by cdzombak's app, WhereIsChris.

[whereisgrant.herokupapp.com](http://whereisgrant.herokuapp.com)

One day it will have its own custom URL

Where was it built?
============
In an airport. Heathrow to be specific. I had a 4 hour wait for my flight :/

How does it work?
============
It's a Flask app. It uses Tweepy to fetch recent Tweets from my account every hour, and parses for location data. It then pushes up the data through Socket.io to the frontend, where the Google Maps API renders the data to plot me on the map.
It's really simple. It's all hosted on Heroku too. 

Room for Improvement?
============
This is a bare-bones project I whipped up because I was bored. I'll change it to make it look prettier and mobile-optimized. Maybe even add it as a page to my personal site, [grantmcgovern.com](http://www.grantmcgovern.com).
