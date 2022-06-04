import sys
import socket
import time
from Jeux import Main


# collect the arguments
host = ''
port = 6060

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    Socket.bind((host,port))
    print("le serveur est mis en route")
except socket.error :
    print("le serveur ne s'est pas lancé")
    sys.exit()

Socket.listen(2)

connexion, adresse = Socket.accept()
data="Vous êtes le premier joueur. En attente du deuxième joueur..."
data=data.encode("utf8");
connexion.send(data);
print("Une personne est connectée avec pour ip ",adresse[0]," et pour port",adresse[1])
connexion2, adresse2 = Socket.accept()
data="Vous êtes le deuxième joueur. C'est parti."
data=data.encode("utf8");
connexion2.send(data);
print("Une deuxième personne est connectée avec pour ip ",adresse2[0]," et pour port",adresse2[1])

Main(connexion,connexion2);


connexion.close()
connexion2.close()
Socket.close()