#インポート
from tkinter import messagebox
import requests, json
import sys
import tkinter
import tkinter.ttk as ttk

#swichbotの必要な情報を変数に代入
ACCESS_TOKEN="544860c7b931d82d6aa99588f1da4add965865c529086c6492d501fa4362458d1604f7f03e4a510f9230c840d2025152"
API_BASE_URL="https://api.switch-bot.com"

#Tikinterの基本設定
root = tkinter.Tk()
root.title(u"家電コントロール")
root.geometry("400x200")
root.resizable(0,0)

#ファンクションプログラム
def plug_ON(event):
    DEVICEID="A848FAE3F045"
    headers = {
        # ヘッダー
        'Content-Type': 'application/json; charset: utf8',
        'Authorization': ACCESS_TOKEN
    }
    url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
    body = {
        # 操作内容
        "command":"turnOn",
        "parameter":"default",
        "commandType":"command"
    }
    ddd = json.dumps(body)
    res = requests.post(url, data=ddd, headers=headers)
    messagebox.showinfo('家電コントロール', 'オンにしました')

def plug_OFF(event):
    DEVICEID="A848FAE3F045"
    headers = {
        # ヘッダー
        'Content-Type': 'application/json; charset: utf8',
        'Authorization': ACCESS_TOKEN
    }
    url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
    body = {
        # 操作内容
        "command":"turnOff",
        "parameter":"default",
        "commandType":"command"
    }
    ddd = json.dumps(body)
    res = requests.post(url, data=ddd, headers=headers)
    messagebox.showinfo('家電コントロール', 'オフにしました')

def light_UP(event):
    DEVICEID ="01-202206120849-55417342"
    headers = {
        # ヘッダー
        'Content-Type': 'application/json; charset: utf8',
        'Authorization': ACCESS_TOKEN
    }
    url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
    body = {
        # 操作内容
        "command":"brightnessUp",
        "parameter":"default",
        "commandType":"command"
    }
    ddd = json.dumps(body)
    res = requests.post(url, data=ddd, headers=headers)
    messagebox.showinfo('家電コントロール', '明るくしました')

def light_DOWN(event):
    DEVICEID ="01-202206120849-55417342"
    headers = {
        # ヘッダー
        'Content-Type': 'application/json; charset: utf8',
        'Authorization': ACCESS_TOKEN
    }
    url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
    body = {
        # 操作内容
        "command":"brightnessDown",
        "parameter":"default",
        "commandType":"command"
    }
    ddd = json.dumps(body)
    res = requests.post(url, data=ddd, headers=headers)
    messagebox.showinfo('家電コントロール', '暗くしました')


#UI
Static1 = tkinter.Label(text=u'プラグの電源')
Static1.pack()

Button1 = tkinter.Button(text=u'オン',width=50)
Button1.bind("<Button-1>",plug_ON) 
Button1.pack()

Button2 = tkinter.Button(text=u'オフ',width=50)
Button2.bind("<Button-1>",plug_OFF) 
Button2.pack()

border1=ttk.Separator(root,orient="horizontal")
border1.pack(fill="both",pady=20)

Static2 = tkinter.Label(text=u'ライトの明るさ調節')
Static2.pack()

Button3 = tkinter.Button(text=u'明るくする',width=50)
Button3.bind("<Button-1>",light_UP) 
Button3.pack()

Button4 = tkinter.Button(text=u'暗くする',width=50)
Button4.bind("<Button-1>",light_DOWN) 
Button4.pack()

border2=ttk.Separator(root,orient="horizontal")
border2.pack(fill="both",pady=20)

root.mainloop()