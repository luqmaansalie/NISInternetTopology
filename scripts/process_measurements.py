from ripe.atlas.sagan import Result
from ripe.atlas.sagan.traceroute import TracerouteResult, Hop, Packet
import json, sys, traceback
import geoip2.database

readerASN = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-ASN_20190827/GeoLite2-ASN.mmdb')
readerCountry = geoip2.database.Reader('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/GeoLite2-Country_20190827/GeoLite2-Country.mmdb')

allnodes = []
alllinks = []
alllinksidx = -1

def print_traceroute(rr):
	result = Result.get(rr)
	print(isinstance(result, TracerouteResult))
	print(result.af)
	print(result.destination_address)
	print(result.destination_name)
	print(result.end_time.isoformat())
	print(result.origin)
	print(result.firmware)
	print(result.measurement_id)
	print(result.probe_id)
	print(result.paris_id)
	print(result.protocol)
	print(result.total_hops)
	print(result.last_median_rtt)
	print(result.ip_path[3][1])
	print(result.hops[0].packets[0].destination_option_size)
	print(result.hops[0].packets[0].hop_by_hop_option_size)
	print(result.hops[0].packets[0].mtu)
	print(result.hops[3].index)
	print(result.hops[3].packets[0].origin)
	print(result.hops[3].packets[1].rtt)
	print(result.hops[3].packets[1].size)
	print(result.hops[3].packets[2].ttl)
	print(result.hops[-1].index)
	print("============================================================================")

def process_traceroute(rr):
	singlenode = {}
	singlelink = {}
	global alllinksidx
	global allnodes
	global alllinks

	result = Result.get(rr)
	hopcount = len(result.hops)
	
	#print(hopcount)
	#print(result.hops[0].packets[0].origin)
	#print(result.origin)

	responseASN = readerASN.asn(result.origin)
	asnID = str(responseASN.autonomous_system_number) + " - " + responseASN.autonomous_system_organization
	asn = responseASN.autonomous_system_number

	print(asnID)

	#responseCountry = readerCountry.country(result.origin)
	#print(responseCountry.country.iso_code)

	source = asnID

	singlenode["id"] = asnID
	singlenode["group"] = asn

	if singlenode not in allnodes:
		allnodes.append(singlenode.copy())

	responseASN = 0

	for i in range(hopcount):
		try:
			responseASN = readerASN.asn(result.hops[i].packets[0].origin)
		except:
			#print(traceback.format_exc())
			continue

		responseASN = readerASN.asn(result.hops[i].packets[0].origin)
		asnID = str(responseASN.autonomous_system_number) + " - " + responseASN.autonomous_system_organization
		asn = responseASN.autonomous_system_number

		#responseCountry = readerCountry.country(result.hops[i].packets[0].origin)
		#print(responseCountry.country.iso_code + " > " + str(asnID) + " > " + result.hops[i].packets[0].origin)

		singlenode["id"] = asnID
		singlenode["group"] = asn

		if singlenode not in allnodes:
			allnodes.append(singlenode.copy())

		singlelink["source"] = source
		singlelink["target"] = asnID
		

		if singlelink in alllinks:
			singlelink["value"] += 1
			alllinks.pop(alllinksidx)
			alllinksidx -= 1
		else:
			singlelink["value"] = 1

		alllinks.append(singlelink.copy())
		alllinksidx += 1

		source = asnID


f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/results.json", "r")
lines = f.readlines()
f.close()

for l in lines:
	if len(l) > 1:
		process_traceroute(l)

dictdata = {}

dictdata["nodes"] = allnodes
dictdata["links"] = alllinks

jsondata = json.dumps(dictdata)

#print(jsondata)

f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/processed.json", 'w')
f.write(jsondata)
f.close()