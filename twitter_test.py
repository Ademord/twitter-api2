from twython import Twython

def search_hashtag(hashtag, cant):
	TWITTER_APP_KEY = 'KlERfpepfwGbr6mFXnJmOlGjB' #supply the appropriate value
	TWITTER_APP_KEY_SECRET = '1eWnSzH4u4uwGghVVDFjkbPnr81pY28dggbHdW2vlNuBByymxU' 
	TWITTER_ACCESS_TOKEN = '73236009-dRCxQMdhcty1Vt2khgAD2umxfLU1azwIuMNVoX1Q7'
	TWITTER_ACCESS_TOKEN_SECRET = 'NRS2pCuGMDy12P5se6qF3u57Ig5vSEiSM7DcnIscAnn2K'

	t = Twython(app_key=TWITTER_APP_KEY, 
				app_secret=TWITTER_APP_KEY_SECRET, 
				oauth_token=TWITTER_ACCESS_TOKEN, 
				oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

	search = t.search(q=hashtag,   #**supply whatever query you want here**
					  count=cant)

	tweets = search['statuses']
	return tweets
	
def main():
	search_hashtag("#steam",5)
	  
if __name__ == '__main__':
    main()