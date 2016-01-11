__author__ = 'clayton-peterson'

import os

# get path to the configuration file
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, 'configuration.txt')

VOICE = 0
VOICE_SPEED = 0


def set_voice():
    # get the gender of the voice
    gender = raw_input("would you like a [m]ale or [f]emale voice?")

    global VOICE
    global VOICE_SPEED

    # if the user chooses female
    if gender == "f":
        selection = raw_input("[A]gnes, [K]athy, [P]rincess, [Vick]i, [Vict]oria")
        if selection == "A":
            VOICE = "Agnes"
        if selection == "K":
            VOICE = "Kathy"
        if selection == "P":
            VOICE = "Princess"
        if selection == "Vick":
            VOICE = "Vicki"
        if selection == "Vict":
            VOICE = "Victoria"

    # if the user chooses male
    if gender == "m":
        selection = raw_input("[B]ruce, [F]red, [J]unior, [R]alph, [W]hisper")
        if selection == "B":
            VOICE = "Bruce"
        if selection == "F":
            VOICE = "Fred"
        if selection == "J":
            VOICE = "Junior"
        if selection == "R":
            VOICE = "Ralph"
        if selection == "W":
            VOICE = "Whisper"

    # get the speaking rate for the users voice
    rate = raw_input("Rate?")
    VOICE_SPEED = int(rate)


# def load():
#     # load the previous port configuration when the program starts
#     config_file = open(file_path, 'r')
#     for line in config_file:
#         if line[0] == "PORT":
#             global PORT
#             PORT = int(line[2])
#
#     # close the configuration file
#     config_file.close()


# def edit():
#     # request a port from the user
#     global PORT
#     PORT = raw_input("port > ")
#
#     # save the address and port to the configuration file
#     config_file = open(file_path, 'w')
#     config_file.write("ADDRESS = " + ADDRESS + "\n")
#     config_file.write("PORT = " + PORT + "\n")


# load the configuration from the previous run
#load()


# if __name__ == "__main__":
#     edit()
