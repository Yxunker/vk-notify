import vk_api
import time
from token2 import token_vk
from win10toast import ToastNotifier

session = vk_api.VkApi(token=token_vk)

def show_notify(title, text):
    toast = ToastNotifier()
    toast.show_toast(title, text, duration=5)

def get_name(user_id):
    global user_name 
    user_name = session.method("users.get", {"user_id": user_id})
    user_name = (str(user_name[0]["first_name"]) + " " + str(user_name[0]["last_name"]))

def Online(user_id):
    get_name(user_id)
    while True:
        user_online = session.method("messages.getLastActivity", {"user_id": user_id})
        if user_online["online"] == 1:
            show_notify(user_name, "В сети.")
            while user_online["online"] != 0:
                time.sleep(3)
                print(1)
                user_online = session.method("messages.getLastActivity", {"user_id": user_id})
        else:
            show_notify(user_name, "Не в сети.")
            while user_online["online"] == 0:
                            time.sleep(3)
                            print(0)
                            user_online = session.method("messages.getLastActivity", {"user_id": user_id})
        
Online(318305315)

