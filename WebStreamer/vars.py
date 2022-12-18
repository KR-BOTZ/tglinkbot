# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv("API_ID", "22161709"))
    API_HASH = str(getenv("API_HASH", "c1292ced60651fe3670854e31c7d2785"))
    BOT_TOKEN = str(getenv("BOT_TOKEN", "5884742619:AAGti_x1h4H4xMiWAytCLl-Dnlq8N3ceSL4"))
    SESSION_NAME = str(getenv('SESSION_NAME', 'gdchekobot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv("BIN_CHANNEL", "-1001584785114"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'filesavejust.osc-fr1.scalingo.io'))
    OWNER_ID = int(getenv('OWNER_ID', '2062513342'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    environ["FQDN"] = "filesavejust.osc-fr1.scalingo.io"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "https://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://manju:1234@cluster0.s6qpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001584785114")).split()))
