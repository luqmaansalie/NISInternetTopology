from ripe.atlas.sagan import Result
from ripe.atlas.sagan.traceroute import TracerouteResult, Hop, Packet
import json, traceback
import geoip2.database

readerASN = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-ASN_20190827/GeoLite2-ASN.mmdb')
readerCity = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-City_20190903/GeoLite2-City.mmdb')
readerCountry = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-Country_20190827/GeoLite2-Country.mmdb')

hdrs = "msmID,source,name,city,country,latitude,longitude,hops\n"
allnodes = hdrs
storedsites = {}

def getCityName(dict):
    if bool(dict):
        return dict['en']
    return ""

def process_tr(rr, msmID, source):
	global allnodes
	global storedsites

	result = Result.get(rr)
	responseASN = readerASN.asn(result.origin)
	rCity = readerCity.city(result.origin)
	rCountry = readerCountry.country(result.origin)

	asn = str(responseASN.autonomous_system_number) + " " + responseASN.autonomous_system_organization.replace(",", "")
	ip = result.destination_name

	print(ip)

	allnodes += msmID + "," + source + "," + asn + "," + getCityName(rCity.city.names) + "," + rCountry.country.name + ","
	allnodes += str(rCity.location.latitude) + "," + str(rCity.location.longitude) + "," + str(len(result.hops)) + "\n"

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
			process_tr(item, mID, source)

ff = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intertracerouteprocessed_flat.csv", 'w')
ff.write(allnodes)
ff.close()