# PythonProject_3


# Vorbereitung für die Ausführung der App
## Erste Schritte
1)  Laden Sie sich die Dateien "requirements.txt" und "YYY.py" herunter und speichern sie in einem Ordner auf dem Desktop.
2)  Doppelklicken Sie den Ordner, in dem Sie die Dateien gespeichert haben und öffnen ihn somit.
3)  Erweitern Sie den Dateipfad mit einem Einfachklick der linken Maustaste in das Adressfeld (Beginnt mit "Desktop").
4)  Kopieren Sie den Pfad aus der Adresszeile (STRG + C).

## Öffnen der Konsole 
1)  Öffnen Sie das Dialogfeld "Ausführen" mit der Tastenkombination "WIN + R".
2)  Nun sollte sich ein Suchfenster mit der Aufschrift "Ausführen" öffnen.
3)  Tippen Sie hier "cmd" ein und drücken Sie Enter.
4)  Ein schwarzes Fenster (die Konsole) öffnet sich.

## Installation der Dependencies
1)  Tippen Sie in die Konsole "cd " und fügen das zuvor kopierte Directory aus dem Zwischenspeicher ein (STRG + V).
2)  Drücken Sie Enter, nun sollte der ausgewählte Ordner in der Konsole als angesteuerter Pfad angezeigt werden.
3)  Tippen Sie nun 'pip install -r "requirements.txt"' ("" müssen hier mit kopiert werden!).
    Sollte die Datei sich nicht öffnen lassen oder einzelne Fehlermeldungen kommen, installieren Sie streamlit, pandas und altair separat
    über "pip install [Bibliotheksname]" in der Konsole.
4)  Alle notwendigen Libraries sollten nun installiert werden.

## Ausführen des Programms
1)  Tippen Sie nun in die Konsole 'streamlit run "YYY.py"' ("" müssen hier mit kopiert werden!).
2)  Nun sollte sich Ihr favorisierter Browser öffnen und die App in einem Browser-Tab starten.


# Bedienung der App
Sie können prinzipiell zwischen zwei Modi wechseln: Dem Einlesen einer FASTA-Sequenz über Copy-Paste oder über das einlesen eines File.
Die Hauptseite der App zeigt die Überschrift "Analyze FASTA-DNA-Sequences" und eine einklappbare Sidebar auf der linken Seite.

## Einlesen einer FASTA-Sequenz
### FASTA-Sequenz über Copy-Paste eingeben
1)  Eine FASTA-Sequenz von beispielsweise NCBI kopieren und in das Feld in der Sidebar unter "Past your FASTA-DNA-Sequence here:" einfügen.
    Beispielsweise die bereitgestellte Versuchssequenz von NCBI unter dem Kapitel "Beispiel-FASTA-Sequenz von NCBI".
2)  Drücken Sie die Tastenkombination STRG + Enter, um die eingegebene Sequenz zu submitten.
3)  Nun erscheinen auf der Hauptseite zwei neue Objekte: der FASTA-Sequence header und das Expandable mit der Original-Sequenz in 5'-3'-Richtung.
    Sollte nur die Sequenz, ohne Header-Zeile eingefügt worden sein, erscheint in der Header-Bos nur "[]".
4)  Wahlweise können alle Expandables ("Expand / Collapse [...]") für eine bessere Übersicht ein- und ausgeklappt werden.
5)  Danach weiter mit Kapitel "Weitere Bearbeitung der FASTA-Sequenz".

### FASTA-Sequenz über eine FASTA-Datei hochladen
1)  Klicken Sie auf den Toggle "Load FASTA-Sequence from file", wenn dieser rot hinterlegt ist, wurde die Funktion aktiviert.
2)  Nun hat sich das Eingabefeld geänert und fordert zum Drag-'n'-Dropp eines FASTA-Files auf.
3)  Sie können wahlweise ein FASTA-File per Drag-'n'-Drop in die schwarze Box ziehen
    oder auf "Browse File" klicken, um im Dateiexplorer eins auszuwählen.
    Hierzu könnten Sie bspw. das mitgelieferte Beispiel-File "sequence.fasta" von NCBI verwenden.
4)  Nach dem erfolgreichen Hochladen werden nun automatisch zwei neue Objekte auf der Hautseite erscheinen:
    Der FASTA-Sequence header und das Expandable mit der Original-Sequenz in 5'-3'-Richtung.
5)  Wahlweise können alle Expandables ("Expand / Collapse [...]") für eine bessere Übersicht ein- und ausgeklappt werden.

## Verarbeiten der eingelesenen FASTA-Sequenz
### Invertierung der DNA-Sequenz
1)  Um den inversen Strang (Gegenstrang) der eingegebenen DNA-Sequenz in 5'-3'-Richtung anzeigen zu lassen,
    Drücken Sie den Toggle "Show inverted DNA-Sequence", sodass dieser rot hinterlegt ist.
2)  Nun wird auf der Hauptseite eine neue Box mit dem Titel "Inverted" erscheinen und die inverse 5'-3'-Sequenz anzeigen.
    Längenunterschiede in der letzten Zeile tauchen aufgrund der Formatierung der unterschiedlichen Zeichen manchmal auf.
3)  Wahlweise können alle Expandables ("Expand / Collapse [...]") für eine bessere Übersicht ein- und ausgeklappt werden.

### Zählen der Basen und Darstellung als Bar-Plot auf der Seite
1)  Drücken Sie den Toggle "Show base count and bar plot", sodass dieser rot hinterlegt ist.
2)  Nun öffnen sich eine neue Box links in der Sidebar mit vier Auswahlmöglichkeiten für die Farbpalette und
    zwei Darstellungen ganz unten auf der Hauptseite unter "Base count bar plot (original sequence)".
    Für bessere Übersicht, kollabieren Sie die beiden Expandables "Original" und "Inverted" mit einem Klick auf den angedeuteten Pfeil darunter.
3)  Die Tabelle mit der Überschrift "Count" gibt eine tabellarische Zusammenfassung der Anzahl an Basen im eingegebenen originalen DNA-Strang.
    Beim Hovern über die Tabelle wird ein Download-Symbol angezeigt, das den Download der Tabelle als .csv-File ermöglicht.
4)  Der Bar-Plot stellt diese Daten mit einer zusätzlichen Legende visuell dar.
5)  Über die Farbauswahl in der Sidebar können Sie unter "Select color for [Base]" frei eine individuelle Farbe für jeden Balken im Diagramm wählen.
6)  Wenn Sie mit der Maus über das Diagramm hovern, wird Ihnen rechts oben am Diagramm ein kleines Fenster-Zeichen angezeigt, das die Grafik
    beim Klick darauf auf dem gesamten Bildschirm anzeigt. Mit Escape kann die Ansicht wieder beendet werden.


# Zusatzinformationen
## Prompts für MS Copilot
### Einlesen einer FASTA Sequenz
Prompt 1 (01.06.2025, 12:55 Uhr)
"Meine Anforderung ist folgende:
Ich möchte eine Funktion haben die es mir ermöglicht eine FASTA Sequenz (Sprich im FASTA Format) später in ein Eingabefenster zu kopieren, und hierdurch die Sequenz im Code "abgespeichert" wird.
Schreibe mit hierfür zunächst ein Funktion mit folgenden Anforderungen: 

Sie sollte die zusätzlichen Zeichen die bei einem FASTA Format mit dabei sind "rauskürzen" sodass nurnoch die Sequenz übrig bleibt mit der dann weitergearbeitet werden kann. 

Die Sequenz sollte so eingespeist werden, dass weiterführende AKtionen damit stattfinden können."

### Nukleotid Counter Funktion
Automatisch durch integrierten CoPilot in VSC vorgeschlagen 

### Funktion zur Umkehr in komplementäre Basenabfolge
Automatisch durch integrierten CoPilot in VSC vorgeschlagen 

## Funktion um Strang-Leserichtung umzudrehen
Prompt 2 (09.06.2025, 19:00)
"Ich würde gerne noch folgende Funktion hinzufügen. Es soll durch einen toggle Button in Streamlit möglich sein die Leserichtung (standardmäßig ist es ja 5' - 3') zu 3' - 5' zu ändern. Sprich die Sequenz soll invertiert werden. Dies soll sowohl bei der Originalsequenz stattfinden, als auch bei dem Gegenstrang, der durch die Funktion "invert sequence" (schon im Code vorhanden) erstellt wird."

# Beispielddaten
## Beispiel-FASTA-Sequenz von NCBI
>NM_001353554.2 Homo sapiens chromosome 11 open reading frame 86 (C11orf86), transcript variant 1, mRNA
AGAGGGCCAGTGTCTTGCTGAGGGGCCGGAGCAGTCCTGTGCCTGCAGCCTCCGGAGCCATGGGAACAGG
GCTGCGAAGTCAGTCCTTGCGAGAGCCCCGACCCTCCTATGGAAAGCTGCAGGAGCCCTGGGGGAGGCCC
CAGGAGGGCCAACTCCGCAGGGCGCTAAGCCTCAGACAGGGGCAAGAGAAGTCCAGGTCCCAGGGCCTCG
AGAGAGGCACAGAAGGGCCAGATGCCACTGCCCAGGAGCGGGTGCCGGGGAGCCTGGGGGACACAGAGCA
GCTGATCCAAGCCCAGCGAAGAGGCAGCCGGTGGTGGCTGAGGCGGTACCAACAGCAGGTAAGAAGAAGG
TGGGAGAGCTTTGTCGCCATCTTCCCCAGCGTGACTCTGAGTCAGCCGGCCTCCCCGTAGCCCACACTGG
GCACCATCAGCTAAAGATGCTGGAAGCCATCGTGGCCCCCTTGCTGTGCCTGGACCAGCCCACCGTGTCT
GCTGACCTACCTCTTCACAGCTCTCTGGACTTTGGCTGGGTGGCCCTAGGAGGCTTCTGCCACCAGCTCA
CTGGAGTCGCCACGTGGCTGCCACTCTTAGCTCTGGCCCTTCCACTCCAGCACTAGCTCTCTTTGAAGAT
CCCAGCAGGGTCAAAAAGAAGGGGGCTCAGCTGTCTGCCCTCTGGGCTTGGGTAGGGGCCTTGGACTATG
ATTCTATGAAGGTTTAGAAGAAGCCTGCCCGGAATGGGGGCTGTGGACGCTCCTGCCCCACACGACCAGC
TGTCAACTTCCAGGACGGAGCTTGATGAAGCCAGACCCATGGCCGAGAGGCTCACGGACGTTGCCTGGTC
ACTGGGCCATGACCCAACTGCCCTTCTTGTCAGTTGCTGATGGTGGGCCAGGGCGCAGGTCTCCCTCCCA
GATGGTGAGCCCTCTGGGGCAAGGACCACAGCTGGGTGGCCCTCCTGGCTGAGCACTCTGTGCTGAAAAC
CTTTGAACCTCACGGTGTCCTGATGAAGGAAGCAGAGGAAGTCTTCCTCCCTGTGTGACAGAGGGGGAAA
CTGAGGCCCAGAGTGGGGAAGGGATTTCTTGGTTTTGACATCTCCGACCCCACCCCACCCCATCCAGTGT
CCAGCACTGGAGTCGAACACAGTAATAAAGATGCTGAGAAAAAGTCAA

Quelle: https://www.ncbi.nlm.nih.gov/nuccore/NM_001353554.2?report=fasta

## Beispiel-FASTA-File von NCBI
Datei: "sequence.fasta"

Quelle: https://www.ncbi.nlm.nih.gov/nuccore/LT934502.1?report=fasta



# Allgemeiner Hinweis
Die protokollierte Bearbeitung der Dateien entspricht nicht dem jeweils zugewiesenen Arbeitsaufwand einzelner Personen, da
teilweise über Zoom zusammengearbeitet wurde, obwohl nur eine Person als Autor eingetragen wurde.
Darüber hinaus erklären wir, dass die Projektarbeit ohne Hilfe Dritter entstanden ist, die nicht in Videoquellen genannt wurden und
lediglich KI als Unterstützung unter den eingesetzten Promts verwendet wurde. Die Struktur und Ausarbeitung des Projekts ist 

# Quellen #
## Python ##
### Klassen ###
https://docs.python.org/3/tutorial/classes.html


## Streamlit ##
### Basics ###
https://docs.streamlit.io
https://www.youtube.com/watch?v=43RJ3JByygE&list=PL2VXyKi-KpYtZzm1K8UKnnBzsOCtekhKq

### Layout ###
https://www.youtube.com/watch?v=saOv9z6Fk88&list=PL2VXyKi-KpYtZzm1K8UKnnBzsOCtekhKq&index=2


## Vega-Altair ##
https://altair-viz.github.io/user_guide/customization.html
https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart
https://vega.github.io/vega/docs/schemes/



# To do #
1) Headerzeilen extrahieren und ausgeben lassen (Marco) Check
2) Komplemente angeben (5'-3') mit Button(?) (Marco) Check
3) Spalten für Originalcode und inversen Code (Adrian) Check
4) Dropdown für beide Codezeilen (Adrian) Check
5) Bar-Chart gesamthaft unter Sequenzen anzeigen (Adrian)
6) Farbschemaauswahl für Barchart? (Adrian)
