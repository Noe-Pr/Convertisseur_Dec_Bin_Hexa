from tkinter import *


def convert_decimal():
    n = int(entree1.get())
    b = 0
    ord = 0
    while n != 0 :
        reste = n % 2
        p = 10 ** ord
        b = b + reste * p
        ord = ord + 1
        n = n // 2
    entree2.delete(0 , END)
    entree2.insert( 0 , b)
    
    nb = int(entree1.get())
    entree3.delete(0 , END)
    entree3.insert(0 , hex(nb))
    entree3.delete(0 , 2)
    return convert_decimal

def convert_binaire():
    n = int(entree2.get())
    resultat=0 
    nchaine=str(n) 
    nliste=list(nchaine) 
    pgexposant=len(nliste) 
    for i in range(pgexposant): 
        int(i) 
        ajout=int(nliste[i])*2**(pgexposant-1-i) 
        resultat=resultat+ajout 
    entree1.delete(0 , END)
    entree1.insert( 0 , resultat)
    
    entree3.delete(0 , END)
    entree3.insert(0 , hex(resultat))
    entree3.delete(0 , 2)
    return convert_binaire
    
    
    
def convert_hexa():
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} 
    hexadecimal = entree3.get().strip().upper()
    decimal = 0
    power = len(hexadecimal) -1
    for digit in hexadecimal:
        decimal += conversion_table[digit]*16**power
        power -= 1
    entree1.delete(0 , END)
    entree1.insert( 0 , decimal)
    
    nb = entree3.get().strip().upper()
    n = int(nb, 16) 
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1    
    res = bStr
    entree2.delete(0 , END)
    entree2.insert( 0 , str(res))
    

# Création de la fenêtre principale (main window)
mafenetre = Tk()
mafenetre.title('Convertisseur')
mafenetre.geometry('355x148')
mafenetre.resizable(width=False, height=False)
mafenetre.config(background="#000078")

# Création de l'entrée pour le décimal
dec=StringVar()
entree1 = Entry(mafenetre, textvariable = dec, font=("Courrier", 15), bg ='white', fg='black')
entree1.place(x=25,y=20)
dec.set(' Valeur décimale')

# Création de l'entrée pour le binaire
bina=StringVar()
entree2 = Entry(mafenetre, textvariable= bina, font=("Courrier", 15), bg ='white', fg='black')
entree2.place(x=25,y=60)
bina.set(' Valeur binaire')

# Création de l'entrée pour le l'hexadécimal
nbr_hexa=StringVar()
entree3 = Entry(mafenetre, textvariable= nbr_hexa, font=("Courrier", 15), bg ='white', fg='black')
entree3.place(x=25,y=100)
nbr_hexa.set(' Valeur hexadécimale')

# Création du bouton convertir
Bouton_calcul = Button(mafenetre, text = 'convertir',font=("Courrier", 11), command=convert_decimal)
Bouton_calcul.place(x=260,y=19)

# Création du bouton convertir 2
Bouton_calcul1 = Button(mafenetre, text = 'convertir',font=("Courrier", 11), command=convert_binaire)
Bouton_calcul1.place(x=260,y=59)

# Création du bouton convertir 3
Bouton_calcul2 = Button(mafenetre, text = 'convertir',font=("Courrier", 11), command=convert_hexa) 
Bouton_calcul2.place(x=260,y=99)


mafenetre.mainloop()