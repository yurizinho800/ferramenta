from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
import socket

def iniciar():
#Construir a requisição ARP
 ether = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=input("\033[94mDigite o seu IP verificado anteriormente:\033[0m").split("/")[0]+"/24") 

#Enviar e receber respostas
 respostas, nao_respondidos = srp(ether, timeout=2, verbose=0) 

 for resposta in respostas:
     for resposta in respostas:
        ip = resposta[1].psrc
        mac = resposta[1].hwsrc
        try:
            nome = socket.gethostbyaddr(ip)[0]
        except:
            nome = "Desconhecido"
        try:
            fabricante = MacLookup().lookup(mac)
        except:
            fabricante = "Fabricante não identificado"

        print(f"\033[92mIP: {ip}\033[0m | \033[94mMAC: {mac}\033[0m | \033[93mNome: {nome}\033[0m | \033[96mFabricante: {fabricante}\033[0m")

    
 salvar = input("Deseja salvar os resultados em um arquivo? (s/n): ")
 
 if salvar.lower() == "s":
        with open("resultados.txt", "w") as arquivo:
          for resultado in respostas:
            arquivo.write(f"IP: {resultado[1].psrc} MAC: {resultado[1].hwsrc}\n")
        print("Resultados salvos em resultados.txt")


