from urllib.request import urlopen
from bs4 import BeautifulSoup

def data_retrieval(urn, figure):
	# gibt den Text der angegebenen Figure zurück, für eine Urn
	source = urlopen("http://ch01.informatik.uni-leipzig.de:8080/truth/cts/?request=GetPassage&urn="+urn)
	bs = BeautifulSoup(source, "xml")
	for note in bs.findAll("note"):
		note.decompose()
	#content = bs.findAll("content")
	#print(content)
	#print("DEBUG POWER")
	#passage = bs.find("passage")
	#speakers = bs.find("speaker") #findet den ersten Speaker
	speakers = bs.findAll("speaker") #findet alle Speaker
	#print(speakers)
	figureContent = ""
	for s in speakers:
		if s.text == figure:
			figureContent += s.find_next_sibling("content").text
	return figureContent
		
def isValid(urn):
	# prüft, ob das Ende einer Folge erreicht wurde (wenn das Ende erreicht wurde, kommt ein Error und somit ist die Urn nicht valide, also wird false zurück gegeben)
	source = urlopen("http://ch01.informatik.uni-leipzig.de:8080/truth/cts/?request=GetPassage&urn="+urn)
	bs = BeautifulSoup(source, "xml")
	if len(bs.findAll("CTSError")) > 0:
		return False
	else:
		return True

def getNextUrn(urn):
	# bestimmt die nächste Urn in einer Episode
	ls = urn.split(":")
	i = int(ls[-1])
	ls.pop()
	i += 1
	ls2 = ":".join(ls)
	ls2+=":"+str(i)
	return ls2
	
def getFolgenInhalt(startUrn, figure, figureText):
	#gibt Inhalt des Textes der angegebenen Figur in der ganzen Folge zurück
	if isValid(startUrn):
		figureText += data_retrieval(startUrn, figure)
		#print(figureText)
		return getFolgenInhalt(getNextUrn(startUrn), figure, figureText)
	else:
		return figureText
		
# Die letzte URN für Folge 1 ist: urn:cts:xfiles:s1.1X01:23		
#print(data_retrieval("urn:cts:xfiles:s1.1X01:23", " MULDER")) # MAN BEACHTE DAS LEERZEICHEN IM STRING
#print(isValid("urn:cts:xfiles:s1.1X01:1"))
#print(getNextUrn("urn:cts:xfiles:s1.1X01:1"))
print(getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " MULDER", ""))
print("\n\n")
print(getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " SCULLY", ""))

