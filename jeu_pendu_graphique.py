from random import choice
from random import *
from tkinter import*
from liste_indice import*
top = Tk()
top.title("jeu de pendule")
les_mots = open('liste_mots.txt','rt')
les_mots = les_mots.readlines()
liste_mots = []
for c in les_mots:
    c = c.rstrip()
    liste_mots.append(c)

def afficher_mot(mot):
    # si on ne lance pas, cette variables n'existe pas par exemple
    global lettres
    mot_large = ""
    i = 0
    while i < len(mot):
        mot_large = mot_large + mot[i] + " "
        i = i + 1
    canevas.delete(lettres)
    lettres = canevas.create_text(440,60,text=mot_large, fill = 'black', font = 'Courrier 30')
def init_jeu():
    global lettres, nbre_echec, partie_en_cours, le_mot, mot_partiel
    nbre_echec = 0
    partie_en_cours = True
    le_mot = choice(liste_mots)
    mot_partiel = '-'*len(le_mot)
    canevas.delete(lettres)

    afficher_mot(mot_partiel)
    photo=PhotoImage(file="pendu_0.gif")
    image_pendu.config(image=photo)
    image_pendu.image=photo

canevas = Canvas(top, bg="white", height=1000, width=1500)
canevas.pack(side=BOTTOM)
lettres = canevas.create_text(320,60,text =" ",fill = 'black', font = 'Courrier 30')


photo=PhotoImage(file="pendu_0.gif")
image_pendu = Label(canevas,image = photo, border=0)
image_pendu.place(x=300,y=500)

bouton = [0]*26
for i in range(26):
    bouton[i] = Button(top, text=chr(i+65), command = lambda x=i+65:lettre_dans_mot(chr(x)))
    bouton[i].pack(side=LEFT)


    


    
def lettre_dans_mot(lettre):
    global partie_en_cours, nbre_echec, mot_partiel
    """
        Verifie que la lettre lettre est dans le mot
        :lettre: (str)
    """
    
    if partie_en_cours:
        afficher_mot(mot_partiel)
        if lettre not in le_mot:
            nbre_echec = nbre_echec + 1
            le_photo = 'pendu_' + str(nbre_echec) + '.gif'
            photo=PhotoImage(file=le_photo)
            
            image_pendu.config(image=photo)
            image_pendu.image=photo
            
        elif lettre in le_mot:
            les_indice = liste(le_mot,lettre)
            mot_partiel = remplace(mot_partiel,les_indice.liste_indices(),lettre)
            afficher_mot(mot_partiel)
        if mot_partiel == le_mot:
            partie_en_cours = False
            afficher_mot("Bravo vous avez réussi")
        if nbre_echec == 7:
            partie_en_cours = False
            afficher_mot("le mot était" + " " + le_mot )
            
    

    
    
bouton1 = Button(top, text = 'Recommencer', command= init_jeu)
bouton1.pack(side = RIGHT)
bouton2 = Button(top, text = 'Quitter', command= quit)
bouton2.pack(side=RIGHT)
init_jeu()
top.mainloop()