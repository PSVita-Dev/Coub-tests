import requests
import random
import string
import uuid
import names
import os
import pyfiglet

from pystyle import Colors,Center #yea i used it back then lmfao
from threading import Thread,active_count
from requests_toolbelt import MultipartEncoder

global session
session = requests.Session()


def setup():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    fig = pyfiglet.Figlet(font='epic')
    banner = fig.renderText("Coub")
    print(Colors.purple+Center.XCenter(banner))
    print(Colors.pink+Center.XCenter("By azubisinmir"))

def randstr():
    s=""
    for i in range(0,20):
        s += random.choice(string.ascii_lowercase)
    return s

def gen_acc():
    ms = randstr()
    name = names.get_full_name()
    url = "https://coub.com/api/v2/sessions/signup"

    payload = {
        "id": 0,
        "session": {
            "birthday": "10/1/2022",
            "email": ms+"@gmail.com",
            "gender": "unspecified",
            "name": name,
            "password": "123456azubi",
            "uid": ms+"@gmail.com"
        }
    }
    headers = {
        "X-Auth-Token": "",
        "User-Agent": "CoubAndroid",
        "Content-Type": "application/json; charset=UTF-8"
    }

    response = session.request("POST", url, json=payload, headers=headers,proxies={"https":"http://"}) #put proxy
    token = response.json()["api_token"]
    chid = response.json()["user"]["current_channel"]["id"]
    print(Colors.green,"{Success} Genned Token: "+token)
    with open("tokens.txt","a") as f:
        f.write(token+"\n")
        f.close()
    return token,chid,name

def follow(token,chid,name):

    url = "https://coub.com/api/v2/follows"

    querystring = {"id":"15673580","channel_id":str(chid)}

    headers = {
        "X-Auth-Token": token,
        "User-Agent": "CoubAndroid"
    }
    response = session.request("POST", url, headers=headers, params=querystring,proxies={"https":"http://"}) #put proxy
    print(Colors.purple,"{Success} "+name+" just followed you!")
    
def view(link):
    
    k,lid = link.split("view/")
    url = "https://coub.com/coubs/"+lid+"/increment_views"

    querystring = {"type":"app","platform":"android"}

    headers = {
        "User-Agent": "CoubAndroid"
    }

    response = requests.request("POST", url, headers=headers, params=querystring,proxies={"https":"http:"}) #put proxy

    print(response.text)
    

def make_fol():
    try:
        tk,ch,n = gen_acc()
        follow(tk,ch,n)
    except:
        print(Colors.red,"{Fail} An error occurred")
        pass
    
setup()

while True:
    if(active_count() <= 100):
            #Thread(target=(view),args=("https://coub.com/view/38h95u",)).start()  #for views
        Thread(target=(make_fol),).start()
    
    
    
