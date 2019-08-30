import math
from nltk import tokenize
from nltk.tokenize import RegexpTokenizer

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
	if len(text) > 0:
		for word in text:
			num_tokens += 1
			#word = word.lower() so würde es noch kleiner werden
			if not word in known_types:
				known_types.add(word)
				num_types += 1
    #return (num_tokens, num_types, num_tokens / num_types)
		return num_types/num_tokens
	return 0    
	
def averageEntropy(txt):
	words = txt.split()
	averageEntropy = 0
	if len(words) > 0:
		totalEntropy = 0
		for word in words:
			totalEntropy += entropy(word)
		averageEntropy = totalEntropy/len(words)
	return averageEntropy
	
def averageRedundance(txt):
	words = txt.split()
	averageRedundance = 0
	if len(words) > 0:
		totalRedundance = 0
		for word in words:
			totalRedundance += maxEntropy(word)
		averageRedundance = totalRedundance/len(words)
	return averageRedundance
	
def averageSentenceLength(txt):
	sentences = tokenize.sent_tokenize(txt)
	averageSentenceLength = 0
	if len(sentences) > 0:
		totalSentencesLength = 0
		for s in sentences:
			totalSentencesLength += len(s)
		averageSentenceLength = totalSentencesLength/len(sentences) # hier eventuell noch -1, weil Satzende wird immer mitgezählt
	return averageSentenceLength
	
def averageWordlength(txt):
	tokenizer = RegexpTokenizer(r'\w+')
	words = tokenizer.tokenize(txt)
	averageWordlength = 0
	#print(words)
	if len(words) > 0:
		totalWordLength = 0
		for w in words:
			totalWordLength += len(w)
		averageWordlength = totalWordLength/len(words)
	return averageWordlength
	
def fillWords(txt):
	fillwords = ["er", "uhm", "uh", "ahm", "hm", "ah", "um", "erm", "am", "huh"]
	tokenizer = RegexpTokenizer(r'\w+')
	words = tokenizer.tokenize(txt)
	totalFillwords = 0
	for w in words:
		if w in fillwords:
			totalFillwords += 1
	return totalFillwords
	
#print(fillWords("Could, ah, you show me, uh, where the caretaker is, hm, working?"))
#print(averageSentenceLength("Hey! Hal? Hdl."))
#print(averageWordlength("ha, ha, ha ha"))
#for k,v in wahrscheinlichkeiten("hallo").items():
	#print(k + ": " + str(v))
#print(str(entropy("abcdefghijklmnopqrstuvwxyz")))
#print(token_type_stats("hallo du \n da da"))
#print(makeEverythingRight("Mulder and Scully make their way through the crowded bar. We see many people sitting at the bar, but one particular man seems to be watching Mulder and Scully. Scully is looking through a file, we see a photo of a man, the same man we saw trembling in his home at the start, in a military uniform"))
