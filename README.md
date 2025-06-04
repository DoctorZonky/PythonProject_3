# PythonProject_3

# Wichtig vor Start der Datei
Python muss installiert werden und dabei dem PATH zugewiesen werden
Verwendete Bibliotheken:
- Streamlit
- Matplotlib

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



# To do #
1) Headerzeilen extrahieren und ausgeben lassen (Marco) Check
2) Komplemente angeben (5'-3') mit Button(?) (Marco) 
3) Spalten für Originalcode und inversen Code (Adrian)
4) Dropdown für beide Codezeilen (Adrian)
5) Bar-Chart gesamthaft unter Codes anzeigen (Adrian)
6) Farbschemaauswahl für Barchart? (Adrian)