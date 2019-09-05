from ripe.atlas.sagan import Result
from ripe.atlas.sagan.traceroute import TracerouteResult, Hop, Packet
import json, traceback
import geoip2.database

readerASN = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-ASN_20190827/GeoLite2-ASN.mmdb')
readerCity = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-City_20190903/GeoLite2-City.mmdb')
readerCountry = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-Country_20190827/GeoLite2-Country.mmdb')

allnodes = "iata,name,city,country,latitude,longitude\n"
storedlinks = {}

def getCityName(dict):
	if bool(dict):
		return dict['en']
	return ""

def process_traceroute(rr):
	global allnodes
	global storedlinks

	result = Result.get(rr)
	hopcount = len(result.hops)

	responseASN = readerASN.asn(result.origin)
	asn = responseASN.autonomous_system_number
	name = responseASN.autonomous_system_organization

	print(asn)

	source = str(asn)
	responseASN = 0

	for i in range(hopcount):
		try:
			responseASN = readerASN.asn(result.hops[i].packets[0].origin)
		except:
			#print(traceback.format_exc())
			continue

		responseASN = readerASN.asn(result.hops[i].packets[0].origin)
		rCity = readerCity.city(result.hops[i].packets[0].origin)
		#print(responseASN)
		#print(rCity)

		asn = responseASN.autonomous_system_number
		name = responseASN.autonomous_system_organization

		link = source + "," + str(asn)
		if link in storedlinks:
			storedlinks[link] += 1
		else:
			storedlinks[link] = 1
		
		allnodes += str(asn) + "," + name + "," + getCityName(rCity.city.names) + "," + getCityName(rCity.country.names) + "," + str(rCity.location.latitude) + "," + str(rCity.location.longitude) + "\n"
		source = str(asn)

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/results.json", "r")
lines = f.readlines()
f.close()

for l in lines:
	if len(l) > 1:
		process_traceroute(l)

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/nodes.csv", 'w')
f.write(allnodes)
f.close()

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/links.csv", 'w')
f.write("origin,destination,count\n")

for key, value in storedlinks.items():
	f.write(key + "," + str(value) + "\n")

f.close()