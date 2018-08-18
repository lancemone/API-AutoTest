from smart_app_interfacetest.config.read_conf import Read_conf
from smart_app_interfacetest.lib.LogOut import MyLog
from smart_app_interfacetest.lib.LogOut import Log
from smart_app_interfacetest.lib import LogOut

config = Read_conf()
log = MyLog.get_log()
logger = Log().get_logger()
smtpserver = config.get_email("smtp_server")
username = config.get_email("sender")
password = config.get_email("mail_pass")
sender = config.get_email("sender")
receiver = config.get_email("receiver")
port = config.get_email("mail_port")
logger.log(smtpserver, username, password, sender, receiver, port)
