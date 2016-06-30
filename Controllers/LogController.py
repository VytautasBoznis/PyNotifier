import os
import logging
import time

#region Variables

log_path = os.path.dirname(os.path.realpath(__file__)) + "\logs"
file_name = "PyNotifier_log_"+time.strftime("%Y_%b_%d")+".log"

#endregion


class LogController:

    def __init__(self):
        print("LogController starting")

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        logging.basicConfig(filename=os.path.join(log_path, file_name), level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        print("LogController online")

    def getLogger(self,name):
        return logging.getLogger(name);
