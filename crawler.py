#from urllib.request import urlopen
from urllib2 import urlopen
import re

myurl = 'https://www.dn.no/'
html = urlopen(myurl).read()

m = re.search('Indeks:.+?<span>(.+?)</span>', html)
print("Oslo Bors Indeks:", m.group(1)) 
m = re.search('Oljepris:.+?<span>(.+?)</span>', html)
print("Oljepris:", m.group(1))
