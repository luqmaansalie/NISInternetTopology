from ripe.atlas.sagan import Result
from ripe.atlas.sagan.ping import PingResult, Packet
import json
import sys
import traceback
import geoip2.database

readerASN = geoip2.database.Reader(
	'C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-ASN_20190827/GeoLite2-ASN.mmdb')
readerCity = geoip2.database.Reader(
	'C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-City_20190903/GeoLite2-City.mmdb')
readerCountry = geoip2.database.Reader(
	'C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-Country_20190827/GeoLite2-Country.mmdb')

hdrs = "msmID,source,name,city,country,latitude,longitude,rtt_average,rtt_median\n"
allnodes = hdrs
storedsites = {}

def test_ping_0(rr):
	result = Result.get(rr)
	print(result.af)
	print(result.rtt_average)
	print(result.rtt_median)
	print(result.destination_address)
	print(result.destination_name)
	print(result.duplicates)
	print(result.origin)
	print(result.firmware)
	print(result.seconds_since_sync)
	print(result.rtt_max)
	print(result.rtt_min)
	print(result.measurement_id)
	print(result.probe_id)
	print(result.protocol)
	print(result.packets_received)
	print(result.packets_sent)
	print(result.packet_size)
	print(result.step)
	print(result.created)
	print(result.packets)

def getCityName(dict):
	if bool(dict):
		return dict['en']
	return ""

def process_ping(rr, msmID, source):
	global allnodes
	global storedsites

	result = Result.get(rr)
	responseASN = readerASN.asn(result.origin)
	rCity = readerCity.city(result.origin)
	rCountry = readerCountry.country(result.origin)

	asn = str(responseASN.autonomous_system_number) + " " + responseASN.autonomous_system_organization.replace(",", "")
	ip = result.destination_name

	print(ip)

	av = ip + "_av"
	md = ip + "_md"
	ct = ip + "_ct"

	if result.rtt_median is None:
		return

	#print(result.rtt_median)

	if ip in storedsites:
		storedsites[ct] += 1
		storedsites[av] += result.rtt_average
		storedsites[md] += result.rtt_median
	else:
		storedsites[ip] = ip
		storedsites[ct] = 1
		storedsites[av] = result.rtt_average
		storedsites[md] = result.rtt_median
	
	city = ip + "_city"
	country = ip + "_country"
	lat = ip + "_lat"
	lon = ip + "_lon"
	
	storedsites[city] = getCityName(rCity.city.names)
	storedsites[country] = rCountry.country.name
	storedsites[lat] = str(rCity.location.latitude)
	storedsites[lon] = str(rCity.location.longitude)

	#print("av: " + str(result.rtt_average))
	#print("md: " + str(result.rtt_median))

	allnodes += msmID + "," + source + "," + asn + "," + getCityName(rCity.city.names) + "," + rCountry.country.name + ","
	allnodes += str(rCity.location.latitude) + "," + str(rCity.location.longitude) + "," + str(result.rtt_average) + "," + str(result.rtt_median) + "\n"

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/interresults.json", "r")
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
			process_ping(item, mID, source)

ff = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/interprocessed_flat.csv", 'w')
ff.write(allnodes)
ff.close()

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/interprocessed.csv", 'w')
f.write(hdrs)

for key, value in storedsites.items():
	if "_" not in key:
		a = storedsites[key + "_av"] / storedsites[key + "_ct"]
		m = storedsites[key + "_md"] / storedsites[key + "_ct"]

		f.write(value + "," + storedsites[key + "_city"] + "," + storedsites[key + "_country"] + "," + storedsites[key + "_lat"] + "," + storedsites[key + "_lon"] + ",")
		f.write(str(a) + "," + str(m) + "\n")

f.close()