from pydoc import Doc
from tkinter import*
from math import*
import time
import timeit
from tkinter import * 
import tkinter as tk
from datetime import datetime

def valider():
    recup_nom=nom1.get()
    recup_prenom=prenom1.get()
    recup_age=age1.get()
    recup_lieu_de_naissance=lieu_de_naissance1.get()
    recup_raison_de_venue=raison_de_venue1.get()
    doc= open ("", "a+") #nom du fichier dans lequel écrire    
    doc.write("NOM : ")
    doc.write (recup_nom)
    doc.write("|||")
    doc.write("PRENOM : ")
    doc.write(recup_prenom) 
    doc.write("|||") 
    doc.write("AGE : ")
    doc.write(recup_age)
    doc.write("|||")
    doc.write("LIEU DE NAISSANCE : ")
    doc.write(recup_lieu_de_naissance)
    doc.write("|||")
    doc.write("RAISON DE VENUE : ")
    doc.write(recup_raison_de_venue)
    doc.write("|||")
    doc.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    doc.write("\n")
    doc.close()
    
    

def clear():
    nom1.delete(0, END)
    prenom1.delete(0, END)
    age1.delete(0, END)
    lieu_de_naissance1.delete(0, END)
    raison_de_venue1.delete(0, END)

root = tk.Tk()
root.geometry("360x340")
root.title("POINTAGE")



nom = Label(root,text="Entrez votre Nom : ")
nom.pack()
nom1=Entry(root,width=20)
nom1.pack()

prenom=Label(root,text="Entrez votre Prénom : ")
prenom.pack()
prenom1=Entry(root,width=20)
prenom1.pack()

age=Label(root,text="Entrez votre âge : ")
age.pack()
age1=Entry(root,width=20)
age1.pack()

lieu_de_naissance=Label(root,text="Entrez votre lieu de naissance : ")
lieu_de_naissance.pack()
lieu_de_naissance1=Entry(root,width=20)
lieu_de_naissance1.pack()

raison_de_venue=Label(root,text="Entrez la raison de votre venue : ")
raison_de_venue.pack()
raison_de_venue1=Entry(root,width=20)
raison_de_venue1.pack()



quitter=Button(root, text="Fermer", command=root.quit)
quitter.pack()

valider=Button(root,text="Valider",command=valider)
valider.pack()

reinitialiser_les_champs=Button(root,text="Supprimer les champs",command=clear)
reinitialiser_les_champs.pack()

root.mainloop()
