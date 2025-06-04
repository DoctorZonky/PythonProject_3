### Wichtige Libraries, die importiert werden müssen ###
import numpy as np
import streamlit as st
from io import StringIO


### Objektorientierte Programmierung mit Klassen ###

# Hauptklasse FASTA definieren
class FASTA:
    def __init__(self, fasta_text=""):
        self.fasta_text = fasta_text

    # Methode zur Eingabe einer FASTA-DNA-Sequenz über eine Textarea in der Sidebar
    def input_FASTA_text(self):
        st.sidebar.header("Copy  & Paste your FASTA-DNA-Sequence here")
        fasta_seq_input = st.sidebar.text_area("Gib deine FASTA-DNA-Sequenz manuell ein:")
        return fasta_seq_input
    
    # Methode zum Upload eines Files und Speichern in einer Variable
    def upload_FASTA_file(self):
        st.sidebar.header("Lade eine FASTA-Datei hoch")                                                  # Header für die Sidebar
        fasta_extensions = ["fasta", "fa", "mpfa", "fna", "fsa"]
        FASTA_file = st.sidebar.file_uploader("Lade hier deine FASTA-Datei hoch:", type=fasta_extensions)       # Hier wird die Datei hochgeladen und als Variable gespeichert
        return FASTA_file                                                                               # Ausgabe der Fasta-Datei

    # Methode zum Aufreinigen eines FASTA-Textes zum Erzeugen eines Sequenz-Strings
    def sequence_input(self):
        lines = self.fasta_text.splitlines()                                                            # Der eingegebene Text wird in separate Lines gesplittet
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]                        # Entfernung des Headers 
        sequence = "".join(seq_lines).replace(" ", "").upper()                                          # Die Linien werden in eine Sequenz gemerget und (falls nötig) in Großbuchstaben umgewandelt, Leerzeichen zwischen den Zeilen werden entfernt
        return sequence
    
    # Methode zur Extraktion der Header Zeilen
    def header_input(self):
        lines = self.fasta_text.splitlines()                                                            # Der eingegebene Text wird in separate Lines gesplittet
        header = [line.strip() for line in lines if line.startswith(">")]                               # Entfernung aller Zeilen außer dem Header
        return header
    
    # Methode zur Erzeugung eines inversen DNA-Strangs in 5'-3'-Richtung
    def sequence_invert(self):
        sequence = self.sequence_input()                                                                # Aufruf der Methode zum Aufreinigen des FASTA-Textes
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}                                           # Definition der komplementären Basen
        inverted_sequence = "".join(complement[base] for base in reversed(sequence))                    # Umkehrung der Sequenz und Ersetzung der Basen durch ihre Komplementäre
        return inverted_sequence
    
    # Methode zum Zählen der Basen in der eingegebenen Sequenz
    def base_count(self):
        sequence = self.sequence_input()                                                                # Aufruf der Methode zum Aufreinigen des FASTA-Textes
        base_counts = {base: sequence.count(base) for base in "ATCG"}                                   # Zählen der Basen in der Sequenz
        return base_counts
    

### Aufbau der App-Page ###
## Titel der Seite
st.title("Analyze FASTA-DNA-Sequences")

## Sidebar für die Auswahl der gewünschten Funktionen
st.sidebar.title("Options")

## Funktion zum Aufruf des Toggle zum Datei-Upload oder manueller Texteingabe
def file_upload():
    fasta_file_on = st.sidebar.toggle("FASTA-Sequenz aus Datei laden", False)                           # Toggle-Button für die primäre Auswahl zwischen Text-Eingabe oder Datei-Upload
    return fasta_file_on

# Funktion um die Anzeigerichtung der Ausgabe-Sequenz zu ändern          
def format_direction(sequence, direction):
    if direction == "3' → 5'":
        return f"3' - {sequence[::-1]} - 5'"                                                             # Ausgabe in inverser Richtung (3' --> 5' Richtung)
    return f"5' - {sequence} - 3'"                                                                                       # Standard-Ausgabe (5' --> 3' Richtung)

# Funktion zum Aufruf des Toggle für die Anzeige des inversen DNA-Strangs
def invert_DNA():
    invert_DNA_on = st.sidebar.toggle("Inversen DNA-Strang anzeigen", False)                            # Toggle-Button für die Anzeige des inversen DNA-Strangs
    return invert_DNA_on
strand_direction = st.sidebar.radio("Richtung der Anzeige", options = ["5' → 3'", "3' → 5'"])           # Toggle-Button für um die Anzeigerichtung der angezeigten Stränge zu ändern

# Spalten-Layout für die Anzeige der Ergebnisse
col1, col2 = st.columns(2)                                                                              # Erstellen von zwei Spalten für die Anzeige der Ergebnisse


### Prüfung auf Upload und konsekutivem Erstellen eines Objekts der Klasse FASTA ###
if file_upload():
    FASTA_file = FASTA().upload_FASTA_file()                                                            # Erstellen eines Objekts und Aufruf der Funktion zum Hochladen einer Datei

    # Ausgabe der nativen Sequenz bei erfolgreichem Upload einer FASTA-Datei
    if FASTA_file is not None:
        col1.header("Original DNA-Sequence")
        fasta_content = FASTA_file.getvalue().decode("utf-8")                                          # Die Datei wird in einen String umgewandelt                                                            
        fasta_obj_file = FASTA(fasta_content)
        header = fasta_obj_file.header_input()
        col1.write(f"Die Header-Zeile der DNA-Sequenz lautet: {header}")                                # Ausgabe des Headers, der in der hochgeladenen Datei enthalten ist
        sequence_native = fasta_obj_file.sequence_input()                                        # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Textes
        sequence_native_fmt = format_direction(sequence_native, strand_direction)
        col1.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native_fmt}")                    # Ausgabe der Sequenz, die in der hochgeladenen Datei enthalten ist


    if invert_DNA and FASTA_file is not None:
        col2.header("Inverted DNA-Sequence")                                                            # Header für die Spalte mit der inversen Sequenz
        sequence_invert = FASTA(fasta_obj_file).sequence_invert()                                       # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        col2.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist
    
else:                                                                    # Prüfung, ob der Toggle-Button für die manuelle Eingabe aktiviert ist
    
    if FASTA().input_FASTA_text():                                                    # Aufruf der Methode zum Eingeben einer FASTA-DNA-Sequenz über eine Textarea in der Sidebar
        fasta_text = FASTA().input_FASTA_text()
        fasta_obj_input = FASTA(fasta_text)                                                   # Erstellung eines Objekts der Klasse FASTA
        header = fasta_obj_input.header_input()                                                         # Aufruf der Methode zum Aufreinigen des Headers
        col1.header("Original DNA-Sequence")
        col1.write(f"Die Header-Zeile der DNA-Sequenz lautet: {header}")                                # Ausgabe des Headers, der in der hochgeladenen Datei enthalten ist
        sequence_native = fasta_obj_input.sequence_input()                                              # Aufruf der Methode zum Aufreinigen des Textes
        sequence_native_fmt = format_direction(sequence_native, strand_direction)
        col1.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native_fmt}") 

    # Abfrage, ob die Sequenz invertiert werden soll
    if invert_DNA and FASTA().input_FASTA_text():
        col2.header("Inverted DNA-Sequence")
        sequence_invert = FASTA(fasta_obj_input).sequence_invert()                                      # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        col2.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                  # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist

