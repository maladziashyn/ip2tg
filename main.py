"""
Send local IP address and computer data to Telegram on machine reboot.
Uses `systemd service` to run at startup. See README.md.
"""

import getpass
import json
import logging
import requests
import socket

from dotenv import dotenv_values
from os.path import dirname, join, realpath


HOME = dirname(realpath(__file__))
CONFIG = dotenv_values(join(HOME, ".env"))

logging.basicConfig(
    filename=join(HOME, "log.txt"),
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_local_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to connect successfully
        # just triggers the right interface
        s.connect(("8.8.8.8", 80))
        return {
            "host name": socket.gethostname(),
            "user name": getpass.getuser(),
            "local ip": s.getsockname()[0],
        }

    finally:
        s.close()


def telegram_bot_sendtext(bot_message):
    bot_token = CONFIG["bot_token"]
    bot_chat_id = CONFIG["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token
                 + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)
    response = requests.get(send_text)
    return response.json()


def main():
    mes = json.dumps(get_local_data())
    resp = telegram_bot_sendtext(mes)
    logger.info(resp)


if __name__ == "__main__":
    main()
