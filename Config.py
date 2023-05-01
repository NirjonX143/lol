import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6170365487:AAEIgj0O4wl54DNmzugwOnSE4Jsi0NSioQ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIQBuxziwFNkZ6fFSwqC_zRB-StToJSfptzMSK2s_DrcGKHhjww4CMad1Hgg-PhJKMPYH_EJNq90dtdFwmZka-ghQoQmWM3UD8eDGaTdGKAMku9NiG9dvzq_92lQjf4xK5fJRomRI4DRrl1mftudgchLWWeMBBeAfr9Txljr0B5_w0LEIPwLb5X1zpKYCy0OHrWnMGRmluUwxZXCnH02jLwrcLCBoeCqvfK8yO6ssW8ywZZ3Qj469v_sE7hUuLMWjUKPD8jSdRyjYdUsq1lAUQ9GVu_7zEBHY3ndaRuONDZCYG2qla5IURpkWrnzYwr2Xo4GSDKavNeaAmKOJ7w1EywH26k=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "eSportMuSicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheBothub") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "BlackWorldMF") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1975589590")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
