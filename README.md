# PythonProject_3

# Vorbereitung für die Ausführung der App
## Erste Schritte
1) Laden Sie sich die Dateien "XXX" und "YYY" herunter und speichern sie in einem Ordner auf dem Desktop
2) Doppelklicken Sie den Ordner, in dem Sie die Dateien gespeichert haben und öffnen ihn somit
3) Erweitern Sie den Dateipfad mit einem Einfachklick der linken Maustaste in das Adressfeld (Beginnt mit "Desktop")
4) Kopieren Sie den Pfad aus der Adresszeile (STRG + C)

## Öffnen der Konsole 
1) Öffnen Sie das Dialogfeld "Ausführen" mit der Tastenkombination "WIN + R"
2) Nun sollte sich ein Suchfenster mit der Aufschrift "Ausführen" öffnen
3) Tippen Sie hier "cmd" ein und drücken Sie Enter
4) Ein schwarzes Fenster (die Konsole) öffnet sich

## Installation der Dependencies
1) Tippen Sie in die Konsole "cd " und fügen das zuvor kopierte Directory aus dem Zwischenspeicher ein (STRG + V)
2) Drücken Sie Enter, nun sollte der ausgewählte Ordner in der Konsole als angesteuerter Pfad angezeigt werden
3) Tippen Sie nun 'pip install -r "requirements.txt"' ("" müssen hier mit kopiert werden!)
4) Alle notwendigen Libraries sollten nun installiert werden

## Ausführen des Programms
1) Tippen Sie nun in die Konsole 'streamlit run "YYY.py"' ("" müssen hier mit kopiert werden!)
2) Nun sollte sich Ihr favorisierter Browser öffnen und die App in einem Browser-Tab starten.


# Bedienung der App
## Einlesen einer FASTA-Sequenz


### Einlesen einer FASTA Sequenz
Prompt 1 (01.06.2025, 12:55 Uhr)
"Meine Anforderung ist folgende:
Ich möchte eine Funktion haben die es mir ermöglicht eine FASTA Sequenz (Sprich im FASTA Format) später in ein Eingabefenster zu kopieren, und hierdurch die Sequenz im Code "abgespeichert" wird.
Schreibe mit hierfür zunächst ein Funktion mit folgenden Anforderungen: 

Sie sollte die zusätzlichen Zeichen die bei einem FASTA Format mit dabei sind "rauskürzen" sodass nurnoch die Sequenz übrig bleibt mit der dann weitergearbeitet werden kann. 

Die Sequenz sollte so eingespeist werden, dass weiterführende AKtionen damit stattfinden können."

### Beispiel-FASTA-Sequenz von NCBI
>NC_000011.10:c2161209-2159779 Homo sapiens chromosome 11, GRCh38.p14 Primary Assembly
AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGT
GGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCG
TGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC
CTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTG
GCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAG
CTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCT
GCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCAC
CCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAG
TTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTG
TTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAA
TGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCT
GGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGA
GGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAG
ATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGAC
GCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGG
GTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGC
AGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGC
TCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGC
CCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCT
CTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACC
GAGAGAGATGGAATAAAGCCCTTGAACCAGC

### Nukleotid Counter Funktion

Automatisch durch integrierten CoPilot vorgeschlagen 


### Funktion zur Umkehr in komplementäre Basenabfolge

Automatisch durch integrierten CoPilot vorgeschlagen 

### Funktion zur Änderung der Anzeige-Richtung der Sequenzen

Prompt 2 (04.06.2025, 12:05 Uhr)

"Ich möchte noch folgende Funktionalität hinzufügen: 

Es soll einen button geben mit dem ich sowohl für den Original sowie den Komplementärstrang die Richtung einstellen kann in der er ausgegeben wird. 
Sprich vom Standardmäßigen 5' - 3' zu 3' - 5'"



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
2) Komplemente angeben (5'-3') mit Button(?) (Marco) 
3) Spalten für Originalcode und inversen Code (Adrian) Check (Für Datei-Upload)
4) Dropdown für beide Codezeilen (Adrian) Check (Für Datei-Upload)
5) Bar-Chart gesamthaft unter Sequenzen anzeigen (Adrian)
6) Farbschemaauswahl für Barchart? (Adrian)