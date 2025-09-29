import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"{addr}: {msg}")
            
            for client in clients:
                if client != conn:
                    client.send(f"{addr}: {msg}".encode('utf-8'))
        except:  # noqa: E722
            break
    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECTED] {addr} left")
    
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen()
    print("[SERVER STARTED] Waiting for connections...")
    
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
if __name__ == "__main__":
    start_server()