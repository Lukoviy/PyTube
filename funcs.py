import telebot, conf, os, log
from telebot import types
from pytube import YouTube
bot = telebot.TeleBot(conf.TOKEN)

def download_video(message,res,url,bot_msg_res,msg_url):
    yt = YouTube(url)
    stream = yt.streams.filter(res=res).desc().first()
    # log.log_entry(message,url,yt,stream)
    try:
        bot_msg = bot.send_message(message.from_user.id, "Скачиваю видео, ожидайте ⏳")
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg_res.message_id)
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=message.id)
        stream.download(f"{message.from_user.id}", filename=f"{message.id}.mp4")
        path = f"D:/Python/telegabot/{message.from_user.id}/{message.id}.mp4"
        video_o = open(path, "rb")
        bot.send_video(message.from_user.id, video_o, supports_streaming=True, reply_to_message_id=msg_url.id)
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, f"Ваше видео в качестве {res} ↑")
    except AttributeError:
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, "Данное качество не доступно")
    except:
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, "Файл весит слишком много, выберите качество меньше")
def download_audio(message,url,bot_msg_res,msg_url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).desc().first()
    log.log_entry(message, url, yt, stream)
    try:
        bot_msg = bot.send_message(message.from_user.id, "Скачиваю аудио, ожидайте ⏳")
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg_res.message_id)
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=message.id)
        stream.download(f"{message.from_user.id}", filename=f"{message.id}.mp3")
        path = f"D:/Python/telegabot/{message.from_user.id}/{message.id}.mp3"
        audio_o = open(path, "rb")
        bot.send_audio(message.from_user.id, audio_o, reply_to_message_id=msg_url.id)
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, "Ваше аудио ↑")
    except AttributeError:
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, "Данное качество не доступно")
    except:
        bot.delete_message(chat_id=bot_msg.chat.id, message_id=bot_msg.message_id)
        bot.send_message(message.from_user.id, "Файл весит слишком много, выберите качество меньше")