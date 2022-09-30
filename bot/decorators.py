from aiogram.types import Message
from asgiref.sync import sync_to_async

import config
from backend.models import BotUser, Template, Template2Button, Group


def print_msg(func, text):
    print(f'from modul decorators({func}) -> ', text)



@sync_to_async
def add_user(message: Message) -> None:
    chat_id = message.from_user.id
    user, success = BotUser.objects.get_or_create(chat_id=chat_id)
    if success:
        full_name = ' '.join([message.from_user.first_name, message.from_user.last_name or ''])
        user.full_name = full_name
        try:
            user.username = message.from_user.username
        except Exception:
            pass
        user.save()

@sync_to_async
def is_bot(message: Message) -> bool:
    return message.from_user.is_bot

@sync_to_async
def exists(chat_id) -> bool: 
    user = BotUser.objects.filter(chat_id=chat_id).exists()
    return user

@sync_to_async
def get_text(title, chat_id, button=False):
    if button:
        text = Template2Button.objects.get(title=title)
    else:
        text = Template.objects.get(title=title)
    lang = BotUser.objects.get(chat_id=chat_id).language
    if lang == 'ru':
        return text.body_ru
    return text.body_eng

@sync_to_async
def get_user_lang(chat_id):
    user = BotUser.objects.get(chat_id=chat_id)
    return user.language

@sync_to_async
def set_user_language(chat_id, lang):
    user = BotUser.objects.get(chat_id=chat_id)
    user.language = lang
    user.save()

@sync_to_async
def create_group(title, username, link, description, members_count, chat_id, chanel_chat_id, type):
    user = BotUser.objects.get(chat_id=chat_id)
    group = Group.objects.create(
        chat_id=chanel_chat_id,
        title=title,
        username=username,
        link=link,
        description=description,
        users_count=members_count,
        black_list='-',
        white_list='-',
        user=user,
        type=type
    )
    return group