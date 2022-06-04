import sys
import socket

host = '192.168.200.10'
port = 6000

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

try:
    Socket.connect((host,port));
    print("Connexion établie");
except socket.error  :
    print("Connexion echoué avec le serveur");
    sys.exit();
 

data=Socket.recv(1024);
data=data.decode("utf8");
print(data);


while(1):
    data=Socket.recv(2048);
    data=data.decode("utf8");
    if(data[-1]=="z" and data[-2]=="z"):
        data=data.replace("zz","");
        print(data);
        
        reponse=input();
        if(reponse==""):
            reponse=" ";
            reponse=reponse.encode("utf8");
            Socket.sendall(reponse);
        elif(reponse!="break" and reponse!="Break"):
            reponse=reponse.encode("utf8");
            Socket.sendall(reponse);
        elif(reponse=="break" or reponse=="Break"):
            break;
    else:
        print(data);
    
    

Socket.close();