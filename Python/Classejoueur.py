from Classe import Carte, Identique, Suite
from fonction import envoyer, recevoir, demandeutilisateur, memoire, Switchplateau2, newpioche, Winner, switch, pointfindepartie, printTab, printPlateau, Tabremove, mel, rangement, menuprincipal
from variable import jeu, plateau, plateau2, plateau3, plateau4, defausse

class Joueur:
    demarrer=0;
    point=0;
    
    def setJoueur(self,con):
        self.tab=[];
        self.demarrer=0;
        self.connexion=con;
        for i in range(1,14):
            self.tab.append(jeu[-1]);
            jeu.remove(jeu[-1]);
    
    def Print(self):
        printPlateau(plateau,self.connexion);
        rangement(self.tab);
        printTab(self.tab,self.connexion,"Votre jeu :\n");
        if(len(plateau2)>0):
            envoyer(self.connexion,"\tVotre coup :\n");
            printTab(plateau2,self.connexion);
        envoyer(self.connexion,"--------------------------------\n");
               
    def pioche(self):
        pioche="";
        data="";
        if(len(defausse)!=0):
            self.Print();
            if(defausse[-1].couleur!="joker"):
                data+=("defausse : ");
                data+=str(defausse[-1].nom);
                data+=(" de ");
                data+=str(defausse[-1].couleur);
            else:
                data+=("defausse : joker");
            while(pioche!="pioche" and pioche!="defausse" and pioche!="défausse"):
                data+=("\nVoulez-vous piocher une carte de la pioche ou la dernière de la défausse?(pioche ou defausse)");
                pioche, data = demandeutilisateur(self.connexion,data);
            if(pioche=="defausse" or pioche=="défausse"):
                self.tab.append(defausse[-1]);
                defausse.remove(defausse[-1]);
            if(pioche=="pioche"):
                self.tab.append(jeu[-1]);
                if(jeu[-1].couleur !="joker"):
                    data+=("\tVous avez pioché : ");
                    data+=str(jeu[-1].nom);
                    data+=(" de ");
                    data+=str(jeu[-1].couleur);
                else:
                    data+=("\tVous avez pioché un joker");
                data=envoyer(self.connexion,data);
                jeu.remove(jeu[-1]);
        else:
            self.tab.append(jeu[-1]);
            jeu.remove(jeu[-1]);

    def defausse(self):
        carte="-1";
        if(len(self.tab)!=0):
            self.Print();
            data=("Choisissez de quelle carte vous voulez vous défausser.\n");
            while(1):
                data+=("\nChoisir le numéro de la carte :");
                carte, data = demandeutilisateur(self.connexion,data);
                try:
                    carte=int(carte);
                    if(1<=carte<=len(self.tab)):
                        defausse.append(self.tab[carte-1]);
                        self.tab.remove(self.tab[carte-1]);
                        return 0;
                    else:
                        data+=("Choisissez une carte qui existe.");
                except:
                    data+=("Seul les numéros sont acceptés.");
                    

    def Demarrer(self,limite):
        self.Print();
        point=0;
        jouer, data = demandeutilisateur(self.connexion,"\nVoulez vous jouer ou passer votre tour? (jouer, passer: autre)");
        if(jouer=="jouer"):
            fini="non";
            while(fini=="non"):
                carte=-1;
                self.Print();
                data+=("Choisissez quelles cartes vous voulez jouer ensemble puis appuyer sur 0.\n");
                while(carte!=0):
                    data+=("Choisir le numéro de la carte(0 pour terminer):\n");
                    carte, data = demandeutilisateur(self.connexion,data);
                    try:
                        carte=int(carte);
                        if(1<=carte<=len(self.tab)):
                            plateau2.append(self.tab[carte-1]);
                            self.tab.remove(self.tab[carte-1]);
                            self.Print();
                        elif(carte!=0):
                            data+=("Choisissez une carte qui existe.");
                    except:
                        data+=("Seul les numéros sont acceptés.");
                a=Joueur.newpaquet(self);
                if(a==0):
                    if(plateau3[-1].attribut==0):
                        point+=Identique.point(plateau3[-1]);
                    else:
                        point+=Suite.point(plateau3[-1]);
                else:
                    for i in range(0,len(plateau2)):
                        self.tab.append(plateau2[i]);
                    Tabremove(plateau2);
                fini="";
                while(fini!="oui" and fini!="non"):
                    data+=("Nombre de points :");
                    data+=str(point);
                    data+=(" sur ");
                    data+=str(limite);
                    data+=("\nAvez vous fini? (oui ou non)");
                    fini, data = demandeutilisateur(self.connexion,data);
            if(point<limite):
                for i in range(0,len(plateau3)):
                    for j in range(0, len(plateau3[i].tab)):
                        self.tab.append(plateau3[i].tab[j]);
                Tabremove(plateau3);
            else:
                longueur=len(plateau3);
                if(longueur!=0):
                    for i in range(0,longueur):
                        plateau.append(plateau3[i]);
                    Tabremove(plateau3);
                self.demarrer=1;
        else:
            return 0;
        
    def choisircarte(self,indice): #main:0 plateau4:1 main + printplateau4:2
        carte=-1;
        data=""
        if(indice==0):
            self.Print();
            data+=("Choisissez quelles cartes de votre main vous voulez jouer puis appuyer sur 0.");
        else:
            self.Print();
            rangement(plateau4);
            printTab(plateau4,self.connexion);
            if(indice==2):
                data+=("\nChoisissez quelles cartes de votre main vous voulez jouer puis appuyer sur 0.");
            else:
                data+=("\nChoisissez quelles cartes des coups choisis vous voulez jouer puis appuyer sur 0.");
        while(carte!=0):
            data+=("\nChoisir le numéro de la carte(0 pour terminer):");
            carte, data = demandeutilisateur(self.connexion,data);
            try:
                carte=int(carte);
                if((indice==0 or indice==2) and (1<=carte<=len(self.tab))):
                    plateau2.append(self.tab[carte-1]);
                    self.tab.remove(self.tab[carte-1]);
                    self.Print();
                elif(indice==1 and (1<=carte<=len(plateau4))):
                    plateau2.append(plateau4[carte-1]);
                    plateau4.remove(plateau4[carte-1]);
                    printTab(plateau4,self.connexion);
                    if(len(plateau2)>0):
                        data+=("\tVotre coup ");
                        data=envoyer(self.connexion,data);
                    printTab(plateau2,self.connexion);
                elif(carte!=0):
                    data+=("Choisissez une carte qui existe.");
            except:
                data+=("Seul les numéros sont acceptés.");
                    
    def coup(self):
       global plateau;
       coup="";
       while(coup!="terminer"):
           self.Print();
           while(coup!="creer" and coup!="ajouter" and coup!="terminer"):
               coup, data = demandeutilisateur(self.connexion,"Voulez vous créer un nouveau coup, jouer sur d'autres cartes ou terminer votre tour(creer, ajouter, terminer)");
           if(coup!="terminer"):
               
               if(coup=="ajouter"):
                   tour="";
                   while(tour!="oui" and tour!="non" and tour!="fini"):
                       tour, data = demandeutilisateur(self.connexion,"Voulez vous modifier le plateau ?(oui, non) Avez vous terminer? (fini)");
                   if(tour=="non" or tour=="oui"):
                       if(tour=="non"):
                           self.Print();
                           suite, data = demandeutilisateur(self.connexion,"Sur quelle suite voulez-vous ajouter quelque-chose ? (0 pour annuler)");
                           while(len(plateau)<suite or suite<0):
                               suite, data = demandeutilisateur(self.connexion,"Choisissez une suite qui existe.");
                           if(suite!=0):
                               suite-=1;
                               Joueur.choisircarte(self,0);
                               if(plateau[suite].attribut==0):
                                   while(len(plateau2)!=0):
                                       erreur=Identique.ajout(plateau[suite],plateau2[0],self.connexion);
                                       if(erreur==1):
                                           self.tab.append(plateau2[0]);
                                           plateau2.remove(plateau2[0]);
                               else:
                                   while(len(plateau2)!=0):
                                       erreur=Suite.ajout(plateau[suite],self.suite);
                                       if(erreur==1):
                                           for i in range(0,len(plateau2)):
                                                self.tab.append(plateau2[i]);
                                           Tabremove(plateau2);

                       else:
                           suite=-1;
                           mainmem=memoire(self.tab);
                           plateaumem=memoire(plateau);
                           while(suite!=0):
                               self.Print();
                               suite,data=demandeutilisateur(self.connexion,"Quelle suite voulez vous modifier?(0 pour annuler)");
                               suite=int(suite);
                               while(suite<0 or suite>len(plateau)):
                                   suite, data = demandeutilisateur(self.connexion,"Choisisez une suite qui existe.");
                                   suite=int(suite);
                               if(suite!=0):
                                   for i in range(0,len(plateau[suite-1].tab)):
                                       plateau4.append(plateau[suite-1].tab[i]);
                                   plateau.remove(plateau[suite-1]);
                           stop="non";
                           while(len(plateau4)!=0 and stop=="non"):
                               Joueur.choisircarte(self,1);
                               Joueur.choisircarte(self,2);
                               erreur=Joueur.newpaquet(self);
                               if(erreur==1):
                                   for i in range(0,len(plateau2)):
                                       Joueur.retournermain(self,mainmem,i);
                                   Tabremove(plateau2);
                               if(len(plateau4)!=0):
                                   stop="";
                                   while(stop!="oui" and stop!="non"):
                                       stop, data = demandeutilisateur(self.connexion,"Voulez vous abandonner?(oui ou non)");
                           if(stop=="oui"):
                               plateau=memoire(plateaumem);
                               self.tab=memoire(mainmem)
                               Tabremove(plateau4);
                           else:
                               for i in range(0, len(plateau3)):
                                   plateau.append(plateau3[i])
                               Tabremove(plateau3);
                           
               if(coup=="creer"):
                   Joueur.choisircarte(self,0);
                   erreur=Joueur.newpaquet(self);
                   if(erreur==1):
                       for i in range(0,len(plateau2)):
                           self.tab.append(plateau2[i]);
                       Tabremove(plateau2);
                   else:
                       plateau.append(plateau3[0]);
                       Tabremove(plateau3);
       return 0;
    
    def newpaquet(self):
        joker=0;
        a=len(plateau2);
        if(a<=2):
            envoyer(self.connexion,"Vous n'avez pas pris assez de cartes");
            return 1;
        rangement(plateau2);
        if(plateau2[-1].couleur=="joker"):
            if(plateau2[-2].couleur=="joker"):
                envoyer(self.connexion,"error:too many joker");
                return 1;
            joker=1;
        if(a<=4):
            if(plateau2[0].nombre==plateau2[1].nombre):
                A=Identique();
                result=Identique.setIdentique(A, a, joker);
                if(result==0):
                    plateau3.append(A);
                    Tabremove(plateau2);
                else:
                    return 1;
            else:
                A=Suite();
                result=Suite.setSuite(A,a, joker,self.connexion);
                if(result==0):
                    plateau3.append(A);
                    Tabremove(plateau2);
                else:
                    return 1;
        else:
            A=Suite();
            result=Suite.setSuite(A,a,joker,self.connexion);
            if(result==0):
                plateau3.append(A);
                Tabremove(plateau2);
            else:
                return 1;
        return 0;
    
    def retournermain(self,mainmem,i):
        for j in range(0,len(mainmem)):
            if(plateau2[i].numero==mainmem[j].numero):
                self.tab.append(plateau2[i]);
                return 0;
        plateau4.append(plateau2[i]);
        return 0;