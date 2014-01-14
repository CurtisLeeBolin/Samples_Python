#!/bin/python3
# URL_title_extractor.py
# URL title extractor with The Open Graph protocol support
#
#
#
# Many sites like Instagram use The Open Graph protocol for the title.
# e.g. http://instagram.com/sarah3llen source
########################################################################
# <title>Instagram</title>
# <meta property="og:title" content="sarah3llen on Instagram" />
########################################################################
# In the above example you can see there is a title tag and meta tag
# with property="og:title".  The OGP title is more descriptive and is
# the one a modern browser will display in the title bar.

import html.parser, urllib.request

class MyHTMLParser(html.parser.HTMLParser):
	def __init__(self):
		html.parser.HTMLParser.__init__(self)
		self.a = False
		self.title = None
		self.ogpTitle = None

	def handle_starttag(self, tag, attrs):
		if tag == 'title':
			self.a = True
		elif tag == 'meta':
			if ('property', 'og:title') in attrs:
				for each in attrs:
					if each[0] == 'content':
						self.ogpTitle = each[1]
		else:
			pass

	def handle_data(self, data):
		if self.a:
			self.a = False
			self.title = data

parser = MyHTMLParser()

response = urllib.request.urlopen('http://instagram.com/sarah3llen')
data = response.read()
html = data.decode('utf-8')

parser.feed(html)

if parser.ogpTitle:
	title = parser.ogpTitle
else:
	title = parser.title

print(title)
