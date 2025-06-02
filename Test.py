### Wichtige Libraries, die importiert werden müssen ###
import numpy as np
import streamlit as st
from io import StringIO


### Objektorientierte Programmierung mit Klassen ###

# Hauptklasse FASTA definieren
class FASTA:
    def __init__(self, fasta_text):
        self.fasta_text = fasta_text

    # Methode zum Aufreinigen eines FASTA-Textes zum Erzeugen eines Sequenz-Strings
    def sequence_input(self):
        lines = self.fasta_text.splitlines()                                                # Der eingegebene Text wird in separate Lines gesplittet
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]            # Entfernung des Headers und der Leerzeichen zwischen den Zeilen
        sequence = "".join(seq_lines).replace(" ", "").upper()                              # Die Linien werden in eine Sequenz gemerget und (falls nötig) in Großbuchstaben umgewandelt
        return sequence
    
    def sequence_invert(self):
        sequence = self.sequence_input()                                                     # Aufruf der Methode zum Aufreinigen des FASTA-Textes
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}                                # Definition der komplementären Basen
        inverted_sequence = "".join(complement[base] for base in reversed(sequence))         # Umkehrung der Sequenz und Ersetzung der Basen durch ihre Komplementäre
        return inverted_sequence

### Wichtige Funktionen außerhalb der Klasse ###

# Funktion zum Upload eines Files und Speichern in einer Variable
def upload_FASTA_file():
    fasta_extensions = ["fasta", "fa", "mpfa", "fna", "fsa"]
    FASTA_file = st.file_uploader("Lade hier deine FASTA-Datei hoch:", type=fasta_extensions)    # Hier wird die Datei hochgeladen und als Variable gespeichert
    return FASTA_file                                                                            # Ausgabe der Fasta-Datei



### Aufbau der App-Page ###
# Titel der Seite
st.title("Analyze FASTA-DNA-Sequences")

# Sidebar für die Auswahl der gewünschten Funktionen
st.sidebar.title("Button-Auswahl")
fasta_file_on = st.sidebar.toggle("FASTA-Sequenz aus Datei laden", False)                                   # Toggle-Button für die primäre Auswahl zwischen Text-Eingabe oder Datei-Upload
invert_DNA_on = st.sidebar.toggle("Inversen DNA-Strang anzeigen", False)                                    # Toggle-Button für die Anzeige des inversen DNA-Strangs




### Prüfung auf Upload und konsekutivem Erstellen eines Objekts der Klasse FASTA ###
if fasta_file_on:
    FASTA_file = upload_FASTA_file()                                                                        # Aufruf der Funktion zum Hochladen einer Datei

    # Ausgabe der nativen Sequenz bei erfolgreichem Upload einer FASTA-Datei
    if FASTA_file is not None:
        fasta_text = FASTA_file.getvalue().decode("utf-8")                                                  # Die Datei wird in einen String umgewandelt
        sequence_native = FASTA(fasta_text).sequence_input()                                                # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Textes
        st.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native}")                              # Ausgabe derSequenz, die in der hochgeladenen Datei enthalten ist

    if invert_DNA_on and FASTA_file is not None:
        sequence_invert = FASTA(fasta_text).sequence_invert()                                               # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        st.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                      # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist
    
else:
    fasta_seq_input = st.text_input("Gib deine FASTA-DNA-Sequenz manuell ein:")
    st.write(f"Die eingegebene DNA-Sequenz lautet: {fasta_seq_input}")


