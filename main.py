from folge1 import getFolgenInhalt
from metrics import makeEverythingRight

def mkFile(urn, figure):
	f = open("ganze_Folge_"+urn+"_"+figure, "w")
	f.write(getFolgenInhalt(urn, " "+figure, ""))
	f.flush
	f.close
	return "ganze_Folge_"+urn+"_"+figure
	
def calculate(filename):
	f = open(filename, "r")
	content = f.read()
	f = open(filename, "a")
	f.write("\n\nCALCULATED:\n"+makeEverythingRight(content))
	f.flush
	f.close

# Berechnungen für die erste Folge, und die angegebenen Figuren	
#calculate(mkFile("urn:cts:xfiles:s1.1X01:1", "MULDER"))
#calculate(mkFile("urn:cts:xfiles:s1.1X01:1", "SCULLY"))
calculate(mkFile("urn:cts:xfiles:s6.6X14:1", "MULDER"))
calculate(mkFile("urn:cts:xfiles:s6.6X14:1", "SCULLY"))
