import socket
import data.excel_engine as ee


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1337))

if __name__ == "__main__":
    excel = ee.Excel()
    s.listen()
    conn, addr = s.accept()
    print(f"Client: {addr}")

    while True:
        data = conn.recv(16 + 64 + 64).decode()
        data = [data[:16].lstrip(" "),
                data[16:16 + 64].lstrip(" "),
                data[16 + 64:16 + 64 + 64].lstrip(" ")]
        print(data)
        if "ok":
            conn.sendall(b"ok")
            excel.add(ident=int(data[0]), equipment=data[1], _type=data[2])

        else:
            conn.sendall(b"Access denied")
    # conn.close()
