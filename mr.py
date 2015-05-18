import urllib2
import pymongo
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from pymongo import MongoClient

def get_db(): 
    client = MongoClient('mongodb://localhost:27017/')
    db=client.urlstore
    return db


data=get_db()


proxy_handler = urllib2.ProxyHandler({"https": "http://ipg_2011080:9685556845@192.168.1.107:3128"})
auth = urllib2.HTTPBasicAuthHandler()

opener = urllib2.build_opener(proxy_handler,auth,urllib2.HTTPHandler)
urllib2.install_opener(opener)





response = urllib2.urlopen('https://ideas.repec.org/s/oup/qjecon.html')
soup = BeautifulSoup(response)
count=0
for div in soup.findAll('div', attrs={'class':'panel-body'}):
   for link in div.find_all('a'):
        data.articles.insert({ '_id': count, 'item': link.get('href') })
        count=count+1
        
print "END";



    
