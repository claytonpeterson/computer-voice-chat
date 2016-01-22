__author__ = 'clayton-peterson'

'''
liberally sampled from
http://www.binarytides.com/code-chat-application-server-client-sockets-python
'''

import socket
import select
import sys
import re
import config
from os import system

ADDRESS = ""
PORT = ""


def prompt():
    """
    prompts the client for text input
    """
    sys.stdout.write("> ")
    sys.stdout.flush()


def create_socket_connection():
    """
    :return: a socket connection to the given host server
    """
    # create a socket connection
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.settimeout(2)

    # connect to remote host
    try:
        new_socket.connect((ADDRESS, PORT))
    except:
        print 'unable to connect'
        sys.exit()

    return new_socket


def run():
    """
    allows the client to send and receive messages from
    the server
    """
    # ask the user for the host I.P address
    global ADDRESS
    ADDRESS = raw_input("IP address > ")

    # ask the user for the host port
    global PORT
    PORT = int(raw_input("Port > "))

    # creates a socket connection to the chat server
    my_socket = create_socket_connection()

    # greet the user and prompt them for input
    print 'voice = ' + config.VOICE
    print 'connected to remote host. start typing!'
    prompt()

    while True:
        socket_list = [sys.stdin, my_socket]

        # get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:

            # 1. an incoming message from the remote server
            if sock == my_socket:
                data = sock.recv(4096)
                if not data:
                    print '\n disconnected from chat server'
                    sys.exit()
                else:
                    # strip the extra data from the message
                    message = re.sub('<[^>]+>', '', data)

                    # extract the speakers voice, voice-speed, and message
                    message = message.split()
                    speakers_voice = message.pop()
                    speakers_voice_speed = message.pop()
                    message = " ".join(message)

                    system('say -v ' + speakers_voice + ' -r ' + speakers_voice_speed + ' ' + message)
                    # system('say -r 140'+message)

            # 2. a user entered a message
            else:
                msg = sys.stdin.readline()
                my_socket.send(msg + " " + str(config.VOICE_SPEED) + " " + config.VOICE + " ")
                prompt()

if __name__ == "__main__":
    run()
