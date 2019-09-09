from datetime import datetime
import urllib.request
#from ripe.atlas.cousteau import (
	#AtlasResultsRequest
#)

#fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/results.json', 'w')
#f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/data.txt", "r")

#fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intratracerouteresults.json', 'w')
#f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intratraceroute.txt", "r")

fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intertracerouteresults.json', 'w')
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/intertraceroute.txt", "r")

#fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/interresults.json', 'w')
#f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/interping.txt", "r")

lines = f.readlines()
f.close()

for l in lines:
	tmp = l.replace("\n", "").split("~")
	kwargs = {
		"msm_id": tmp[0]
	}
	
	#is_success, results = AtlasResultsRequest(**kwargs).create()

	print(tmp[0])

	fc.write(tmp[1] + "~" + tmp[2] + "~" + urllib.request.urlopen("https://atlas.ripe.net/api/v2/measurements/" + tmp[0] + "/results/?format=json&filename=RIPE-Atlas-measurement-" + tmp[0] + ".json").read().decode('utf-8') + "\n")
	#print(str(results))

fc.close()