import urlparse
import urllib
from bs4 import BeautifulSoup

#What URL are we going to visit?
url = "http://bbc.co.uk"

#Keep track of URL's we're visiting
urls = [url]
visited = [url]

#Create a stack that the program can run through to find URL's
while len(urls) > 0 :
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext, "html.parser")

	urls.pop(0)
	print len(urls)

	#Find Links
	for tag in soup.findAll('a',href=True):
		tag ['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

print visited