from tkinter import*
from math import*
import time
import timeit
from tkinter import * 
import tkinter as tk

def recuperation_entry():
    recup_nom=nom1.get()
    recup_prenom=prenom1.get()
    recup_age=age1.get()
    recup_lieu_de_naissance=lieu_de_naissance1.get()
    recup_raison_de_venue=raison_de_venue1.get()
    f = open ("class.txt", "a+")    # ouverture
    f.write("NOM : ")
    f.write (recup_nom)
    f.write("|||")
    f.write("PRENOM : ")
    f.write(recup_prenom)  
    f.write("|||") # écriture de la chaîne de caractères  s
    f.write("AGE : ") # écriture de la chaîne de caractères  s
    f.write(recup_age)
    f.write("|||")
    f.write("LIEU DE NAISSANCE : ")
    f.write(recup_lieu_de_naissance)
    f.write("|||")
    f.write("RAISON DE VENUE : ")
    f.write(recup_raison_de_venue)
    f.write("\n")
    f.close ()
    print(recup_age,recup_lieu_de_naissance,recup_nom,recup_prenom,recup_raison_de_venue)
    
     # fermeturef = open ("nom-fichier", "w")    # ouverture
def clear():
    nom1.delete(0, END)
    prenom1.delete(0, END)
    age1.delete(0, END)
    lieu_de_naissance1.delete(0, END)
    raison_de_venue1.delete(0, END)

root = tk.Tk()
root.geometry("1920x1080")
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

valider=Button(root,text="Valider",command=recuperation_entry)
valider.pack()

reinitialiser_les_champs=Button(root,text="Supprimer les champs",command=clear)
reinitialiser_les_champs.pack()

root.mainloop()
