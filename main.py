import socket
import threading
import time 

server = socket.socket()

server.bind(("0.0.0.0",10000))
server.listen(5)


def handel(conn):
    try:
        data =  conn.recv(1024)
        if not data:
            conn.close()

        data = data.decode().split()[1]
        if data == "/":

            
            while True:
                send = "hellow world\r\n"
                conn.sendall(send.encode())
                time.sleep(1)
    except Exception as e:
        conn.close()
    

while True:
    conn , addr = server.accept()
    thread = threading.Thread(target= handel, args=(conn,), daemon= True)
    thread.start()
