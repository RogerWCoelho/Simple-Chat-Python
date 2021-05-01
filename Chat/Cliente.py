import threading
import time
from socket import *
from threading import Thread

#Informações do servidor
servidor = "127.0.0.1"
porta = 43210

#Função para o recebimento da mensagem
def recebe_msg(obj_socket):
    while True:
        msg = obj_socket.recv(1024)
        if not(len(msg)):
            break
        print("Mensagem recebida: ", msg.decode())

#Envia a mensagem no chat
def envia_msg(obj_socket):
    while True:
        msg = bytes(input("Sua mensagem: "), 'utf-8')
        try:
            obj_socket.send(msg)
        except socket.error:
            break
        if str(msg).upper() == "FIM":
            obj_socket.close()
            break

#Função do cliente
def client(servidor, porta):

    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))

    envia = Thread(target=envia_msg, args=(obj_socket,))
    recebe = Thread(target=recebe_msg, args=(obj_socket,))

    envia.start()
    recebe.start()

    while threading.active_count() > 1:
        time.sleep(0.1)
    print("Conexão encerrada!")

#Inicializa o cliente
if __name__ == '__main__':
    client(servidor,porta)