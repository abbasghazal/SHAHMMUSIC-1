from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",24868656))
API_HASH = getenv("API_HASH","ccb43a2f3e973458d230a9c2983f8140")

BOT_TOKEN = getenv("BOT_TOKEN", "8081591964:AAHSWe_2HsZ_CAPAPPCGQovHQqB5Yraoy7w")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",6848908141))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/d7f33299ed8c60ad82721.mp4")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")

SESSION = getenv("SESSION","AgCnJPQAsJ4808wqFjMSpMQ7yftRKgi27J3M-CfU3Lgy8dytdE_xANih7ALzKRrmTi9_ZglkLexxI9l5ABiT9r-SNP5O8wToQ7orXahI4Rf6SEEAwSd_CIQg08bdXUl2-VgLJ-nh2Sol3MsNyGBFEFlh_DyCtH_bYePhyZMp5gsUgmZINW9lxXomTUc4dWFGoDLJtUi-iQOIPMFbChbvXCvpOg5x3QSHCN0FRk3qQodtyrpMMd-izMhTq63OVSb_vId7hOBSFcapK3F1-6TQ2nIR3v-OLg3UhhmYPUDkMS0zGif9oFpiGHna4CVaNn9RQxzMgj-Ywit0oKJdFSNUH_J1P51GhQAAAAHSXzHZAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Shahmplus")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Shahmplus")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6848908141").split()))


FAILED = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
