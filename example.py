# main.py

from midjourney.Midjourney import MidjourneyClient
import time, random
from dotenv import load_dotenv
import os

load_dotenv()

message_id = "1129240328994570363"
token = os.getenv("TOKEN")
value = "Creative halo above the clouds --ar 1:2"  # value that will be sent to the modal popup
channel_id = os.getenv("CHANNEL_ID")

#listener function to process the modal popup, or other messages
def process_message(message):
    channel_id = message.get("channel_id")
    if channel_id == channel_id:
        if message.get("title") == "Remix Prompt":
            time.sleep(random.uniform(1, 1.5))
            client.interact_modal(message, value=value)
            print("modal: " + str(message))

client = MidjourneyClient(
        name="ModalTest",
        token = token,
        application_id = os.getenv("APPLICATION_ID"),
        guild_id = os.getenv("GUILD_ID"),
        channel_id = channel_id,
        message_handler=process_message,
    )

def main():
    client.run()
    time.sleep(3)
    client.interact(message_id=message_id, label="Vary (Strong)")

if __name__ == "__main__":
    main()