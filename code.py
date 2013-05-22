import web
from web import form

import requests
import urllib
import simplejson
import folium
import time

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
	form.Textbox('Search'), 
	form.Textbox('Location'), 
) 

class index: 
	def GET(self): 
		form = myform()
		# make sure you create a copy of the form by calling it (line above)
		# Otherwise changes will appear globally
		return render.formtest(form)

	def POST(self): 
		form = myform() 
		if not form.validates(): 
			return render.formtest(form)
		else:
			searchvalue = form['Search'].value
			alllocation = ['New York City','Seattle','San Francisco', 'Boston', 'Austin', 'Chicago']
			alllocation.append(str(form['Location'].value))
			map_osm = folium.Map(location=[40.84706,-96.064453], zoom_start=4)
			for i in range(len(alllocation)):
				locgit = alllocation[i].replace(' ', '+')

				url = 'https://jobs.github.com/positions.json?description=' + searchvalue + '&location=' + locgit

				r = requests.get(url)
				resp = r.json()

				htmlinput = urllib.quote(alllocation[i])
				url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
				jsonResponse = simplejson.load(urllib.urlopen(url2))
				lati = jsonResponse[0]['lat']
				longi = jsonResponse[0]['lon']

				map_osm.simple_marker([lati, longi], popup='Number of ' + str(searchvalue) + ' jobs in ' + alllocation[i] + ': ' + str(len(resp)))

			mapurl = str(time.time()).replace('.','') + '.html'
			map_osm.create_map(path = 'static/' + mapurl)

			return render.mapoutput(mapurl, searchvalue)

if __name__=="__main__":
	web.internalerror = web.debugerror
	app.run()