from pyrogram import Client
from jobs.sheduler import scheduler

# Bot init
app = Client("MyAcoount")

# App launch
if __name__ == "__main__":
    # scheduler.start()
    app.run()
