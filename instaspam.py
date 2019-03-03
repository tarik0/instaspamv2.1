# coding=utf-8
#!/usr/bin/env python3

""" 
Programı değiştirip bir yerde yayınlamadan önce lütfen
bu programın GPLv3 lisansı altında olduğunu unutmayınız.
Daha Fazla Bilgi:
https://tr.wikipedia.org/wiki/GNU_Genel_Kamu_Lisans%C4%B1
https://www.gnu.org/licenses/quick-guide-gplv3.html
"""

__author__ = "Hichigo TurkHackTeam"
__license__ = "GPLv3"
__version__ = "2.1.0"
__status__ = "Geliştiriliyor"



from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapılıyor!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapılıyor!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Kullanıcılar yükleniyor!")
    USERS = LoadUsers("./kullanicilar.txt")
    PrintStatus("Proxler yükleniyor!")
    PROXIES = LoadProxies("./proxyler.txt")
    print("")

    username = GetInput("Şikayet etmek istediğiniz hesap kullanıcı adı:")
    userid = GetInput("Şikayet etmek istediğiniz hesap numarası:")
    useproxy = GetInput("Proxy kullanmak ister misin? [Evet/Hayır]:")
    if (useproxy == "Evet"):
        useproxy = True
    elif (useproxy == "Hayır"):
        useproxy = False
    else:
        PrintFatalError("Lütfen sadece 'Evet' yada 'Hayır' girin!")
        exit(0)
    usemultithread = GetInput("Multithreading kullanmak ister misin? [Evet/Hayır] (Çok fazla kullanıcınız varsa veya bilgisayarınız yavaşsa bu özelliği kullanmayın!):")
    
    if (usemultithread == "Evet"):
        usemultithread = True
    elif (usemultithread == "Hayır"):
        usemultithread = False
    else:
        PrintFatalError("Lütfen sadece 'Evet' yada 'Hayır' girin!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Lütfen üstteki şikayet nedenlerinden birini seçin (örn: spam için 1):")

    
    
    
    print("")
    PrintStatus("Başlıyor!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
    

    
