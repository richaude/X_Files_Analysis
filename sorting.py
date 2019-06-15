from folge1 import getFolgenInhalt, isValid
from metrics import makeEverythingRight
# für Staffel - Figurwerte
# Episode, Figur, Demenz (types/tokens), Entropie, Redundanz

def detNextEpisode(urn):
	#vielleicht finde ich irgendwann mal einen besseren Weg
	if isValid(urn):
		chunks = urn.split(":")
		i = chunks[-2]
		if i[-2] == "0" and i[-1] == "9":
			prev1 = i[-1]
			prev2 = i[-2] # die Zehnerstelle
			prevAll = int(i[-2])+int(i[-1])
			nxt = str(prevAll+1)
			i = i[:-2]
			i += str(nxt)
			print(i)
		elif i[-2] == "0":
			prev = i[-1]
			nxt = int(prev)+1
			i = i[:-1]
			print(i)
			i += str(nxt)
			print(i)
		else:
			prev1 = i[-1]
			prev2 = i[-2] # die Zehnerstelle
			prevAll = i[-2]+i[-1]
			nxt = str(prevAll+1)
			print(nxt)
			i = i[:-2]
			i += str(nxt)
			print(i)
		chunks[-2] = i
		chunks2 = ":".join(chunks)
		return chunks2
	else:
		print("not valid")
		
#print(detNextEpisode("urn:cts:xfiles:s1.1X10:1")) die Methode ist zu aufwändig
f = open("values.txt", "w")
start = "Episode,Character,Dementia,Entropy,Redundance\n"
start += "01,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " MULDER", ""))+"\n"
start += "02,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X02:1", " MULDER", ""))+"\n"
start += "03,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X03:1", " MULDER", ""))+"\n"
start += "04,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X04:1", " MULDER", ""))+"\n"
start += "05,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X05:1", " MULDER", ""))+"\n"
start += "06,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X06:1", " MULDER", ""))+"\n"
start += "07,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X07:1", " MULDER", ""))+"\n"
start += "08,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X08:1", " MULDER", ""))+"\n"
start += "09,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X09:1", " MULDER", ""))+"\n"
start += "10,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X10:1", " MULDER", ""))+"\n"
start += "11,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X11:1", " MULDER", ""))+"\n"
start += "12,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X12:1", " MULDER", ""))+"\n"
start += "13,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X13:1", " MULDER", ""))+"\n"
start += "14,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X14:1", " MULDER", ""))+"\n"
start += "15,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X15:1", " MULDER", ""))+"\n"
start += "16,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X16:1", " MULDER", ""))+"\n"
start += "17,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X17:1", " MULDER", ""))+"\n"
start += "18,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X18:1", " MULDER", ""))+"\n"
start += "19,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X19:1", " MULDER", ""))+"\n"
start += "20,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X20:1", " MULDER", ""))+"\n"
start += "21,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X21:1", " MULDER", ""))+"\n"
start += "22,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X22:1", " MULDER", ""))+"\n"
start += "23,"+"MULDER,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X23:1", " MULDER", ""))+"\n"
start += "01,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " SCULLY", ""))+"\n"
start += "02,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X02:1", " SCULLY", ""))+"\n"
start += "03,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X03:1", " SCULLY", ""))+"\n"
start += "04,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X04:1", " SCULLY", ""))+"\n"
start += "05,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X05:1", " SCULLY", ""))+"\n"
start += "06,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X06:1", " SCULLY", ""))+"\n"
start += "07,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X07:1", " SCULLY", ""))+"\n"
start += "08,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X08:1", " SCULLY", ""))+"\n"
start += "09,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X09:1", " SCULLY", ""))+"\n"
start += "10,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X10:1", " SCULLY", ""))+"\n"
start += "11,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X11:1", " SCULLY", ""))+"\n"
start += "12,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X12:1", " SCULLY", ""))+"\n"
start += "13,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X13:1", " SCULLY", ""))+"\n"
start += "14,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X14:1", " SCULLY", ""))+"\n"
start += "15,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X15:1", " SCULLY", ""))+"\n"
start += "16,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X16:1", " SCULLY", ""))+"\n"
start += "17,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X17:1", " SCULLY", ""))+"\n"
start += "18,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X18:1", " SCULLY", ""))+"\n"
start += "19,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X19:1", " SCULLY", ""))+"\n"
start += "20,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X20:1", " SCULLY", ""))+"\n"
start += "21,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X21:1", " SCULLY", ""))+"\n"
start += "22,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X22:1", " SCULLY", ""))+"\n"
start += "23,"+"SCULLY,"+makeEverythingRight(getFolgenInhalt("urn:cts:xfiles:s1.1X23:1", " SCULLY", ""))+"\n"

f.write(start)
f.flush
f.close
