import socket
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1337  # The port used by the server


def get_time():
    return time.strftime("%H:%M:%S, %d %b %Y, %a", time.gmtime())


def data_to_bytes(lst):
    ans = b""
    for i in lst:
        if type(i) is int:
            ans += str.encode(f"{str(i):>16}")
        elif type(i) is str:
            ans += str.encode(f"{i:>64}")
        else:
            print(f"Unknown type: {type(i)}")
    return ans


def request():
    time.sleep(2)
    # get data
    data = [12, "Spotlight", "get"]  # id (int), equipment (str), get/give
    return data


while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        while True:
            s.sendall(data_to_bytes(request()))
            data = s.recv(2**16).decode()
            print(data)
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError) as error:
        print(get_time(), f"| Server offline: {error}")
        time.sleep(5)
