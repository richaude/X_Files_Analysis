import math

def wahrscheinlichkeiten(txt):
	properties = {}
	summe = 0
	for sign in txt:
		summe += 1
		if sign not in properties:
			properties[sign] = 1 #nur auf den Zähler schauen
		else: 
			properties[sign] = properties[sign]+1
	realProbs = {}
	for k, v in properties.items(): # jetzt sind es die Wahrscheinlichkeiten, unter der Annahme, dass die Zeichen stochastisch unabhängig voneinander sind
		realProbs[k] = v/summe
	return realProbs
	# vergleichbar mit Hmax in: https://de.wikipedia.org/wiki/Entropie_(Informationstheorie)
	
def englishProperties():
	# Werte von hier: https://de.wikipedia.org/wiki/Entropie_(Kryptologie) - für Englisch
	engProp = {}
	engProp["a"] = 7.19/100
	engProp["b"] = 1.58/100
	engProp["c"] = 4.05/100
	engProp["d"] = 3.11/100
	engProp["e"] = 13.05/100
	engProp["f"] = 2.42/100
	engProp["g"] = 2.34/100
	engProp["h"] = 4.71/100
	engProp["i"] = 7.71/100
	engProp["j"] = 0.09/100
	engProp["k"] = 0.58/100
	engProp["l"] = 3.72/100
	engProp["m"] = 2.54/100
	engProp["n"] = 7.81/100
	engProp["o"] = 7.52/100
	engProp["p"] = 2.3/100
	engProp["q"] = 0.1/100
	engProp["r"] = 6.41/100
	engProp["s"] = 6.49/100
	engProp["t"] = 9.22/100
	engProp["u"] = 2.83/100
	engProp["v"] = 0.86/100
	engProp["w"] = 1.07/100
	engProp["x"] = 0.45/100
	engProp["y"] = 1.73/100
	engProp["z"] = 0.1/100
	return engProp
	
def deutschProps():
	# für Deutsch - gleicher Variablenname für das Dictionary, da copypaste vom Englischen
	engProp = {}
	engProp["a"] = 5.45/100
	engProp["b"] = 1.75/100
	engProp["c"] = 3.37/100
	engProp["d"] = 5.11/100
	engProp["e"] = 16.89/100
	engProp["f"] = 1.28/100
	engProp["g"] = 3.76/100
	engProp["h"] = 5.26/100
	engProp["i"] = 8.51/100
	engProp["j"] = 0.18/100
	engProp["k"] = 1.51/100
	engProp["l"] = 3.77/100
	engProp["m"] = 2.22/100
	engProp["n"] = 10.42/100
	engProp["o"] = 3.11/100
	engProp["p"] = 0.63/100
	engProp["q"] = 0.01/100
	engProp["r"] = 7.14/100
	engProp["s"] = 6.24/100
	engProp["t"] = 6.08/100
	engProp["u"] = 3.4/100
	engProp["v"] = 0.89/100
	engProp["w"] = 1.64/100
	engProp["x"] = 0.02/100
	engProp["y"] = 0.07/100
	engProp["z"] = 1.27/100
	return engProp
	
def entropy(word):
	word = word.lower()
	negEntropy = 0
	#alleP = wahrscheinlichkeiten(word)
	alleP = englishProperties()
	for s in word:
		if s in alleP:
		    val = alleP[s]
		    negEntropy += val * math.log(val, 2)
	entropy = 0 - negEntropy
	return entropy
	
def maxEntropy(word):
	word = word.lower()
	negEntropy = 0
	alleP = wahrscheinlichkeiten(word)
	#alleP = englishProperties()
	for s in word:
		if s in alleP:
		    val = alleP[s]
		    negEntropy += val * math.log(val, 2)
	entropy = 0 - negEntropy
	return entropy
	
def token_type_stats(text): #dementia
    num_tokens, num_types, known_types = 0, 0, set()
    #tokens = text.split()
    for word in text:
        num_tokens += 1
        #word = word.lower() so würde es noch kleiner werden
        if not word in known_types:
            known_types.add(word)
            num_types += 1
    #return (num_tokens, num_types, num_tokens / num_types)
    return num_types/num_tokens
    
def makeEverythingRight(txt):
	words = txt.split()
	answer = str(token_type_stats(words))
	# calculating entropy for each word - should we average it? Currently doing it
	totalEntropy = 0
	totalRedundance = 0
	for word in words:
		totalEntropy += entropy(word)
		totalRedundance += (maxEntropy(word) - entropy(word))
		#print(word + ": "+ str(entropy(word)))
	averageEntropy = totalEntropy/len(words)
	averageRedundance = totalRedundance/len(words)
	answer += ","+str(averageEntropy)
	answer += ","+str(averageRedundance) # ist that even right? They are almost the same
	return answer
	
def averageEntropy(txt):
	words = txt.split()
	totalEntropy = 0
	for word in words:
		totalEntropy += entropy(word)
	averageEntropy = totalEntropy/len(words)
	return averageEntropy
	
	
			
#for k,v in wahrscheinlichkeiten("hallo").items():
	#print(k + ": " + str(v))
#print(str(entropy("abcdefghijklmnopqrstuvwxyz")))
#print(token_type_stats("hallo du \n da da"))
#print(makeEverythingRight("Mulder and Scully make their way through the crowded bar. We see many people sitting at the bar, but one particular man seems to be watching Mulder and Scully. Scully is looking through a file, we see a photo of a man, the same man we saw trembling in his home at the start, in a military uniform"))
