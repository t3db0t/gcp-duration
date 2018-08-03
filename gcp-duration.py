import requests
import xml.etree.ElementTree as ET

gcpXML = requests.get("https://www.blubrry.com/feeds/the_glass_cannon.xml")
cfXML = requests.get("https://www.blubrry.com/feeds/cannonfodder.xml")
aaXML = requests.get("https://www.blubrry.com/feeds/androidsandaliens.xml")

podcasts = [gcpXML, cfXML, aaXML]

allMinutes = 0

for p in podcasts:
	root = ET.fromstring(p.content)
	enclosures = root[0].findall('item//enclosure')
	totalLength = sum(int(c.attrib["length"]) for c in enclosures)
	minutes = totalLength / 64000 * 8 / 60.00
	hours = totalLength / 64000 * 8 / 60 / 60.00
	title = root[0].find("title").text

	allMinutes += minutes

	print "%s: Total Minutes: %f - Total Hours: %f\n" % (title, minutes, hours)

print "Across all podcasts - minutes: %f - hours: %f" % (allMinutes, allMinutes/60)