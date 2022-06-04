from time import sleep
from Classejoueur import Joueur
from Classe import Carte, Identique, Suite
from fonction import envoyer, recevoir, demandeutilisateur, memoire, Switchplateau2, newpioche, Winner, switch, pointfindepartie, printTab, printPlateau, Tabremove, mel, rangement, menuprincipal
from variable import jeu, plateau, plateau2, plateau3, plateau4, defausse


def Main(connexion1,connexion2):
    stop=0;
    manche=1;
    Tabjoueur=[];
    nbjoueur=2;
    limite=30;
    data=""
    
    for i in range (0,nbjoueur):
        player=Joueur();
        Tabjoueur.append(player);

    
    
    while(stop==0):
        joueur=0;
        vainqueur=0;
        multiplicateurdepoints=1;
        data+=("\nVous êtes à la manche ");
        data+=str(manche);
        data+=".\n";
        envoyer(connexion1, data);
        data=envoyer(connexion2, data);
        
    
        for k in range(0,108):
                A=Carte();
                jeu.append(A);
                Carte.setCarte(A,k);
        limite=menuprincipal(limite,connexion1);
        mel(jeu);
        Joueur.setJoueur(Tabjoueur[0],connexion1)
        Joueur.setJoueur(Tabjoueur[1],connexion2)
        while(vainqueur==0):
            data+=("C'est au joueur ");
            data+=str(joueur+1);
            data+=(" de jouer.");
            envoyer(Tabjoueur[0].connexion, data);
            data=envoyer(Tabjoueur[1].connexion, data);
            Tabjoueur[joueur].pioche();
            newpioche();
            if(Tabjoueur[joueur].demarrer==0):
                Tabjoueur[joueur].Demarrer(limite);
                if(len(Tabjoueur[joueur].tab)==1):
                    multiplicateurdepoints=2;
            else:
                Tabjoueur[joueur].coup();
            if(len(Tabjoueur[joueur].tab)>0):
                Tabjoueur[joueur].defausse();
                vainqueur=Winner(Tabjoueur[joueur])*(joueur+1);
            else:
                vainqueur=-joueur-1;
                Tabjoueur[joueur].point+=100;
            joueur=switch(joueur,nbjoueur);
        
        if(vainqueur>0):
            data+=("Joueur ");
            data+=str(vainqueur);
            data+=(" a gagné ce tour.");
            data=envoyer(Tabjoueur[0].connexion, data);
            data=envoyer(Tabjoueur[1].connexion, data);
            for i in range(0,nbjoueur):
                if(i!=vainqueur-1):
                    a=pointfindepartie(Tabjoueur[i])*multiplicateurdepoints;
                    Tabjoueur[i].point+=a;
                else:
                    a=0;
                data+=("Point de la manche : Joueur ");
                data+=str(i+1);
                data+=(" :");
                data+=str(a);
                data+=("\nPoint de la partie : Joueur ");
                data+=str(i+1);
                data+=(" :");
                data+=str(Tabjoueur[i].point);
                data=envoyer(Tabjoueur[0].connexion, data);
                data=envoyer(Tabjoueur[1].connexion, data);
        else:
            data+=("Joueur ");
            data+=str(-vainqueur);
            data+=(" a perdu ce tour. Cents points dans sa gueule.\n");
            for i in range(0,nbjoueur):
                if(i!=-vainqueur):
                    a=pointfindepartie(Tabjoueur[i]);
                    Tabjoueur[i].point+=a;
                data+=("Point de la manche : Joueur ");
                data+=str(i+1);
                data+=(" :");
                data+=str(a);
                data+=("\nPoint de la partie : Joueur ");
                data+=str(i+1);
                data+=(" :");
                data+=str(Tabjoueur[i].point);
                
        c="";
        while(c!="stop" and c!="manche"):
            data+=("\nVoulez vous arréter ou faire une autre manche?(stop,manche)");
            c, data = demandeutilisateur(Tabjoueur[0].connexion, data);
        if(c=="stop"):
            stop=1;
        else:
            manche+=1;
            Tabremove(jeu);
            Tabremove(defausse);
            Tabremove(plateau);
            for i in range(0,nbjoueur):
                Tabremove(Tabjoueur[i].tab);