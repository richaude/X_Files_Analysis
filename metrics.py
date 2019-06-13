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

def entropy(word):
	negEntropy = 0
	alleP = wahrscheinlichkeiten(word)
	for s in word:
		val = alleP[s]
		negEntropy += val * math.log(val, 2)
	entropy = 0 - negEntropy
	return entropy
	
def token_type_stats(text): #dementia
    num_tokens, num_types, known_types = 0, 0, set()
    tokens = text.split()
    for word in tokens:
        num_tokens += 1
        if not word in known_types:
            known_types.add(word)
            num_types += 1
    return (num_tokens, num_types, num_tokens / num_types)
			
for k,v in wahrscheinlichkeiten("hallo").items():
	print(k + ": " + str(v))
print(str(entropy("abcdefghijklmnopqrstuvwxyz")))
print(token_type_stats("hallo du \n da da"))
