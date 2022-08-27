import socket
# binding ports and crap
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

hostname = socket.gethostname()  
SERVER_HOST = socket.gethostbyname(hostname)
print("Listening as", SERVER_HOST)
serversocket.listen(5)
conn, addr = serversocket.accept()
with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
            conn.sendall(data)