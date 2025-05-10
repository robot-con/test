import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 10000))
server.listen(5)

def handel(conn):
    try:
        data = conn.recv(1020)
        if not data:
            conn.close()
        send = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"
        send += "<h1>this is socket server</h1>"
        conn.sendall(send.encode())
        conn.close()
    except Exception as e:
        conn.close()
while True:
    try:
        conn , addr =server.accept()
        print(addr)

        thread = threading.Thread(target=handel, args=(conn,),daemon= True)
        thread.start()

    except Exception as e:
        print (e)
    


