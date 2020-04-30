from pyrogram import Client, Filters, Message

from models import User


@Client.on_message(Filters.command("start"))
def start(bot: Client, message: Message):
    tg_id = message.from_user.id
    u, is_created = User.get_or_create(
        tg_id=tg_id,
        defaults={
            'username': message.from_user.username
        })

    print(message.text)

    msg = 'Hi, new user.' if is_created else 'Hi, old user.'
    bot.send_message(tg_id, msg)
