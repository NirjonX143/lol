import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6202456169:AAHdtXNPrsTACnd7u4fw_YqX6cWf60H9UYY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMgBu3BQEWbiQCgVQPKMiTrL9iw499siUO4yQcBBC1nwkRfBTn0nk-8Iy3dKZr_u3M3Xn_OMrWZOKmhU9YDL1VzQ8P8eBJsw0dEi6uBI03o4JL0SRxrpld-ES8BmIPxpTVtPbMPJ-pLNHLE9S3WTW03Hp68-shYGBoE9JXxCJZ0uW5CI8IgoCRNaUaiCTBI4fdzBU5hOG3vRV4RkJtfM1wLrYubRQGheUgb6jWgOvIvbVNNtX4F7ZQsvPdNg8KrsrwkKL7YMDWj4Y9Bgl5b4yRURKi2yYoZKtEZKx12v5EO5mvFg-_-y8Xvd7B1GqU2TtsoYvgL0VSJSQPw1BZ2MYQF1ofQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DeadMusicXBot")
    SUPPORT = os.environ.get("SUPPORT", "TheBothub") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "BlackWorldMF") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5018475590")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
