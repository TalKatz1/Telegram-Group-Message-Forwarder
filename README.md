# Telegram Group Message Forwarder

This script allows you to forward messages from selected Telegram groups to other group. It uses the Telethon library for interacting with the Telegram API.

Prerequisites:

- Python 3.x
- Telethon library (pip install telethon)

Configuration:

Before running the script, make sure to edit the config.ini file with the required information:

```
[TELEGRAM]
API_ID = <YOUR_TELEGRAM_API_ID>
API_HASH = <YOUR_TELEGRAM_API_HASH>
PHONE_NUMBER = <YOUR_TELEGRAM_USER_PHONE NUMBER> (looks like +12124567890)
```

Replace the values with your own Telegram API credentials and phone number.

Usage:

1. Run the script using Python: python copy_messages.py
2. The script will read the config.ini file and connect to Telegram using the provided API credentials.
3. You will be prompted to choose the groups to follow and groups to send messages to.
4. The script will start listening to the selected groups and forward any new messages to the specified send groups.
5. Press Ctrl+C to stop the script and exit.

Or just download the copy_messages.exe executable file, place it on the same folder with the config.ini file and open it.

Note: Ensure that the phone number associated with the Telegram API credentials has access to the groups you want to follow and send messages to.
