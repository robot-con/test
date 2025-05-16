import socket

server = socket.socket()

server.bind(("0.0.0.0",10000))
server.listen(5)


while True:
    try:
        conn , addr = server.accept()
        data = conn.recv(3099)
        if not data:
            conn.close()
        
        print(data.decode())
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nConnection: keep-alive\r\n\r\nTunnel connected\n".encode())
        while True:
            data = conn.recv(3099)
            print(data.decode())
            conn.send("data recevied".encode())

    except Exception as e:
        print("conn error")
        conn.close()
    finally:
        continue
