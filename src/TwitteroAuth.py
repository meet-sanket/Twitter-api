import tweepy


token = ""

def generate_token():
	consumer_key = ""
	consumer_secret = ""

	auth  = tweepy.OAuthHandler(consumer_key,consumer_secret)
	api = tweepy.API(auth)
	token =auth.set_access_token(access_token,access_token_secret) 
	return token

if token == null:
	token  = generate_token()
