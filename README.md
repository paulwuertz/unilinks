# [Unilinks](http://p4w5.eu/uninoten)

Beispiel: [Ein bisschen Hauptstudium](http://www.p4w5.eu/noten/et_gs/?noten=4%2C2.9%2C3.2%2C2.4%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5%2C5)

## Was ist Uninoten

Unilinks ist eine private Linksammlung zu Veranstaaltungen und Seiten der [TU Dresden](https://tu-dresden.de/), deren Ziel es ist, einen zusammenfassenden Überblick für Ressourcen einzelner Studiengänge zu geben. Dieses Repository dient zur offenen Verwaltung dieser Sammlung.

## Verfügbare Studiengänge

Aktuell sind nur folgende Studiengänge aufgelistet:
* Elektrotechnik (Vordiplom/Grundstudium)
  * Automatisierungstechnik
	* Mikroelektronik
	* Elektroenergietechnik
	* Informationstechnik
	* Geräte-Medizin-Technik
* Informationssystemtechnik (Vordiplom/Grundstudium)
* Psychologie (Bachlor)

## Beitragen

Es ist möglich und erwünscht, zu dieser Sammlung weitere Studiengänge, Fächer sowie Korrekturen und Aktualisierungen beizutragen. Alle Daten sind im [json](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)-Format abgelegt.
Dabei gibte es einen Index (`index.json`), in dem alle verfügbaren Studiengänge mit ihrer ID (alphanumerischer, kurzer Name) sowie ihrer lesbaren Bezeichnung abgelegt sind.
Die Module eines Studiengangs sind in jeweils einer Datei abgelegt deren Name sich aus der ID bildet (`id.json`).
Die Module der Studiengänge enthalten mindestens einen lesbaren Namen sowie die Anzahl der Credits, die das Modul bringt. (bestes Beispiel ist der Psychologie BA, in den ET jsons sind noch Artefakte aus ner anderen Projektidee)

## Note berechnen

Schiebe die Regler bei den Modulen die du bestanden hast in deine entsprechende Position und das Ergebnis ganz unten aktualisiert sich automatisch. Alle Module schlechter als 4.0 werden ignoriert.
Die aktuelle Endnote wird aus dem gewichteten Mittel aller Module berechnet (is in allen DPOs die ich bisher sah so der Fall...).

Den Link der oben generiert wird könnt ihr euch bequem in eure Bookmarks packen und beim nächsten mal alle Neuerungen eintragen oder einfach spekulieren ;)
