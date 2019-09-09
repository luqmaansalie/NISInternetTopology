from ripe.atlas.sagan import Result
from ripe.atlas.sagan.traceroute import TracerouteResult, Hop, Packet
import json, traceback
import geoip2.database

readerASN = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-ASN_20190827/GeoLite2-ASN.mmdb')
readerCity = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-City_20190903/GeoLite2-City.mmdb')
readerCountry = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-Country_20190827/GeoLite2-Country.mmdb')

allnodes = "iata,name,city,country,latitude,longitude,s\n"
storedlinks = {}
storedASNs = {}
countrylinks = {}

def getCityName(dict):
	if bool(dict):
		return dict['en']
	return ""

def process_traceroute(rr, mID, sourceCountry):
	global allnodes
	global storedlinks
	global storedASNs
	global countrylinks

	result = Result.get(rr)
	hopcount = len(result.hops)

	responseASN = readerASN.asn(result.origin)
	asn = responseASN.autonomous_system_number
	name = responseASN.autonomous_system_organization.replace(",", "")

	#print(asn)

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
		name = responseASN.autonomous_system_organization.replace(",", "")

		link = source + "," + str(asn)

		if link in storedlinks:
			storedlinks[link] += 1
		else:
			storedlinks[link] = 1

		clink = sourceCountry + "_" + source + "," + str(asn)

		if clink in countrylinks:
			countrylinks[clink] += 1
		else:
			countrylinks[clink] = 1

		if asn not in storedASNs:
			storedASNs[asn] = sourceCountry
		elif sourceCountry not in storedASNs[asn]:
			storedASNs[asn] += sourceCountry
		
		allnodes += str(asn) + "," + name + "," + getCityName(rCity.city.names) + "," + getCityName(rCity.country.names) + ","
		allnodes += str(rCity.location.latitude) + "," + str(rCity.location.longitude) + "," + "replace" + str(asn) + "here" + "\n"
		source = str(asn)

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intertracerouteresults.json", "r")
lines = f.readlines()
f.close()

for l in lines:
	if len(l) > 1:
		tmp = l.split("~")
		l = tmp[2]
		source = tmp[1]
		mID = tmp[0]
		json_array = json.loads(l)
		for item in json_array:
			process_traceroute(item, mID, source)

for key, value in storedASNs.items():
	allnodes = allnodes.replace("replace" + str(key) + "here", value)

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/nodesinter.csv", 'w')
f.write(allnodes)
f.close()

# =========================

c = "All"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in storedlinks.items():
	f.write(key + "," + str(value) + "\n")
f.close()

c = "Mozambique"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Morocco"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Tanzania"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Ghana"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Algeria"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Senegal"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Kenya"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Nigeria"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "Egypt"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()

c = "SA"
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/linksinter" + c + ".csv", 'w')
f.write("origin,destination,count\n")

for key, value in countrylinks.items():
	if c in key:
		f.write(key[len(c)+1:] + "," + str(value) + "\n")

f.close()
