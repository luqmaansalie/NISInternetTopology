from datetime import datetime
import urllib.request

fc = open('C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/pingresults5.json', 'w')
f = open("C:/Users/lsalie/Desktop/UCT/NIS/Assignment/data/pingdata5.txt", "r")

lines = f.readlines()
f.close()

for l in lines:
	fc.write(urllib.request.urlopen("https://atlas.ripe.net/api/v2/measurements/22730338/results/?format=json&filename=RIPE-Atlas-measurement-" + l.replace("\n", "") + ".json").read().decode('utf-8') + "\n")

fc.close()