# description: test_socket
# date: 2021/2/4 22:41
# author: objcat
# version: 1.0

import socket


def http():
    """
    基于socket的http协议
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        print(data)
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("hello world".encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    http()
