from twython import Twython

def search_hashtag(hashtag, cant):
	TWITTER_APP_KEY = '' #supply the appropriate value
	TWITTER_APP_KEY_SECRET = '' 
	TWITTER_ACCESS_TOKEN = ''
	TWITTER_ACCESS_TOKEN_SECRET = ''

	t = Twython(app_key=TWITTER_APP_KEY, 
				app_secret=TWITTER_APP_KEY_SECRET, 
				oauth_token=TWITTER_ACCESS_TOKEN, 
				oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

	search = t.search(q=hashtag,   #**supply whatever query you want here**
					  count=cant)

	tweets = search['statuses']
	return tweets
	
def main():
	print search_hashtag("#steam",20)
	  
if __name__ == '__main__':
    main()