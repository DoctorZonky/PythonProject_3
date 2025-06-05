# Wichtige Libraries, die importiert werden müssen #
!pip install 

import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
from io import StringIO



# Hauptklasse FASTA definieren
class FASTA:
    def __init__(self, fasta_input=""):
        self.fasta_input = fasta_input
        self.fasta_seq = ""
        self.fasta_header = ""
        self.fasta_inverted = ""
        self.fasta_base_counts = {}

    def fasta_file_to_string(self):
        self.fasta_input = self.fasta_input.getvalue().decode("utf-8")                              # Die hochgeladene Datei wird in einen String umgewandelt und intern gespeichert

    ## Methode zum Aufreinigen eines FASTA-Textes zum Erzeugen eines Sequenz-Strings
    def get_sequence(self):
        lines = self.fasta_input.splitlines()                                                       # Der eingegebene Text wird in separate Lines gesplittet
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]                    # Entfernung des Headers 
        self.fasta_seq = "".join(seq_lines).replace(" ", "").upper()                                # Die Linien werden in eine Sequenz gemerget und (falls nötig) in Großbuchstaben umgewandelt, Leerzeichen zwischen den Zeilen werden entfernt
    
    ## Methode zur Extraktion der Header Zeilen
    def get_header(self):
        lines = self.fasta_input.splitlines()                                                       # Der eingegebene Text wird in separate Lines gesplittet
        self.fasta_header = [line.strip() for line in lines if line.startswith(">")]                # Entfernung aller Zeilen außer dem Header
           
    ## Methode zur Erzeugung eines inversen DNA-Strangs in 5'-3'-Richtung
    def invert_sequence(self):
        sequence = self.fasta_seq                                                                   # Abgreifen des Attributs für den Sequenz-String
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}                                       # Definition der komplementären Basen
        self.fasta_inverted = "".join(complement[base] for base in reversed(sequence))              # Umkehrung der Sequenz und Ersetzung der Basen durch ihre Komplementäre
            
    ## Methode zum Zählen der Basen in der eingegebenen Sequenz
    def base_count(self):
        sequence = self.fasta_seq                                                                   # Abgreifen des Attributs für den Sequenz-String
        self.fasta_base_counts = {base: sequence.count(base) for base in "ATCG"}                    # Zählen der Basen in der Sequenz
        


# Funktionen, die aufgerufen werden sollen #

## Funktion zum Darstellen des Headers aus der eingegebenen Sequenz ##
def do_header(header):
    st.header("FASTA-Sequence header")                                                              # Header der Fasta-Sequenz
    st.container(border=True).write(f"{header}")                                                    # Ausgabe des Headers, der im Objekt FASTA-file gespeichert ist in einem Container


## Funktion zum Erstellen der linken Spalte (Col1) für die Anzeige der nativen Sequenz ##
def do_col1(sequence):
    col1.header("Original")                                                                         # Header der Spalte
    col1.expander("Expand / Collapse DNA Sequence", True).write(sequence)                           # Anzeige der nativen Sequenz in der ersten (linken) Spalte

## Funktion zum Erstellen der rechten Spalte (Col2) für die Anzeige der inversen Sequenz ##
def do_col2(sequence_inv):
    col2.header("Inverted")  
    col2.expander("Expand / Collapse DNA Sequence", True).write(sequence_inv)                       # Ausgabe des inversen DNA-Strangs in der zweiten (rechten) Spalte als kollabierbarer Bereich



## Funktion zum Wählen der Farben für das Balkendiagramm ##
def do_color_palette():
    with st.sidebar.container(border=True):
        color_A = st.color_picker("Select color for A", "#2DE6FF")                                # Farbauswahl für A-Balken des Balkendiagramms
        color_C = st.color_picker("Select color for C", "#2296B3")                                # Farbauswahl für C-Balken des Balkendiagramms
        color_G = st.color_picker("Select color for G", "#3284FF")                                # Farbauswahl für G-Balken des Balkendiagramms
        color_T = st.color_picker("Select color for T", "#1E5CB9")                                # Farbauswahl für T-Balken des Balkendiagramms
    col_pal = [color_A, color_C, color_G, color_T]                                                  # Zusammenführen der ausgewählten Farben in eine Liste (Palette)
    return col_pal                                                                                  # Ausgabe der Palette mit den gewählten Farben

## Funktion zur Erstellung des Barplots ##
def do_bar_plot(base_counts_df, col_pal):
      
    st.altair_chart(
        alt.Chart(base_counts_df.reset_index())
        .mark_bar()
        .encode(
            x=alt.X('index:N', title='Bases'),
            y=alt.Y('Count:Q', title='Frequency'),
            color=alt.Color('index:N', scale=alt.Scale(domain=['A', 'C', 'G', 'T'], range=col_pal)),
            tooltip=['index:N', 'Count:Q']
        )
    )

## Funktion für die Ausführung zur Erstellung und Anzeige des Balkendiagramms ##
def show_base_count_plot(base_counts):
    st.header("Base count bar plot (original sequence)")           
    col_pal = do_color_palette()                                                                    # Aufruf der Funktion zur Erzeugung der Farbpalette für das Balkendiagramm
    base_counts_df = pd.DataFrame.from_dict(base_counts, orient='index', columns=['Count'])         # Umwandlung des Dictionaries in ein DataFrame für die Darstellung im Balkendiagramm

    st.write(base_counts_df)
    do_bar_plot(base_counts_df, col_pal)                                                            # Aufruf der Funktion zum Erstellen des Balkendiagramms mit gewählten Farben
                                                                                                    

# Aufbau der App-Page #
st.title("Analyze FASTA-DNA-Sequences")                                                             # Titel der Seite
st.sidebar.title("Options")                                                                         # Sidebar für die Auswahl der gewünschten Funktionen



# Prüfung auf Upload und konsekutivem Erstellen eines Objekts der Klasse FASTA #
if st.sidebar.container(border = True).toggle("Load FASTA Sequence from file", False):
    file_uploaded = st.sidebar.file_uploader(                                                               # Sidebar-Datei-Upload für FASTA-Dateien
        "Drag and drop your file here:",
        type=["fasta", "fa", "mpfa", "fna", "fsa"]
        )

    ## Kontrollstruktur für die Anzeige der Sequenzen und des Headers in der App ##
    if file_uploaded is not None:                                                                           # Prüfung, ob eine Datei hochgeladen wurde
        FASTA_file = FASTA(file_uploaded)                                                                   # Erstellen eines FASTA-Objekts mit der hochgeladenen Datei
        FASTA_file.fasta_file_to_string()                                                                   # Das hochgeladene FASTA-File wird in einen String umgewandelt und intern gespeichert
        FASTA_file.get_sequence()                                                                           # Aufruf der Methode zum Extrahieren der Sequenz aus dem FASTA-String
        
        ### Layout der ersten Spalte und der Anzeige des Sequenz-Headers darüber ###
        FASTA_file.get_header()                                                                             # Aufruf der Methode zum Herausziehen des Headers
        do_header(FASTA_file.fasta_header)                                                                                         # Aufruf der Funktion zum Anzeigen des Headers der Sequenz

        col1, col2 = st.columns(2)                                                                          # Erzeugen der zwei Spalten für die Anzeige auf der Hauptseite
        do_col1(FASTA_file.fasta_seq)                                                                                           # Aufruf der Funktion zum Erstellen der linken Spalte

        invert_DNA_on = st.sidebar.toggle("Show inverted DNA-Sequence", False)                              # Toggle-Button für die Anzeige des inversen DNA-Strangs
        base_count_on = st.sidebar.toggle("Show base count and bar plot", False)                            # Toggle-Button für die Anzeige des inversen DNA-Strangs

        ### Kontrollstruktur zur Ausführung der Invertierung der DNA-Sequenz, falls gewünscht ###
        if invert_DNA_on and FASTA_file is not None:
            FASTA_file.invert_sequence()
            do_col2(FASTA_file.fasta_inverted)


        ### Kontrollstruktur zur Ausführung der Basenzählung und der Anzeige im Balkendiagramm ###
        if base_count_on and FASTA_file is not None:
            FASTA_file.base_count()                                                                         # Aufruf der Methode des Objekts FASTA_file zum Zählen der Basen und dem internen Speichern
            show_base_count_plot(FASTA_file.fasta_base_counts)


# Wenn kein Upload gewollt, dann wird die manuelle Eingabe der Sequenz freigeschaltet #    
else:
    fasta_seq_input = st.sidebar.text_area("Gib deine FASTA-DNA-Sequenz manuell ein:")                      # Aufruf des Textfeldes, um eine FASTA-Sequenz manuell eingeben zu können

    ## Kontrollstruktur, wenn Sequenz manuell eingegeben wurde ##
    if fasta_seq_input is not None and fasta_seq_input.strip() != "":                                       # Prüfung, ob eine Sequenz eingegeben wurde
        FASTA_input = FASTA(fasta_seq_input)                                                                # Erstellen eines neuen FASTA-Objekts aus dem manuellen Input
        FASTA_input.get_sequence()                                                                          # Aufruf der Methode zum Extrahieren der Sequenz aus dem Input
        FASTA_input.get_header()                                                                            # Aufruf der Methode zum Herausziehen des Headers
        do_header(FASTA_input.fasta_header)                                                                 # Aufruf der Funktion zum Anzeigen des Headers auf der Hauptseite der App

        col1, col2 = st.columns(2)                                                                          # Erzeugen der zwei Spalten für die Anzeige auf der Hauptseite
        do_col1(FASTA_input.fasta_seq)                                                                      # Aufruf der Funktion zum Erstellen der linken Spalte


        invert_DNA_on = st.sidebar.toggle("Show inverted DNA-Sequence", False)                              # Toggle-Button für die Anzeige des inversen DNA-Strangs
        base_count_on = st.sidebar.toggle("Show base count and bar plot", False)                            # Toggle-Button für die Anzeige des inversen DNA-Strangs


        ### Kontrollstruktur zur Ausführung der Invertierung der DNA-Sequenz, falls gewünscht ###
        if invert_DNA_on and fasta_seq_input is not None:
            FASTA_input.invert_sequence()
            do_col2(FASTA_input.fasta_inverted)


        ### Kontrollstruktur zur Ausführung der Basenzählung und der Anzeige im Balkendiagramm ###
        if base_count_on and fasta_seq_input is not None:
            FASTA_input.base_count()                                                                         # Aufruf der Methode des Objekts FASTA_file zum Zählen der Basen und dem internen Speichern
            show_base_count_plot(FASTA_input.fasta_base_counts)


############################################### Bis hier hin überarbeitet ####################################################