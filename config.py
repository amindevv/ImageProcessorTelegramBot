
# Telegram Bot Token
TOKEN = "1086787905:AAH69hya-fhtn9z0BBCcnLyKiTUUo8z0JBQ"

# Ngrok server urls, must be in HTTPS
NGROK_URL = "https://c4adc940.ngrok.io"   

# Base URL for REST
BASE_TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

# Base URL to retrieve file
BASE_TELEGRAM_FILE_URL = f"https://api.telegram.org/file/bot{TOKEN}"

# Webhook address
LOCAL_WEBHOOK_ENDPOINT = f"{NGROK_URL}/webhook"  

TELEGRAM_INIT_WEBHOOK_URL = BASE_TELEGRAM_URL + f"/setWebhook?url={LOCAL_WEBHOOK_ENDPOINT}"
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + "/sendMessage?chat_id={}&text={}"
TELEGRAM_GET_FILE_PATH_URL = BASE_TELEGRAM_URL + "/getFile?file_id={}"

# Just add the file path to the parameter
TELEGRAM_GET_FILE_URL = BASE_TELEGRAM_FILE_URL + "/{}"

# Path to save the receiving images
FILE_SAVE_PATH = "unprocessed_images/"

# A place to save the Output when it's finished
PROCESSED_OUTPUT_PATH = "processed_images/"

# Frame which is drawn on top of the Image
FRAME_PATH = "frames/base.png"

# You can improve this by inserting user's name as parameter
MESSAGE_WELCOME_STARTED = "Hey there! welcome. Send me a photo of your choice!"
MESSAGE_PHOTO_EDITED = "Thanks for using our bot, Here is your photo!"
