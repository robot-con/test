import socket
import threading


def fun_ser(conn,addr):
    data = conn.recv(5000)
    if not data:
        conn.close()
    print(data.decode())
    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n  server ok".encode())

    while True:
        dt = conn.recv(5000)
        if not dt:
            conn.close()
            break

        print(dt.decode())
        conn.send(f"data receive: {dt}".encode())        

def main():
    server = socket.socket()
    server.bind(("0.0.0.0",10000))
    server.listen(5)

    while True:
        conn , addr = server.accept()
        handel_server = threading.Thread(target=fun_ser, args=(conn,addr),daemon= True)
        handel_server.start()

if __name__=="__main__":
    main()
