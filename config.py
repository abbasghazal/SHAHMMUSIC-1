from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","24868656"))
API_HASH = getenv("API_HASH","ccb43a2f3e973458d230a9c2983f8140")

BOT_TOKEN = getenv("BOT_TOKEN","8081591964:AAHSWe_2HsZ_CAPAPPCGQovHQqB5Yraoy7w")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",6848908141))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/d7f33299ed8c60ad82721.mp4")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Shahmplus")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shahmplus")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6848908141").split()))


FAILED = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
