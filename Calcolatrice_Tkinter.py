# Si importa la libreria per inizzializzare e visualizzare la finestra
import tkinter as tk

# Si inizializza la finestra
window = tk.Tk()
# Si da un titolo alla finestra
window.title("calcolatrice")
# Si danno delle dimensioni alla finestra
window.geometry("600x600")
# Si da la possibilità di ridimensionare la finestra direttamente da schermo
window.resizable(True,True)
# Si da il colore di background alla finestra
window.configure(background="white")

# Etichetta statica che compare dentro la finestra, in questo caso ci dice che è una calcolatrice
etichetta = tk.Label(window, text="CALCOLATRICE", fg="#ffffff", font=("Helvetica",25))
etichetta.grid(row=0, column=0, sticky="N", padx=200, pady=10)

# Si va a creare tutte le funzioni necessarie per operare la calcolatrice su due nuemri dati in input
def numero1_output():
    """ Si va a prendere il primo numero inserito in input (input_numero1.get()) e 
    si restituisce una label corrispondente in output
    VAR:
    numero1 -> variabile che prende il primo numero preso in input """
    numero1 = input_numero1.get()
    text_output1 = tk.Label(window,text = numero1, fg="#ffffff", font=("Helvetica",20))
    text_output1.grid(row= 3,column = 0,sticky="s")

def numero2_input():
    """ Si va a prendere il secondo numero inserito in input (input_numero2.get()) e 
    si restituisce una label corrispondente in output
    VAR:
    numero2 -> variabile che prende il secondo numero preso in input """
    numero2 = input_numero2.get()
    text_output1 = tk.Label(window,text = numero2, fg="#ffffff", font=("Helvetica",20))
    text_output1.grid(row= 7,column = 0,sticky="s")
    
def somma():
    """ Funzione che somma i due numeri dati in input e restituisce il risultato sotto forma di label 
    VAR:
    sum -> variabile che significa sum """
    # Si sommano i due numeri in input
    sum = float(input_numero1.get())+float(input_numero2.get())
    # Si stampa la somma
    if sum - int(sum) == 0: # Se la somma è intera si stampa un numero intero
        text_output1 = tk.Label(window,text = str(int(sum)), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 10,column = 0,sticky="s")
    elif sum - int(sum)!=0: # Se la somma non è intera si stampa il numero con la virgola
        text_output1 = tk.Label(window,text = str(sum), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 10,column = 0,sticky="s")

def sottrazione():
    """ Funzione che sottrae i due numeri dati in input e restituisce il risultato sotto forma di label 
    VAR:
    sub -> variabile che significa subtraction """
    # Si sottraggono i due numeri in input
    sub = float(input_numero1.get())-float(input_numero2.get())
    # Si stampa la sottrazione
    if sub - int(sub) == 0:# Se la sottrazione è intera si stampa un numero intero
        text_output1 = tk.Label(window,text = str(int(sub)), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 14,column = 0,sticky="s")
    elif sub - int(sub)!=0: # Se la sottrazione non è intera si stampa il numero con la virgola
        text_output1 = tk.Label(window,text = str(sub), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 14,column = 0,sticky="s")

def divisione():
    """ Funzione che divide i due numeri dati in input e restituisce il risultato sotto forma di label
    se la divisione è per 0 restituisce ERRORE 
    VAR:
    div -> variabile che significa division """
    # Controllo sulla divisione per verificare che non si divida per 0
    if float(input_numero2.get()) != 0:    
        # Si dividono i due numeri in input 
        div = round(float(input_numero1.get())/float(input_numero2.get()),3)
        #Si stampa la divisione
        if div - int(div) == 0:# Se la divisione è intera si stampa un numero intero
            text_output1 = tk.Label(window,text = str(int(div)), fg="#ffffff", font=("Helvetica",20))
            text_output1.grid(row= 18,column = 0,sticky="s")
        elif div - int(div) != 0:# Se la divisione non è intera si stampa il numero con la virgola
            text_output1 = tk.Label(window,text = str(div), fg="#ffffff", font=("Helvetica",20))
            text_output1.grid(row= 18,column = 0,sticky="s")
    elif float(input_numero2.get()) == 0:
        text_output1 = tk.Label(window,text = "ERRORE", fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 18,column = 0,sticky="s")

def moltiplicazione():
    """ Funzione che moltiplica i due numeri dati in input e restituisce il risultato sotto forma di label 
    VAR:
    prod -> variabile che significa product """
    # Si moltiplicano i due numeri in input 
    prod = float(input_numero1.get())*float(input_numero2.get())
    #Si stampa la moltiplicazione
    if prod - int(prod) == 0: # Se la moltiplicazione è intera si stampa un numero intero
        text_output1 = tk.Label(window,text = str(int(prod)), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 22,column = 0,sticky="s")
    elif prod-int(prod) != 0: # Se la moltiplicazione non è intera si stampa il numero con la virgola
        text_output1 = tk.Label(window,text = str(prod), fg="#ffffff", font=("Helvetica",20))
        text_output1.grid(row= 22,column = 0,sticky="s")

# Qui di seguito si va ad implementare il primo pulsante che prende in input il primo numero per l'operazione da eseguire
input_numero1 = tk.Entry(window)
input_numero1.grid(row=2,column=0,sticky="W")
button_n1 = tk.Button(window, text = "Inserire numero 1",command=numero1_output)
button_n1.grid(row=1,column=0,sticky="W")

#Qui di seguito si va ad implementare il secondo pulsante che prende in input il secondo numero per l'operazione da eseguire
input_numero2 = tk.Entry(window)
input_numero2.grid(row=6,column=0,sticky="W")
button_n2 = tk.Button(window, text = "Inserire numero 2",command=numero2_input)
button_n2.grid(row=5,column=0,sticky="W")

# Qui si implementa il pulsante per la somma
button_somma = tk.Button(window, text = "somma",command=somma)
button_somma.grid(row=10,column=0,sticky="W")

# Qui si implementa il pulsante per la sottrazione
button_sottrazione = tk.Button(window, text = "sottrazione",command=sottrazione)
button_sottrazione.grid(row=14,column=0,sticky="W")

# Qui si implementa il pulsante per la divisione
button_divisione = tk.Button(window, text = "divisione",command= divisione)
button_divisione.grid(row=18,column=0,sticky="W")

# Qui si implementa il pulsante per la moltiplicazione
button_moltiplicazione = tk.Button(window, text = "moltiplicazione",command=moltiplicazione)
button_moltiplicazione.grid(row=22,column=0,sticky="W")

# Inizializzazione loop per mantenere la tabella aperta
if __name__ == "__main__":
    window.mainloop()