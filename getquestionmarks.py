#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import socket
import sys
import httplib2
import dbmodule
#print "all modules imported successfully"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'

#print sys.argv
if len(sys.argv) > 1:
	searchurl = sys.argv[1]
else:
	searchurl = "http://cnn.com"
'''
searchurl = "http://www.foxnews.com/politics/2014/04/21/fox-news-poll-independents-more-likely-to-back-anti-obamacare-candidates/?intcmp=latestnews"
searchurl = "http://drudgereport.com"
searchurl = "http://msnbc.com"
searchurl = "http://cnn.com"
searchurl = "http://foxnews.com/index.html"
'''
headers = { 'User-Agent' : user_agent }

h = httplib2.Http(".cache")
resp, html = h.request(searchurl, "GET", headers=headers)
#print resp
#print content
#exit()
#req = urllib2.Request(searchurl, '', headers)
#html = urllib2.urlopen(req).read()



soup = BeautifulSoup(html)



count =0
for link in soup.find_all("a",""):
	if "?" in link.text:
		count = count +1
#		print link.text


print "Number of Question Marks Currently on " + searchurl + ":\t" + str(count)

# Update the database
dbmodule.update_site_count(searchurl,str(count))
