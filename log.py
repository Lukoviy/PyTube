import datetime

def log_entry(message,url,yt,stream):
    current_time = datetime.datetime.now().time()
    log = open("log.txt", "a")
    log.write(f"\n{current_time} \n" 
              f"username - {message.from_user.username}({message.from_user.id}) \n"
              f"url - {url} | title - {yt.title} \n"
              f"stream - {stream}\n")
    log.close()