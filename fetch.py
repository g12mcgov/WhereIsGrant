## Fetch Twitter Data

import tweepy
import json 
from geopy.geocoders import Nominatim 

class Twitter():
	def __init__(self):
		self.api = ""

		## Consumer Credentials
		self.consumer_key = 'lZqAC2G5ReVYqumbCv'
		self.consumer_secret = 'slijdIL4mMxJ8RaodvG6GbOhKlmdg2RWas'

		## Access Tokens 
		self.access_token = '45555007-dJKIsb3Lqt3h12XvZcPgDoG9dtzyy93Uq7djsG2Wq'
		self.access_token_secret = 'UH6VVIF56ei6y5ktAmkIw0wF7wlDUYEwwTXrfZksPpbvP'
		
		## Create GeoLocater instance
		self.geolocater = Nominatim()


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
			location = status[itr].place

			## If we found a location, pull off the coordinates 
			if(location):
				cityName = status[itr].place.full_name

				## We generalize the address here by sending the city name
				## to geocoders and getting the general lat/long back
				geo_response = self.geolocater.geocode(str(cityName))
				lat = geo_response.latitude
				lng = geo_response.longitude

				break
			else:
				pass

			itr += 1
		
		## This should be a dict, but I don't feel like fooling with 
		## socket.io's acceptance of the data on the frontend...
		locationPacket = [
					lng,
					lat, 
					cityName
					]

		print locationPacket

		return locationPacket


## Debug Purposes 

if __name__ == "__main__":
	temp = Twitter()
	temp.login()
	temp.getUserTweets()

	
