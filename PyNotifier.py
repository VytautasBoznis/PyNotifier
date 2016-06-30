import logging

from Controllers.LogController import LogController
from Controllers.CommandController import CommandController

__LogController = LogController()

logger = __LogController.getLogger("Main")
logger.log(logging.INFO, "Logging online")

print("===== PyNotifier =====")
print("Starting...")
print("Starting command controller...")

__CommandController = CommandController(__LogController.getLogger("Command Controller"))

print("For possible commands type 'help'")

while 1:
    cmd = input(">")
    __CommandController.handleInput(command = cmd)




