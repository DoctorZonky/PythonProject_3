# Wichtige Libraries, die importiert werden müssen #
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt



# Hauptklasse FASTA definieren
## Konstruktor der Klasse FASTA, der Attribute festlegt
class FASTA:
    def __init__(self, fasta_input=""):                                                                     
        self.fasta_input = fasta_input
        self.fasta_seq = ""
        self.fasta_header = ""
        self.fasta_inverted = ""
        self.fasta_base_counts = {}

    ## Methode, um die hochgeladene Datei in einen String umzwandeln und intern zu speichern
    def fasta_file_to_string(self):
        self.fasta_input = self.fasta_input.getvalue().decode("utf-8")                                      

    ## Methode zum Aufreinigen eines FASTA-Textes und der Erzeugung eines Sequenz-Strings durch Entfernung des Headers
    def get_sequence(self):
        lines = self.fasta_input.splitlines()                                                               
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]                            
        self.fasta_seq = "".join(seq_lines).replace(" ", "").upper()                                        
    
    ## Methode zur Extraktion der Header Zeilen, alle weiteren Zeilen werden ignoriert
    def get_header(self):
        lines = self.fasta_input.splitlines()                                                               
        self.fasta_header = [line.strip() for line in lines if line.startswith(">")]
           
    ## Methode zur Erzeugung eines inversen DNA-Strangs in 5'-3'-Richtung mittels Komplement-Dictionary
    def invert_sequence(self):
        sequence = self.fasta_seq
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        self.fasta_inverted = "".join(complement[base] for base in reversed(sequence))
            
    ## Methode zum Zählen der Basen in der eingegebenen Sequenz durch eine for-Schleife in einem Dictionary
    def base_count(self):
        sequence = self.fasta_seq
        self.fasta_base_counts = {base: sequence.count(base) for base in "ATCG"}
        


# Funktionen, die aufgerufen werden sollen #

## Funktion zum Darstellen des Headers aus der eingegebenen Sequenz in einem Container (borders) ##
def do_header(header):
    st.header("FASTA-Sequence header")
    st.container(border=True).write(f"{header}")


## Funktion zum Erstellen der linken Spalte (Col1) für die Anzeige der Überschrift und der nativen Sequenz in einem Expander ##
def do_col1(sequence):
    col1.header("Original")
    col1.expander("Expand / Collapse DNA Sequence", True).write(sequence)

## Funktion zum Erstellen der rechten Spalte (Col2) für die Anzeige der Überschrift und der inversen Sequenz in einem Expander ##
def do_col2(sequence_inv):
    col2.header("Inverted")  
    col2.expander("Expand / Collapse DNA Sequence", True).write(sequence_inv)



## Funktion zur Erzeugung einer Liste der Farbauswahlen für das Balkendiagramm über Hex-Farbcode-Picker ##
def do_color_palette():
    with st.sidebar.container(border=True):
        color_A = st.color_picker("Select color for A", "#2DE6FF")
        color_C = st.color_picker("Select color for C", "#2296B3")
        color_G = st.color_picker("Select color for G", "#3284FF")
        color_T = st.color_picker("Select color for T", "#1E5CB9")
    col_pal = [color_A, color_C, color_G, color_T]
    return col_pal

## Funktion zur Erstellung des Barplots über ein Altair-Chart nach Documentation examples ##
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

## Funktion für die Erzeugung des Balkendiagramms über die User-Farbpalette und ein "pandas" Base-Cound-Dataframe ##
def show_base_count_plot(base_counts):
    st.header("Base count bar plot (original sequence)")           
    col_pal = do_color_palette()
    base_counts_df = pd.DataFrame.from_dict(base_counts, orient='index', columns=['Count'])

    st.write(base_counts_df)
    do_bar_plot(base_counts_df, col_pal)
                                                                                                    

# Aufbau der App-Page mit Titel der App und Generierung der Sidebar #
st.title("Analyze FASTA-DNA-Sequences")
st.sidebar.title("Options")



# Prüfung auf gewollten Dateiupload und Ausführen der Uploader-Methode für einzelne Dateien mit Typbeschreibung #
if st.sidebar.container(border = True).toggle("Load FASTA Sequence from file", False):
    file_uploaded = st.sidebar.file_uploader(
        "Drag and drop your file here:",
        type=["fasta", "fa", "mpfa", "fna", "fsa"]
        )

    ## Kontrollstruktur falls Datei hochgeladen wurde mit folgenden Methodenaufrufen für Stringumwandlung und Sequenzextraktion ##
    if file_uploaded is not None:
        FASTA_file = FASTA(file_uploaded)
        FASTA_file.fasta_file_to_string()
        FASTA_file.get_sequence()
        
        ### Layout der ersten Spalte und der Anzeige des Sequenz-Headers darüber ###
        FASTA_file.get_header()
        do_header(FASTA_file.fasta_header)
        
        ### Erzeugung der zwei Spalten für die Anzeige auf der Hauptseite und Ausführung der Generierungsfunktionen für die linke Spalte ###
        col1, col2 = st.columns(2)
        do_col1(FASTA_file.fasta_seq)

        ### Toogler für die Auswahl der Anzeige des inversen DNA-Strangs und der Basenzählung ###
        invert_DNA_on = st.sidebar.toggle("Show inverted DNA-Sequence", False)
        base_count_on = st.sidebar.toggle("Show base count and bar plot", False)

        ### Kontrollstruktur zur Ausführung der Invertierung der DNA-Sequenz, falls gewünscht und der Generierung der rechten Spalte ###
        if invert_DNA_on and FASTA_file is not None:
            FASTA_file.invert_sequence()
            do_col2(FASTA_file.fasta_inverted)


        ### Kontrollstruktur zur Ausführung der Basenzählung und der Anzeige im Balkendiagramm mit eigenen Farben, falls gewünscht ###
        if base_count_on and FASTA_file is not None:
            FASTA_file.base_count()
            show_base_count_plot(FASTA_file.fasta_base_counts)


# Wenn kein Upload gewollt, dann wird die manuelle Eingabe der Sequenz freigeschaltet #    
else:
    ## Aufruf der Methode zum Erstellen eines Texteingabefeldes für mehrere Zeilen ##
    fasta_seq_input = st.sidebar.text_area("Gib deine FASTA-DNA-Sequenz manuell ein:")

    ## Kontrollstruktur, ob Sequenz manuell eingegeben wurde und folgender Methodenaufrufe zum Erhalt der Sequenz und des Headers ##
    if fasta_seq_input is not None and fasta_seq_input.strip() != "":
        FASTA_input = FASTA(fasta_seq_input)
        FASTA_input.get_sequence()
        FASTA_input.get_header()
        do_header(FASTA_input.fasta_header)

        ### Erzeugung der zwei Spalten für die Anzeige auf der Hauptseite und Ausführung der Generierungsfunktionen für die linke Spalte
        col1, col2 = st.columns(2)
        do_col1(FASTA_input.fasta_seq)

        ### Toogler für die Auswahl der Anzeige des inversen DNA-Strangs und der Basenzählung ###
        invert_DNA_on = st.sidebar.toggle("Show inverted DNA-Sequence", False)
        base_count_on = st.sidebar.toggle("Show base count and bar plot", False)


        ### Kontrollstruktur zur Ausführung der Invertierung der DNA-Sequenz, falls gewünscht und Generierung der rechten Spalte ###
        if invert_DNA_on and fasta_seq_input is not None:
            FASTA_input.invert_sequence()
            do_col2(FASTA_input.fasta_inverted)


        ### Kontrollstruktur zur Ausführung der Basenzählung und der Anzeige im Balkendiagramm mit eigenen Farben, falls gewünscht ###
        if base_count_on and fasta_seq_input is not None:
            FASTA_input.base_count()
            show_base_count_plot(FASTA_input.fasta_base_counts)