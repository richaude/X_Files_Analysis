from folge1 import getFolgenInhalt, isValid
from metrics import entropy, averageEntropy, token_type_stats, averageRedundance
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
		
#print(detNextEpisode("urn:cts:xfiles:s1.1X10:1")) die Methode ist zu aufwändig. da geht von Hand eintragen schneller

def mulder():
 contentMulder = [getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X02:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X03:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X04:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X05:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X06:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X07:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X08:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X09:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X10:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X11:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X12:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X13:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X14:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X15:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X16:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X17:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X18:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X19:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X20:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X21:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X22:1", " MULDER", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X23:1", " MULDER", "")]
 return contentMulder
	
def scully():
 contentScully = [getFolgenInhalt("urn:cts:xfiles:s1.1X01:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X02:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X03:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X04:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X05:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X06:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X07:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X08:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X09:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X10:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X11:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X12:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X13:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X14:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X15:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X16:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X17:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X18:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X19:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X20:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X21:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X22:1", " SCULLY", "")
	                ,getFolgenInhalt("urn:cts:xfiles:s1.1X23:1", " SCULLY", "")]
 return contentScully
	
def writeEntropy():
	f = open("valuesEntropy.csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	m = mulder()
	s = scully()
	for i in range(1, 24):
		start += str(i)+","+str(averageEntropy(m[i-1]))+","+str(averageEntropy(s[i-1]))+"\n"
	f.write(start)
	f.flush
	f.close
	
def writeDementia():
	f = open("valuesDementia.csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	m = mulder()
	mf = open("MulderS1", "w")
	mf.write(" ".join(m))
	mf.flush
	mf.close
	s = scully()
	sf = open("ScullyS1", "w")
	sf.write(" ".join(s))
	sf.flush
	sf.close
	for i in range(1, 24):
		wordsM = m[i-1].split()
		wordsS = s[i-1].split()
		start += "Episode_"+str(i)+","+str(token_type_stats(wordsM))+","+str(token_type_stats(wordsS))+"\n"
	f.write(start)
	f.flush
	f.close
	
def writeEntropy2(staffeln):
	f = open("valuesEntropy2.csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	#m = mulder()
	#s = scully()
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			for i in range(0, episodenzahlen[z]):
				print(episodenzahlen[z])
				m = open("mulder"+str(z+1), "r")
				s = open("scully"+str(z+1), "r")
				mulder = m.read()
				mulderEpisodes = mulder.split("SEPARATOR")
				print(str(len(mulderEpisodes)))
				scully = s.read()
				scullyEpisodes = scully.split("SEPARATOR")
				print(str(len(scullyEpisodes)))
				start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageEntropy(mulderEpisodes[i]))+","+str(averageEntropy(scullyEpisodes[i]))+"\n"
				m.close
				s.close
		z += 1
	f.write(start)
	f.flush
	f.close
	
def writeRedundance(staffeln):
	f = open("valuesRedundance.csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	#m = mulder()
	#s = scully()
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			for i in range(0, episodenzahlen[z]):
				#print(episodenzahlen[z])
				m = open("mulder"+str(z+1), "r")
				s = open("scully"+str(z+1), "r")
				mulder = m.read()
				mulderEpisodes = mulder.split("SEPARATOR")
				#print(str(len(mulderEpisodes)))
				scully = s.read()
				scullyEpisodes = scully.split("SEPARATOR")
				#print(str(len(scullyEpisodes)))
				start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageRedundance(mulderEpisodes[i]))+","+str(averageRedundance(scullyEpisodes[i]))+"\n"
				m.close
				s.close
		z += 1
	f.write(start)
	f.flush
	f.close

def writeDementia2(staffeln):
	f = open("valuesDementia2.csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			m = open("mulder"+str(z+1), "r")
			wordsM = m.read()
			wordsM_Episodes = wordsM.split("SEPARATOR")
			print(str(len(wordsM_Episodes)))
			s = open("scully"+str(z+1), "r")
			wordsS = s.read()
			wordsS_Episodes = wordsS.split("SEPARATOR")
			print(str(len(wordsS_Episodes)))
			for i in range(0, episodenzahlen[z]):
				start += "S"+str(z+1)+"E"+str(i+1)+","+str(token_type_stats(wordsM_Episodes[i].split()))+","+str(token_type_stats(wordsS_Episodes[i].split()))+"\n"
		z += 1
	f.write(start)
	f.flush
	f.close

#writeEntropy2([0,1,2,3,4,5])	
#writeDementia2([0,1,2,3,4,5])
writeRedundance([0,1,2,3,4,5])
