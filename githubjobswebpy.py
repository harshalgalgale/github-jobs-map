import requests
import time
import requests
import urllib
import simplejson
import folium
import time

timelist = []
start = time.time()
search = 'Ruby'
alllocation = ['New York City','Seattle','San Francisco', 'Boston', 'Austin', 'Chicago']
map_osm = folium.Map(location=[40.84706,-96.064453], zoom_start=4)
end1 = time.time()
timelist.append(end1 - start)
for i in range(len(alllocation)):
	end2 = time.time()
	locgit = alllocation[i].replace(' ', '+')

	url = 'https://jobs.github.com/positions.json?description=' + search + '&location=' + locgit

	r = requests.get(url)
	resp = r.json()

	end25 = time.time()
	timelist.append(end25 - end2)

	htmlinput = urllib.quote(alllocation[i])
	url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
	jsonResponse = simplejson.load(urllib.urlopen(url2))
	lati = jsonResponse[0]['lat']
	longi = jsonResponse[0]['lon']

	map_osm.simple_marker([lati, longi], popup='Number of ' + search + ' jobs in ' + alllocation[i] + ': ' + str(len(resp)))
	
	end3 = time.time()
	timelist.append(end3 - end25)

map_osm.create_map(path= str(time.time()).replace('.','') + '.html')

end4 = time.time()
timelist.append(end4 - end3)

print timelist