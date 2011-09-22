import urllib
import simplejson
import xml.dom.minidom as minidom

def searchTweets(query):
	search=urllib.urlopen("http://search.twitter.com/search.json?q="+query)
	di = simplejson.loads(search.read())
	for result in di["results"]:
		print ">",result["text"],"\n"

def printTweets(username):
	timeline_xml = urllib.urlopen("http://twitter.com/statuses/user_timeline.xmlscreen_name="+username)
	doc = minidom.parse(timeline_xml) # we're using the twitter xml format
	tweets = doc.getElementsByTagName("text") # tweet text is in ...
	
	for tweet in tweets:
		print "tweet:",tweet.childNodes[0].data,"\n"

if __name__=="__main__":
	while True:
		q=input('Que quieres hacer?: 1-buscar 2-ver tweets: ')
		
		if q==1:
			x=raw_input('Que quieres buscar?: ')
			searchTweets(x)
		elif q==2:
			x=raw_input('Cual es tu usuario?: ')
			printTweets(x)
		else:
			break
	print "Bye"
	print
