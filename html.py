import urllib.request
a=input("enter url ") #eisagei url selidas
webp= urllib.request.urlopen(a)
#diabazo url kai psaxno links
html=str(webp.read())
import re
li=len(re.findall("((http|ftp)s?://.*?)",html))
lc=len(re.findall("</p>",html)) +len(re.findall("<br>",html))
print ("links :", li)
print ("line changes:", lc)
