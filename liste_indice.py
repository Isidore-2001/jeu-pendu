# liste du nombre d'occurence
class liste:
    def __init__(self,mot,lettre):
        
        self.__mot = mot
        self.__lettre = lettre
        
    def liste_indices(self):
        nb = 0
        l = []
        while nb < len(self.__mot):
            if self.__mot[nb] == self.__lettre:
                l.append(nb)
            nb = nb + 1
        return l
def remplace(chaine,liste_indice,lettre):
    chaine = list(chaine)
    for c in liste_indice:
        chaine[c] = lettre
    chaine1 = ''
    for k in chaine:
        chaine1 = chaine1 + k
    return chaine1
        

        