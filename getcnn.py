#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib
import socket
import sys
# print "all modules imported successfully"

if len(sys.argv) > 1:
	searchurl = sys.argv[1]
else:
	searchurl = "http://cnn.com"
searchurl = "http://foxnews.com/index.html"
f = urllib.urlopen(searchurl)
html = f.read()
soup = BeautifulSoup(html)

count =0
for link in soup.find_all("a",""):
	print link.text
	if "?" in link.text:
		count = count +1
#		print link.text

print "\n\nNumber of Question Marks Currently on " + searchurl + ":\t" + str(count)
