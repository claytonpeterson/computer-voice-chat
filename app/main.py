#!/usr/bin/env python

__author__ = 'clayton-peterson'

import sys
import client
import server
import config
import views


def ask_for_mode():
    """
    ask the user
    """
    prompt = "Type [A] to run through command line\n" \
             "Type [B] to run with a UI\n" \
             "Type [C] to quit\n" \
             "- "

    # wait for the user to choose an option
    choice = ""
    while choice != "A" and choice != "B" and choice != "C":
        choice = raw_input(prompt).upper()
        print ""

    # execute the selected task
    if choice == "A":
        run_text_interface()
    elif choice == "B":
        run_graphical_interface()
    elif choice == "C":
        sys.exit()


def run_text_interface():
    """
    takes command line input
    """
    prompt = "press 1 to start a group chat\n" \
             "press 2 to join a group chat\n" \
             "press 3 to quit\n" \
             "> "

    # wait for the user to choose an option
    choice = ""
    while choice != "1" and choice != "2" and choice != "3":
        choice = raw_input(prompt)
        print ""

    # run the selected option
    if choice == "1":
        server.run()
    if choice == "2":
        config.set_voice()
        client.run()
    elif choice == "3":
        sys.exit()


def run_graphical_interface():
    """
    takes input through a graphical user interface
    """
    views.app.run()


if __name__ == "__main__":
    run_graphical_interface()
    pass
