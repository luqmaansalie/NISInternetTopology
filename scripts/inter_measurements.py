from datetime import datetime
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest,
  Probe,
  Measurement,
  AtlasResultsRequest
)

ATLAS_API_KEY = "f9ccf6c6-f942-436a-8f93-ffef8b676236"

def initRequest(country, source, m):
	atlas_request = AtlasCreateRequest(
		start_time=datetime.utcnow(),
		key=ATLAS_API_KEY,
		measurements=m,
		sources=[source],
		is_oneoff=True
	)

	(is_success, response) = atlas_request.create()
	print(str(country) + ": " + str(response))

def getMeasurementList(c, one, two):
	msmnts = []

	p1 = Ping(af=4, target="www.uct.ac.za", description="intra ping 1 - " + c)
	p2 = Ping(af=4, target="www.uwc.ac.za", description="intra ping 2 - " + c)
	p3 = Ping(af=4, target="www.aucegypt.edu", description="intra ping 3 - " + c)
	p4 = Ping(af=4, target="www.cu.edu.eg", description="intra ping 4 - " + c)
	p5 = Ping(af=4, target="www.abu.edu.ng", description="intra ping 5 - " + c)
	p6 = Ping(af=4, target="www.unilag.edu.ng", description="intra ping 6 - " + c)
	p7 = Ping(af=4, target="www.uonbi.ac.ke", description="intra ping 7 - " + c)
	p8 = Ping(af=4, target="www.ku.ac.ke", description="intra ping 8 - " + c)
	p9 = Ping(af=4, target="www.ucad.sn", description="intra ping 9 - " + c)
	p10 = Ping(af=4, target="www.ugb.sn", description="intra ping 10 - " + c)
	p11 = Ping(af=4, target="www.uaq.ma", description="intra ping 11 - " + c)
	p12 = Ping(af=4, target="www.uca.ma", description="intra ping 12 - " + c)
	p13 = Ping(af=4, target="www.univ-tlemcen.dz", description="intra ping 13 - " + c)
	p14 = Ping(af=4, target="www.univ-bejaia.dz", description="intra ping 14 - " + c)
	p15 = Ping(af=4, target="www.ug.edu.gh", description="intra ping 15 - " + c)
	p16 = Ping(af=4, target="www.knust.edu.gh", description="intra ping 16 - " + c)
	p17 = Ping(af=4, target="www.uem.mz", description="intra ping 17 - " + c)
	p18 = Ping(af=4, target="www.up.ac.mz", description="intra ping 18 - " + c)
	p19 = Ping(af=4, target="www.udsm.ac.tz", description="intra ping 19 - " + c)
	p20 = Ping(af=4, target="www.sua.ac.tz", description="intra ping 20 - " + c)

	# ============================================================================

	tr1 = Traceroute(af=4, target="www.uct.ac.za", description="intra traceroute 1 - " + c, protocol="ICMP")
	tr2 = Traceroute(af=4, target="www.uwc.ac.za", description="intra traceroute 2 - " + c, protocol="ICMP")
	tr3 = Traceroute(af=4, target="www.aucegypt.edu", description="intra traceroute 3 - " + c, protocol="ICMP")
	tr4 = Traceroute(af=4, target="www.cu.edu.eg", description="intra traceroute 4 - " + c, protocol="ICMP")
	tr5 = Traceroute(af=4, target="www.abu.edu.ng", description="intra traceroute 5 - " + c, protocol="ICMP")
	tr6 = Traceroute(af=4, target="www.unilag.edu.ng", description="intra traceroute 6 - " + c, protocol="ICMP")
	tr7 = Traceroute(af=4, target="www.uonbi.ac.ke", description="intra traceroute 7 - " + c, protocol="ICMP")
	tr8 = Traceroute(af=4, target="www.ku.ac.ke", description="intra traceroute 8 - " + c, protocol="ICMP")
	tr9 = Traceroute(af=4, target="www.ucad.sn", description="intra traceroute 9 - " + c, protocol="ICMP")
	tr10 = Traceroute(af=4, target="www.ugb.sn", description="intra traceroute 10 - " + c, protocol="ICMP")
	tr11 = Traceroute(af=4, target="www.uaq.ma", description="intra traceroute 11 - " + c, protocol="ICMP")
	tr12 = Traceroute(af=4, target="www.uca.ma", description="intra traceroute 12 - " + c, protocol="ICMP")
	tr13 = Traceroute(af=4, target="www.univ-tlemcen.dz", description="intra traceroute 13 - " + c, protocol="ICMP")
	tr14 = Traceroute(af=4, target="www.univ-bejaia.dz", description="intra traceroute 14 - " + c, protocol="ICMP")
	tr15 = Traceroute(af=4, target="www.ug.edu.gh", description="intra traceroute 15 - " + c, protocol="ICMP")
	tr16 = Traceroute(af=4, target="www.knust.edu.gh", description="intra traceroute 16 - " + c, protocol="ICMP")
	tr17 = Traceroute(af=4, target="www.uem.mz", description="intra traceroute 17 - " + c, protocol="ICMP")
	tr18 = Traceroute(af=4, target="www.up.ac.mz", description="intra traceroute 18 - " + c, protocol="ICMP")
	tr19 = Traceroute(af=4, target="www.udsm.ac.tz", description="intra traceroute 19 - " + c, protocol="ICMP")
	tr20 = Traceroute(af=4, target="www.sua.ac.tz", description="intra traceroute 20 - " + c, protocol="ICMP")

	msmnts = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20, tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9,tr10,tr11,tr12,tr13,tr14,tr15,tr16,tr17,tr18,tr19,tr20]
	del msmnts[one:two]
	del msmnts[(18+one):(18+two)]

	#for i in range(36):
		#print(msmnts[i].description)
	
	return(msmnts)

# ============================================================================

country = "SA"
source = AtlasSource(type="probes", value="33159, 18114, 31523", requested=3)
initRequest(country, source, getMeasurementList(country, 0, 2))

# ============================================================================

country = "Egypt"
source = AtlasSource(type="probes", value="35074, 34151, 32206", requested=3)
#initRequest(country, source, getMeasurementList(country, 2, 4))

# ============================================================================

country = "Nigeria"
source = AtlasSource(type="probes", value="51730, 33267, 30090", requested=3)
#initRequest(country, source, getMeasurementList(country, 4, 6))

# ============================================================================

country = "Kenya"
source = AtlasSource(type="probes", value="33965, 33752, 33751", requested=3)
initRequest(country, source, getMeasurementList(country, 6, 8))

# ============================================================================

country = "Senegal"
source = AtlasSource(type="probes", value="22522, 32258, 22588", requested=3)
#initRequest(country, source, getMeasurementList(country, 8, 10))

# ============================================================================

country = "Morocco"
source = AtlasSource(type="probes", value="35067, 32925, 30145", requested=3)
#initRequest(country, source, getMeasurementList(country, 10, 12))

# ============================================================================

country = "Algeria"
source = AtlasSource(type="probes", value="51462, 15328, 16604", requested=3)
#initRequest(country, source, getMeasurementList(country, 12, 14))

# ============================================================================

country = "Ghana"
source = AtlasSource(type="probes", value="33031, 14945, 6380", requested=3)
#initRequest(country, source, getMeasurementList(country, 14, 16))

# ============================================================================

country = "Mozambique"
source = AtlasSource(type="probes", value="19574, 14968, 13799", requested=3)
#initRequest(country, source, getMeasurementList(country, 16, 18))

# ============================================================================

country = "Tanzania"
source = AtlasSource(type="probes", value="50463, 33284, 27442", requested=3)
#initRequest(country, source, getMeasurementList(country, 18, 20))

# ============================================================================



