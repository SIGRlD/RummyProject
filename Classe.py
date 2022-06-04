from fonction import envoyer, recevoir, demandeutilisateur, memoire, Switchplateau2, newpioche, Winner, switch, pointfindepartie, printTab, printPlateau, Tabremove, mel, rangement, menuprincipal
from variable import jeu, plateau, plateau2, plateau3, plateau4, defausse

class Carte :
    couleur = "";
    #couleur=("coeur" "carreau" "pique" "trefle" "joker")
    nombre = 0;
    numero = 0;
    nom = "";
    def setCarte(self, i):
        if(0<=i%54<13):
            self.couleur="coeur";
        if(26>i%54>=13):
            self.couleur="carreau";
        if(39>i%54>=26):
            self.couleur="pique";
        if(52>i%54>=39):
            self.couleur="trefle";
        if(i%54>=52):
            self.couleur= "joker";
        if(i>=54):
            self.nombre=(i-54)%13 +1;
        else:
            self.nombre=i%13 +1;
        self.numero=i;
        if(self.nombre==1):
                self.nom = "As";
        elif(self.nombre==11):
            self.nom = "Valet";
        elif(self.nombre==12):
            self.nom = "Dame";
        elif(self.nombre==13):
            self.nom = "Roi";
        else:
            self.nom = str(self.nombre);
        
class Identique :
    attribut= 0;
    valeur=0;
    joker=0;
    #0=non 1=oui
    
    
    def setIdentique(self, longueur, jok):
        self.clmanquante=["coeur","carreau","pique","trefle"];
        self.tab=[];
        self.joker=jok;
        if(jok==0):
            if(longueur==3):
                if(plateau2[1].nombre==plateau2[2].nombre):
                    self.valeur=plateau2[0].nombre;
                    for i in range(0,3):
                        self.clmanquante.remove(plateau2[i].couleur);
                    if(len(self.clmanquante)!=1):
                        return 1; #erreur
            else:
                if(plateau2[1].nombre==plateau2[2].nombre==plateau2[3].nombre):
                    self.valeur=plateau2[0].nombre;
                    for i in range(0,4):
                        self.clmanquante.remove(plateau2[i].couleur);
                    if(len(self.clmanquante)!=0):
                        return 1; #erreur
        else:
            if(longueur==3):
                self.valeur=plateau2[0].nombre;
                for i in range(0,2):
                    self.clmanquante.remove(plateau2[i].couleur);
                if(len(self.clmanquante)!=2):
                    return 1; #erreur
            else:
                if(plateau2[1].nombre==plateau2[2].nombre):
                    self.valeur=plateau2[0].nombre;
                    for i in range(0,3):
                        self.clmanquante.remove(plateau2[i].couleur);
                    if(len(self.clmanquante)!=1):
                        return 1; #erreur
        for i in range(0, longueur):
            self.tab.append(plateau2[i]);
        return 0;
    
    def point(self):
        if(self.valeur>=10):
            valeur=10;
        else:
            valeur=self.valeur;
        return valeur*(4-len(self.clmanquante));
    
    def ajout(self,carte,connexion):
        #data="";
        if(carte.nombre==self.valeur and carte.couleur!="joker"):
            for i in range (0,len(self.clmanquante)):
                if(carte.couleur==self.clmanquante[i]):
                    self.clmanquante.remove(carte.couleur);
                    self.tab.append(carte);
                    rangement(self.tab);
                    plateau2.remove(carte);
                    """if(self.joker==1):
                        if(len(self.tab)==5):
                            envoyer(connexion, "Vous avez récuperé le joker.");
                            plateau2.append(self.tab[-1]);
                            self.tab.remove(self.tab[-1]);
                        else:
                            choix=0;
                            while(choix!="oui" and choix!="non"):
                                choix, data = demandeutilisateur(connexion, "Voulez vous prendre le joker ?(oui non)")
                            if(choix=="oui"):
                                plateau2.append(self.tab[-1]);
                                self.tab.remove(self.tab[-1]);"""
                    return 0; #pas d'erreur
        if(carte.couleur=="joker" and len(self.clmanquante)!=0 and self.joker==0):
            self.tab.append(carte);
            plateau2.remove(carte);
            return 0; #pas d'erreur
        return 1; #erreur
    
class Suite:
    attribut=1;
    debut=0;
    fin=0;
    couleur="";
    joker=-1; #-1=non et sinon valeur
    
    def setSuite(self, longueur, jok, connexion):
        self.tab=[];
        self.couleur=plateau2[0].couleur;
        data="";
        choix="";
        if(jok==0):
            if(plateau2[0].nombre==1 and plateau2[1].nombre!=2):
                Switchplateau2(0,"fin");
            elif(plateau[-1].nombre==13 and plateau[0].nombre==1):#ajout du choix dans ce cas très particulier où on a une suite de 1 à roi
                while(choix!="debut" and choix!="fin"):
                    data+=("voulez-vous jouer l'as au début ou à la fin de la suite?(début ou fin)")
                    choix=demandeutilisateur(connexion, data);
                    data="";
                if(choix=="fin"):
                    Switchplateau2(0,"fin");
            self.debut=plateau2[0].nombre;
            for i in range(1,longueur):
                if(plateau2[i].couleur!=self.couleur or (plateau2[i].nombre!=self.debut+i and (i!=longueur-1 or plateau2[-1].nombre!=1 or plateau2[-2].nombre!=13))):
                    return 1;
        else:
            test=1;
            while(test==1):
                self.debut=plateau2[0].nombre;
                if(self.debut==1):
                        test=0;
                if(test==1):
                    test=2;
                i=1;
                while(i<longueur):
                    if(plateau2[i].couleur!=self.couleur and plateau2[i].couleur!="joker"):
                        return 1;
                    if(plateau2[i].nombre!=self.debut+i and (plateau2[i].nombre!=1 or plateau2[i-1].nombre!=13) and (plateau2[i].nombre!=1 or plateau2[i-1].couleur!="joker" or plateau2[i-2].nombre!=12)):
                        if(self.joker==-1):
                            self.joker=self.debut+i;
                            Switchplateau2(-1, i);
                        else:
                            if(test==2):
                                return 1;
                            else:
                                test=1;
                                rangement(plateau2);
                                Switchplateau2(0, longueur-2);
                                self.joker=-1;
                                i=longueur-1;
                    i+=1;
            if(plateau2[-1].couleur=="joker"):
                if(plateau2[-2].nombre==1):
                    Switchplateau2(-1, 0);
                    self.debut-=1;
                    self.joker=self.debut;
                elif(plateau2[0].nombre!=1):
                    placejoker="";
                    while(placejoker!="debut" and placejoker!="fin"):
                        placejoker, data = demandeutilisateur(connexion,"Voulez vous placer le joker au début ou à la fin ?(debut, fin)");
                    if(placejoker=="debut"):
                        Switchplateau2(-1, 0);
                        self.debut-=1;
                        self.joker=self.debut;
        if(plateau2[-1].couleur=="joker"):
            self.fin=plateau2[-2].nombre+1;
        elif(plateau2[-1].nombre==1):
            self.fin=14;
        else:
            self.fin=plateau2[-1].nombre;
        for i in range(0, longueur):
            self.tab.append(plateau2[i]);
        return 0;
    
    def point(self):
        points=0;
        for i in range(0, len(self.tab)):
            if(i==len(self.tab)-1 and self.tab[i].nombre==1 and self.tab[i].couleur!="joker"):
                points+=11;
            elif(self.tab[i].couleur!="joker"):
                if(self.tab[i].nombre>=10):
                    points+=10;
                else:
                    points+=self.tab[i].nombre;
        return points;
    
    def ajout(self,connexion): 
        longueur=len(plateau2);
        rangement(plateau2);
        
        for i in range(0, longueur):
            if(len(self.tab)==13):
                envoyer(connexion,"La suite est déjà complète");
                return 1;
            
            if(plateau2[i].couleur!="joker" and plateau2[i].couleur!=self.couleur):
                return 1;
            if(plateau2[i].nombre==1 and self.fin==13 and plateau2[i].couleur!="joker"):#cas As
                if(self.debut==2):#si le max est Roi ET le min est un As
                    plas=0;
                    while(plas!="sous" and plas!="sur"):#On demande
                        plas, data = demandeutilisateur(connexion,"Voulez vous jouer l'As sous le 2 ou sur le Roi?(sous ou sur)");
                    if(plas=="sous"):#On joue sous le 2
                        self.debut=1;
                        Suite.Inser(self, plateau2[i], 0);
                        return 0;
                    else:
                        self.fin=14;
                        Suite.Inser(self, plateau2[i], "fin");
                        return 0;
                else:#As joué et Roi en max sans 2 en min
                    self.fin=14;
                    Suite.Inser(self, plateau2[i], "fin");
                    return 0;
                
                 
            if(plateau2[i].nombre==self.debut-1):#cas habituel
                self.debut-=1;
                Suite.Inser(self, plateau2[i], 0);
                return 0;
            if(plateau2[i].nombre==self.fin+1):#cas habituel
                self.fin+=1;
                Suite.Inser(self, plateau2[i], "fin");
                return 0;
                    
        if(self.joker==-1 and plateau2[-1].couleur=="joker"):#Si on a rien pu jouer du tableau
            for i in range (0, longueur):
                if(plateau2[i].nombre==self.debut-2 and plateau2[i].couleur!="joker"):
                    self.debut-=2;
                    Suite.Inser(self, plateau2[-1], 0);
                    self.joker==self.debut+1;
                    Suite.Inser(self, plateau2[i], 0);
                    return 0;
                elif(plateau2[i].nombre==self.fin+2 and plateau2[i].couleur!="joker"):
                    self.fin+=2;
                    Suite.Inser(self, plateau2[-1], "fin");
                    self.joker=self.fin-1;
                    Suite.Inser(self, plateau2[i], "fin");
                    return 0;
                if(i==longueur-1):
                    place=0;
                    while(place!="sous" and place!="sur"):
                        place, data = demandeutilisateur(connexion,"Voulez vous jouer le joker au dessus ou en dessous de la suite?(sur ou sous)");
                    if(place=="sous" and self.debut!=1):
                        self.debut-=1;
                        self.joker=self.debut;
                        Suite.Inser(self, plateau2[-1], 0);
                        return 0;
                    elif(self.fin!=14):
                        self.fin+=1;
                        self.joker=self.fin;
                        Suite.Inser(self, plateau2[-1], "fin");
                        return 0;
        return 1;
    
    def Inser(self, carte, place):
        plateau2.remove(carte);
        if(place=="fin"):
            self.tab.append(carte);
        else:
            self.tab.insert(place,carte);