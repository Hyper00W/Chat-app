import socket
import threading

def receive_message(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            print(msg)
        except:  # noqa: E722
            print('Disconnected From Server')
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1",5555))
    
    #thread to recieve message
    threading.Thread(target=receive_message, args=(client,), daemon=True).start()
    
    while True:
        msg = input("")
        client.send(msg.encode('utf-8'))
        
if __name__ == "__main__":
    start_client()