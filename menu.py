import descobrir
import scanner

def menu():

 print("descobrir  o  ip:  [1]")
 print("quem está na rede: [2]")

 escolha = input("Escolha uma opção:   ")
 if escolha == "1":
    descobrir.get_gateway_windows()
 elif escolha == "2":
  scanner.iniciar()
    


menu()
