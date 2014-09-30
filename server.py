import tornado.ioloop
import tornado.web
from twitter_test import search_hashtag
import tornado.template
import os
import os.path

loader = tornado.template.Loader(os.path.join(os.getcwd(), "templates"))

class Templates(object):
	tweet_list = loader.load("tweet_list.html")
	


class MainHandler(tornado.web.RequestHandler):
    def get(self):
		count_str = self.get_argument("count", default=10)
		count = int(count_str)

		hashtag = self.get_argument("hashtag", default="python")
		if not hashtag.startswith("#"):
			hashtag = "#" + hashtag
		
		tweets = search_hashtag(hashtag,count)
		html = loader.load("tweet_list.html").generate(tweets = tweets, count=count, hashtag = hashtag[1:])
		self.write(html)

	
application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
	
	