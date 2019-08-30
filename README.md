# X Files Analysis
## Repository zum Seminar Drama Mining und Filmanalyse 
Personensprachliche Analyse im Zeitverlauf, am Beispiel der Serie Akte X.
## Forschungsfrage
Mit welchen Methoden lassen sich sprachliche Veränderungen in einer Fernsehserie über die Zeit messen?
## Ausführen
### Gliederung
Die Texte von Mulder und Scully werden von `crawlAlles.py` erzeugt, es existiert jeweils eine Datei mit dem Text einer Person pro Staffel. (Staffel 1 bis 6).
Die einzelnen Dateien unterliegen momentan einem schnellen kontinuierlichen Wandel, aber die generelle Idee ist jetzt, nur `sorting.py` auszuführen, um die Werte in den csv-Dateien zu erzeugen.
#### Übersicht über die CSV Dateien
Die Werte für alle Staffeln sind in den entsprechend benannten CSV Dateien gespeichert. Es gibt bis auf die Füllwörter für jeden erhobenen Wert eine Version, die Groß- und Kleinschreibung berücksichtigt, und eine Version, die Groß- und Kleinschreibung ignoriert (letztere csv-Dateien enden auf `lower`.
## Ansicht
`index.html` im Browser öffnen.
