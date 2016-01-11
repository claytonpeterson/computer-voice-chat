__author__ = 'clayton-peterson'

'''
sampled liberally from
'http://www.binarytides.com/code-chat-application-server-client-sockets-python'
'''

import socket
import select
# from config import ADDRESS, PORT


def broadcast_data(sock, message):
    """
    broadcast chat messages to all connected clients
    """
    # do not send the message to master socket and the client who has send us the message
    for socket_connection in CONNECTION_LIST:
        if socket_connection != server_socket and socket_connection != sock:
            try:
                socket_connection.send(message)
            except:
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket_connection.close()
                CONNECTION_LIST.remove(socket_connection)


def run():
    # list to keep track of socket descriptors
    global CONNECTION_LIST
    CONNECTION_LIST = []
    RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2

    # get the public network interface
    address = socket.gethostbyname(socket.gethostname())

    # ask the user for the port they want to use
    port = int(raw_input("PORT > "))

    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print "chat server started on port " + address + ":" + str(port)

    while True:
        # get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:

            # 1. new connection. handle the case in which there is a new
            # connection received through server_socket
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "client (%s, %s) connected" % addr
                broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)

            # 2. some incoming message from a client
            else:
                # data received from client, process it
                try:
                    # in windows, sometimes when a TCP program closes abruptly,
                    # a "connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
                except:
                    broadcast_data(sock, "client (%s, %s) is offline" % addr)
                    print "client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()


if __name__ == "__main__":
    run()
