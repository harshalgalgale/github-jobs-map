import requests
import time
import requests
import urllib
import simplejson
import folium


search = 'Ruby'
alllocation = ['New York City','Seattle','San Francisco', 'Boston', 'Austin', 'Chicago']
map_osm = folium.Map(location=[40.84706,-96.064453], zoom_start=4)
for i in range(len(alllocation)):
	locgit = alllocation[i].replace(' ', '+')

	url = 'https://jobs.github.com/positions.json?description=' + search + '&location=' + locgit

	r = requests.get(url)
	resp = r.json()

	htmlinput = urllib.quote(alllocation[i])
	url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
	jsonResponse = simplejson.load(urllib.urlopen(url2))
	lati = jsonResponse[0]['lat']
	longi = jsonResponse[0]['lon']

	map_osm.simple_marker([lati, longi], popup='Number of ' + search + ' jobs in ' + alllocation[i] + ': ' + str(len(resp)))

map_osm.create_map(path='osm1.html')
