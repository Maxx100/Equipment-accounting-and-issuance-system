import socket
import sqlalchemy as sql


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1337))
s.listen()
conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(16 + 64 + 64).decode()
    data = [data[:16].lstrip(" "),
            data[16:16 + 64].lstrip(" "),
            data[16 + 64:16 + 64 + 64].lstrip(" ")]
    print(data)
    conn.sendall(b"ok")
# conn.close()
