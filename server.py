from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

connection_port = 1025
data_port = 1024
server_host = ''


def main():
    server_socket = create_server_socket()
    server_socket.listen(5)

    print "server waiting for connection"

    connection_socket, client_address = server_socket.accept()

    while True:
        data_socket = create_data_socket()
        data_socket.listen(5)
        print "server waiting for data"

        s, a = data_socket.accept()

        data_length = receive_data_length(s)

        data = receive_data(s, data_length)
        print data

        s.close()
        data_socket.close()
        connection_socket.close()

def create_server_socket():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((server_host, connection_port))
    return server_socket

def create_data_socket():
    data_socket = socket(AF_INET, SOCK_STREAM)
    data_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    data_socket.bind((server_host, data_port))
    return data_socket

def receive_data_length(socket):
    data_length = ""
    data_length += socket.recv(255)
    data_length = int(data_length)
    return data_length

def receive_data(socket, data_length):
    tmpbuffer = ""
    data = ""
    while len(data) < data_length - 1:
        tmpbuffer = socket.recv(40)
        data += tmpbuffer
    return data

if __name__ == "__main__":
    main()