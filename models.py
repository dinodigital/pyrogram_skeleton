from peewee import SqliteDatabase, Model, CharField, IntegerField, DateTimeField

from datetime import datetime


db = SqliteDatabase('users.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    tg_id = IntegerField()
    username = CharField()
    registered = DateTimeField(default=datetime.now)


# Создание таблиц
db.create_tables([User, ])
