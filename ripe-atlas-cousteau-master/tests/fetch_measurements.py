from datetime import datetime
from ripe.atlas.cousteau import (
	AtlasResultsRequest
)

fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/results.json', 'w')
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/data.txt", "r")
lines = f.readlines()
f.close()

for l in lines:
	kwargs = {
		"msm_id": l.replace("\n", "")
	}
	
	is_success, results = AtlasResultsRequest(**kwargs).create()

	fc.write(str(results[0]).replace("'", "\"") + "\n")
	#print(str(results))

fc.close()