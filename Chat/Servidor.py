from socket import *
from threading import Thread

#Informações do servidor
servidor = "127.0.0.1"
porta = 43210
l = []

#Funçao que realiza a comunicação do chat entre os clientes
def chat_clientes(a, b):
    msg = ""
    while str(msg).upper()  != "FIM":
        print("Conversa inciada...")
        msg = l[a].recv(5000)
        if not msg:
            break
        l[b].sendall(msg)
    con.close()

#Inicialização do servidor
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen()

#Laço de repetição para conexão de clientes
for i in range(2):
    # Esperando que um cliente seja conectado ao servidor
    print("Aguardando cliente......")
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    l.append(con)

#Nesse caso dois clientes para se comunicarem por meio do servidor
cli1 = Thread(target=chat_clientes, args=(1,0)).start()
cli2 = Thread(target=chat_clientes, args=(0,1)).start()