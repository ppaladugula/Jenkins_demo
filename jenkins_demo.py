import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 
access_key = "1194104096518787072-uJ9KiTZaJl4HCosfjCnDsHyFflw9GQ"
access_secret =  "CcLmcbJUAZuNig3tDKSPrL289ZadfWsmjtkZVU78gs6J2"
consumer_key =  "32DXZaQ0bBnuIMn3eviE9N3VU"
consumer_secret =  "dqyPdSetrbQFRpzS3Zd4xdIxPVbkgQK6m5VB1Bs5crclHECyp4"

# Function to extract tweets 
def get_tweets(username): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 20 tweets to be extracted 
		number_of_tweets=20000
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		tmp=[] 

		# create array of tweet information: username, 
		# tweet id, date/time, text 
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		for j in tweets_for_csv: 

			# Appending tweets to the empty array tmp 
			tmp.append(j) 

		# Printing the tweets 
		print(tmp) 


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("Apache_hadoop") 
