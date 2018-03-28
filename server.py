from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

connection_port = 1025
data_port = 1024
server_host = ''


def main():
    while True:
        server_socket = socket(AF_INET, SOCK_STREAM)

        #to allow reuse of socket's address('') in while loop
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # two parentheses due to bind() only accepting one argument and requiring a tuple
        server_socket.bind(('', connection_port))

        # set server_socket to listen for one connection
        server_socket.listen(5)

        print "server waiting for connection"

        connection_socket, client_address = server_socket.accept()

        data_socket = socket(AF_INET, SOCK_STREAM)
        data_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        data_socket.bind(('', data_port))
        data_socket.listen(5)
        print "server waiting for data"

        s, a = data_socket.accept()

        data_length = ""
        data_length += s.recv(255)
        data_length = int(data_length)

        tmpbuffer = ""
        data = ""

        while len(data) < data_length - 1:
            tmpbuffer = s.recv(40)
            data += tmpbuffer
        print data

        s.close()
        data_socket.close()
        connection_socket.close()
if __name__ == "__main__":
    main()