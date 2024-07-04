import telebot, conf, os
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from pytube import YouTube
from funcs import download_video, download_audio

#elif message.text == ("360p"):
# try:
#   download_video_360(message, url, bot_msg_res)
# except:
# bot.send_message(message.from_user.id, "Неизвестная ошибка, попробуйте позже")

#The on_progress_callback function will run whenever a chunk is downloaded from a video

bot = AsyncTeleBot(conf.TOKEN)
@bot.message_handler(commands = ['start'])
async def get_message(message):
        await bot.send_message(message.from_user.id, "Пришлите ссылку на Youtube видео, которое хотите скачать")

@bot.message_handler(content_types = ["text"])
async def get_message_youtube(message):
    if message.text.startswith("https://www.youtube.com/"):
        global url, bot_msg_res, msg_url
        url = message.text
        msg_url = message
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="360p")
        btn2 = types.KeyboardButton(text="480p")
        btn3 = types.KeyboardButton(text="720p")
        btn4 = types.KeyboardButton(text="1080p")
        btn5 = types.KeyboardButton(text="Аудио")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot_msg_res = await bot.send_message(message.from_user.id, "Выберите качество видео", reply_markup=markup)
        # bot.delete_message(chat_id=message.from_user.id, message_id=message.id)
    elif message.text == ("360p"):
        await download_video(message, "360p", url, bot_msg_res, msg_url)
    elif message.text == ("480p"):
        await download_video(message, "480p", url, bot_msg_res, msg_url)
    elif message.text == ("720p"):
        await download_video(message, "720p", url, bot_msg_res, msg_url)
    elif message.text == ("1080p"):
        await download_video(message, "1080p", url, bot_msg_res, msg_url)
    elif message.text == ("Аудио"):
        await download_audio(message, url, bot_msg_res, msg_url)
    else:
        await bot.send_message(message.from_user.id, "Неверная ссылка или видео невозможно скачать")

bot.polling(none_stop= True)