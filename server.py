import tornado.ioloop
import tornado.web
from twitter_test import search_hashtag
import tornado.template
import tornado.httpserver
import os
import os.path
import re
from replacer import tweet_replace_links

loader = tornado.template.Loader(os.path.join(os.getcwd(), "templates"))

class Templates(object):
	tweet_list = loader.load("tweet_list.html")
	


class MainHandler(tornado.web.RequestHandler):
    def get(self):
		count_str = self.get_argument("count", default=50)
		count = int(count_str)

		hashtag = self.get_argument("hashtag", default="python")
		if not hashtag.startswith("#"):
			hashtag = "#" + hashtag
		
		tweets = search_hashtag(hashtag,count)
		for t in tweets:
			#t['text'] = re.sub(r'(http+[^ ]+[a-zA-Z0-9])+.+[a-zA-Z0-9]',r'<a href="\1">\1</a>', t['text'])
			t['text'] = tweet_replace_links(t)
		html = loader.load("tweet_list.html").generate(tweets = tweets, count=count, hashtag = hashtag[1:])
		self.write(html)


def main():
	application = tornado.web.Application([
	(r"/", MainHandler),
	])
	http_server = tornado.httpserver.HTTPServer(application)
	port = int(os.environ.get("PORT", 5000))
	http_server.listen(port)
	tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
	main()
"""
application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

"""
