## Fetch Twitter Data

import tweepy
import json 
from geopy import geocoders 

class Twitter():
	def __init__(self):
		self.api = ""

	def login(self):
		## Credentials 
		consumer_key = 'lZqAC2G5ReXqFD1G7VYqumbCv'
		consumer_secret = 'slijdIL4mMtz09Ism7eCurqfHbxJ8RaodvG6GbOhKlmdg2RWas'

		## Access Tokens 
		access_token = '45555007-dJKIsb3Lqt3h12XvZcPgDoG9dtzyy93Uq7djsG2Wq'
		access_token_secret = 'UH6VVIF56ei6y5ktAmkIw0wF7wlDUYEwwTXrfZksPpbvP'

		## Authenticate App
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		self.api = tweepy.API(auth)

	def getUserTweets(self):
		status = self.api.user_timeline("SwedeDeamon", None, None, 1, None)
		location = status[0].coordinates['coordinates']

		'''
		gn = geocoders.GeoNames()
		latLong = geocode(str(location))
		print latLong
		'''

		return location
	