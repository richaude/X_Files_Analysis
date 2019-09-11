from folge1 import getFolgenInhalt, isValid
from metrics import entropy, averageEntropy, token_type_stats, averageRedundance, averageSentenceLength, averageWordlength, fillWords
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
	
def writeEntropy2(staffeln, filename):
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	#m = mulder()
	#s = scully()
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			for i in range(0, episodenzahlen[z]):
				print(episodenzahlen[z])
				m = open("toLower_mulder"+str(z+1), "r")
				s = open("toLower_scully"+str(z+1), "r")
				mulder = m.read()
				mulderEpisodes = mulder.split("separator")
				print(str(len(mulderEpisodes)))
				scully = s.read()
				scullyEpisodes = scully.split("separator")
				print(str(len(scullyEpisodes)))
				if ((averageEntropy(mulderEpisodes[i]) != 0) and (averageEntropy(scullyEpisodes[i]) != 0)):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageEntropy(mulderEpisodes[i]))+","+str(averageEntropy(scullyEpisodes[i]))+"\n"
					
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close
	
def writeRedundance(staffeln, filename):
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	#m = mulder()
	#s = scully()
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			for i in range(0, episodenzahlen[z]):
				#print(episodenzahlen[z])
				m = open("toLower_mulder"+str(z+1), "r")
				s = open("toLower_scully"+str(z+1), "r")
				mulder = m.read()
				mulderEpisodes = mulder.split("separator")
				#print(str(len(mulderEpisodes)))
				scully = s.read()
				scullyEpisodes = scully.split("separator")
				#print(str(len(scullyEpisodes)))
				if ((averageRedundance(mulderEpisodes[i]) != 0) and (averageRedundance(scullyEpisodes[i]) != 0)):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageRedundance(mulderEpisodes[i]))+","+str(averageRedundance(scullyEpisodes[i]))+"\n"
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close

def writeDementia2(staffeln, filename):
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			m = open("toLower_mulder"+str(z+1), "r")
			wordsM = m.read()
			wordsM_Episodes = wordsM.split("separator")
			print(str(len(wordsM_Episodes)))
			s = open("toLower_scully"+str(z+1), "r")
			wordsS = s.read()
			wordsS_Episodes = wordsS.split("separator")
			print(str(len(wordsS_Episodes)))
			for i in range(0, episodenzahlen[z]):
				if ((token_type_stats(wordsM_Episodes[i].split()) != 0) and (token_type_stats(wordsS_Episodes[i].split()) != 0)):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(token_type_stats(wordsM_Episodes[i].split()))+","+str(token_type_stats(wordsS_Episodes[i].split()))+"\n"
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close
	
def writeSentences(staffeln, filename):
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			m = open("toLower_mulder"+str(z+1), "r")
			txt = m.read()
			m_Episodes = txt.split("separator")
			s = open("toLower_scully"+str(z+1), "r")
			txtS = s.read()
			s_Episodes = txtS.split("separator")
			for i in range(0, episodenzahlen[z]):
				if ((averageSentenceLength(m_Episodes[i]) != 0) and (averageSentenceLength(s_Episodes[i]) != 0)):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageSentenceLength(m_Episodes[i]))+","+str(averageSentenceLength(s_Episodes[i]))+"\n"
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close
	
def writeWordLengths(staffeln, filename):
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			m = open("toLower_mulder"+str(z+1), "r")
			txt = m.read()
			m_Episodes = txt.split("separator")
			s = open("toLower_scully"+str(z+1), "r")
			txtS = s.read()
			s_Episodes = txtS.split("separator")
			for i in range(0, episodenzahlen[z]):
				if ((averageWordlength(m_Episodes[i]) != 0) and (averageWordlength(s_Episodes[i]) != 0)):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(averageWordlength(m_Episodes[i]))+","+str(averageWordlength(s_Episodes[i]))+"\n"
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close
	
def writeFillwords(staffeln, filename):
	# leave out 6-19, 2-7, 4-21, 5-1, 5-15, 2-20, 4-7, 5-20
	missOut = ["S6E19", "S2E7", "S4E21", "S5E1", "S5E15", "S2E20", "S4E7", "S5E20"]
	f = open(filename+".csv", "w")
	start = "Episode,MULDER,SCULLY\n"
	episodenzahlen = [23, 25, 24, 24, 20, 22]
	z = 0
	while z < 6:
		if z in staffeln:
			m = open("toLower_mulder"+str(z+1), "r")
			txt = m.read()
			m_Episodes = txt.split("separator")
			print(str(len(m_Episodes)))
			s = open("toLower_scully"+str(z+1), "r")
			txtS = s.read()
			s_Episodes = txtS.split("separator")
			print(str(len(s_Episodes)))
			for i in range(0, episodenzahlen[z]):
				if ("S"+str(z+1)+"E"+str(i+1) not in missOut):
					start += "S"+str(z+1)+"E"+str(i+1)+","+str(fillWords(m_Episodes[i]))+","+str(fillWords(s_Episodes[i]))+"\n"
				else:
					pass
			m.close
			s.close
		z += 1
	f.write(start)
	f.flush
	f.close

#writeEntropy2([0,1,2,3,4,5], "valuesEntropyLower")	
writeDementia2([0,1,2,3,4,5], "valuesDementiaLower")
writeRedundance([0,1,2,3,4,5], "valuesRedundanceLower")
writeSentences([0,1,2,3,4,5], "valuesSatzlaengenLower")
writeWordLengths([0,1,2,3,4,5], "valuesWortlaengenLower")
writeFillwords([0,1,2,3,4,5], "valuesFillwordsLower")
