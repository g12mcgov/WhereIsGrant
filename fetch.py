## Fetch Twitter Data

import tweepy
import json 
from geopy import geocoders 

class Twitter():
	def __init__(self):
		self.api = ""

		## Consumer Credentials
		self.consumer_key = 'lZqAC2G5ReXqFD1G7VYqumbCv'
		self.consumer_secret = 'slijdIL4mMtz09Ism7eCurqfHbxJ8RaodvG6GbOhKlmdg2RWas'

		## Access Tokens 
		self.access_token = '45555007-dJKIsb3Lqt3h12XvZcPgDoG9dtzyy93Uq7djsG2Wq'
		self.access_token_secret = 'UH6VVIF56ei6y5ktAmkIw0wF7wlDUYEwwTXrfZksPpbvP'

	def login(self):
		## Authenticate App
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		self.api = tweepy.API(auth)

	def getUserTweets(self):
		status = self.api.user_timeline("SwedeDeamon", None, None, 1, None)

		itr = 0
		latLng = 0
		location = ""
		cityName = ""

		while(True):
			## Recursively check for the first Tweet with a location
			itr += 1
			location = status[itr].place

			## If we found a location, pull off the coordinates 
			if(location):
				cityName = status[itr].place.full_name
				latLng = status[itr].coordinates['coordinates']
				break
			else:
				pass
		
		## This should be a dict, but I don't feel like fooling with 
		## socket.io's acceptance of the data on the frontend...
		locationPacket = [
					latLng[0],
					latLng[1], 
					cityName
					]

		print locationPacket

		return locationPacket

## Debug Purposes 
'''
if __name__ == "__main__":
	temp = Twitter()
	temp.login()
	temp.getUserTweets()
'''
	
