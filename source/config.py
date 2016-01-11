__author__ = 'clayton-peterson'

import os

ADDRESS = "0.0.0.0"
PORT = ""

# get path to the configuration file
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, 'configuration.txt')


def load():
    # load the previous port configuration when the program starts
    config_file = open(file_path, 'r')
    for line in config_file:
        if line[0] == "PORT":
            global PORT
            PORT = int(line[2])

    # close the configuration file
    config_file.close()


def edit():
    # request a port from the user
    global PORT
    PORT = raw_input("port > ")

    # save the address and port to the configuration file
    config_file = open(file_path, 'w')
    config_file.write("ADDRESS = " + ADDRESS + "\n")
    config_file.write("PORT = " + PORT + "\n")


# load the configuration from the previous run
load()


if __name__ == "__main__":
    edit()
