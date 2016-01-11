#!/usr/bin/env python

__author__ = 'clayton-peterson'

import sys
import client
import server
import config


def ask_for_mode():
    """
    asks the user if the would like to run as a server
    or a client
    """
    prompt = "press 1 to start a group chat\n" \
             "press 2 to join a group chat\n" \
             "press 3 to quit\n" \
             "> "

    # wait for the user to correctly choose an option
    choice = ""
    while choice != "1" and choice != "2" and choice != "3":
        choice = raw_input(prompt)
        print ""

    # 1. start a group chat
    if choice == "1":
        server.run()

    # 2. join a group chat
    if choice == "2":
        config.set_voice()
        client.run()

    # # 3. edit settings
    # if choice == "3":
    #     config.set_voice()
    #     print ""
    #     ask_for_mode()

    # 4. quit
    elif choice == "3":
        sys.exit()


if __name__ == "__main__":
    ask_for_mode()
