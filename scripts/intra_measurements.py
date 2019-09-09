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

def initRequest(country, source, p1, p2, t1, t2):
	atlas_request = AtlasCreateRequest(
		start_time=datetime.utcnow(),
		key=ATLAS_API_KEY,
		measurements=[p1, t1, p2, t2],
		sources=[source],
		is_oneoff=True
	)

	(is_success, response) = atlas_request.create()
	print(str(country) + ": " + str(response))

# ============================================================================

country = "SA"
source = AtlasSource(type="probes", value="33159, 18114, 31523", requested=3)

ping1 = Ping(af=4, target="www.uct.ac.za", description="intra ping1 1 - " + country)
ping2 = Ping(af=4, target="www.uwc.ac.za", description="intra ping2 2 - " + country)

traceroute1 = Traceroute(af=4, target="www.uct.ac.za", description="intra traceroute1 1 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.uwc.ac.za", description="intra traceroute2 2 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Egypt"
source = AtlasSource(type="probes", value="35074, 34151, 32206", requested=3)

ping1 = Ping(af=4, target="www.aucegypt.edu", description="intra ping1 3 - " + country)
ping2 = Ping(af=4, target="www.cu.edu.eg", description="intra ping2 4 - " + country)

traceroute1 = Traceroute(af=4, target="www.aucegypt.edu", description="intra traceroute1 3 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.cu.edu.eg", description="intra traceroute2 4 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Nigeria"
source = AtlasSource(type="probes", value="51730, 33267, 30090", requested=3)

ping1 = Ping(af=4, target="www.abu.edu.ng", description="intra ping1 5 - " + country)
ping2 = Ping(af=4, target="www.unilag.edu.ng", description="intra ping2 6 - " + country)

traceroute1 = Traceroute(af=4, target="www.abu.edu.ng", description="intra traceroute1 5 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.unilag.edu.ng", description="intra traceroute2 6 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Kenya"
source = AtlasSource(type="probes", value="33965, 33752, 33751", requested=3)

ping1 = Ping(af=4, target="www.uonbi.ac.ke", description="intra ping1 7 - " + country)
ping2 = Ping(af=4, target="www.ku.ac.ke", description="intra ping2 8 - " + country)

traceroute1 = Traceroute(af=4, target="www.uonbi.ac.ke", description="intra traceroute1 7 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.ku.ac.ke", description="intra traceroute2 8 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Senegal"
source = AtlasSource(type="probes", value="22522, 32258, 22588", requested=3) 

ping1 = Ping(af=4, target="www.ucad.sn", description="intra ping1 9 - " + country)
ping2 = Ping(af=4, target="www.ugb.sn", description="intra ping2 10 - " + country)

traceroute1 = Traceroute(af=4, target="www.ucad.sn", description="intra traceroute1 9 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.ugb.sn", description="intra traceroute2 10 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Morocco"
source = AtlasSource(type="probes", value="35067, 32925, 30145", requested=3)

ping1 = Ping(af=4, target="www.uaq.ma", description="intra ping1 11 - " + country)
ping2 = Ping(af=4, target="www.uca.ma", description="intra ping2 12 - " + country)

traceroute1 = Traceroute(af=4, target="www.uaq.ma", description="intra traceroute1 11 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.uca.ma", description="intra traceroute2 12 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Algeria"
source = AtlasSource(type="probes", value="51462, 15328, 16604", requested=3)

ping1 = Ping(af=4, target="www.univ-tlemcen.dz", description="intra ping1 13 - " + country)
ping2 = Ping(af=4, target="www.univ-bejaia.dz", description="intra ping2 14 - " + country)

traceroute1 = Traceroute(af=4, target="www.univ-tlemcen.dz", description="intra traceroute1 13 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.univ-bejaia.dz", description="intra traceroute2 14 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Ghana"
source = AtlasSource(type="probes", value="33031, 14945, 6380", requested=3)

ping1 = Ping(af=4, target="www.ug.edu.gh", description="intra ping1 15 - " + country)
ping2 = Ping(af=4, target="www.knust.edu.gh", description="intra ping2 16 - " + country)

traceroute1 = Traceroute(af=4, target="www.ug.edu.gh", description="intra traceroute1 15 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.knust.edu.gh", description="intra traceroute2 16 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Mozambique"
source = AtlasSource(type="probes", value="19574, 14968, 13799", requested=3)

ping1 = Ping(af=4, target="www.uem.mz", description="intra ping1 17 - " + country)
ping2 = Ping(af=4, target="www.up.ac.mz", description="intra ping2 18 - " + country)

traceroute1 = Traceroute(af=4, target="www.uem.mz", description="intra traceroute1 17 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.up.ac.mz", description="intra traceroute2 18 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================

country = "Tanzania"
source = AtlasSource(type="probes", value="50463, 33284, 27442", requested=3)

ping1 = Ping(af=4, target="www.udsm.ac.tz", description="intra ping1 19 - " + country)
ping2 = Ping(af=4, target="www.sua.ac.tz", description="intra ping2 20 - " + country)

traceroute1 = Traceroute(af=4, target="www.udsm.ac.tz", description="intra traceroute1 19 - " + country, protocol="ICMP")
traceroute2 = Traceroute(af=4, target="www.sua.ac.tz", description="intra traceroute2 20 - " + country, protocol="ICMP")

initRequest(country, source, ping1, ping2, traceroute1, traceroute2)

# ============================================================================