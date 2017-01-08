import urllib.request
 
Webseite = "http://www.boerse-online.de/aktie/Volkswagen_vz-Aktie"
t = urllib.request.urlopen(Webseite)
 
print(t.read())

print(t.read())

