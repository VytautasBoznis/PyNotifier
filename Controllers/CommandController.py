from pip.utils import logging
import sys
import threading
import queue

class CommandController:

    #region Variables

    running = True

    #endregion

    def __init__(self,logger = (logging)):
        self.logger = logger
        self.logger.info("Command controller online")

    #region Commands

    def getHelp(self):
        print("Possible commands: ")
        print("exit - Closes PyNotifier")
        print("help - Shows all posible commands")

    def quit(self):
        self.logger.info("Closing PyNotifier...")
        print("Closing PyNotifier...")
        sys.exit(1)

    def invalid_input(self,command):
        print("--> Unknown command '"+command+"' use 'help' for commands")
    #endregion

    def handleInput(self,command):
        if command == "help":
            self.getHelp()
        elif command == "exit":
            self.quit()
        else:
            self.invalid_input(command)
