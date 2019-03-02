from requests import Session

def CheckPublicIP():
    try:
        with Session() as ses:
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                return res.json()["ip"]
            return None
    except:
        return None
    pass
    
def IsProxyWorking(proxy):
    try:
        with Session() as ses:
            ses.proxies.update(proxy)
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                if(res.json()["ip"] != CheckPublicIP() and CheckPublicIP != None):
                    return True
            return False
    except:
        return False
    pass

def PrintSuccess(message, username, *argv):
    print("[ OK ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

# Spam 1
# Kendine Zarar verme 2
# Uyuşturucu 3
# Çıplaklık 4
# Şiddet 5
# Nefret Söylemi 6
# Taciz ve Zorbalık 7
# Kimlik Taklidi 8
# Yaşı Tutmayan Çocuk 11

def PrintChoices():
    print("""    
    +----------------------+--------+
    |        Sebep         | Numara |
    +----------------------+--------+
    | Spam                 |      1 |
    | Kendine Zarar Verme  |      2 |
    | Uyuşturucu           |      3 |
    | Çıplaklık            |      4 |
    | Şiddet               |      5 |
    | Nefret Söylemi       |      6 |
    | Taciz ve Zorbalık    |      7 |
    | Kimlik Taklidi       |      8 |
    | Yaşı Tutmayan Çocuk  |     11 |
    +----------------------+--------+
    """)

def GetInput(message, *argv):
    print("[ ? ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    return input()

def PrintFatalError(message, *argv):
    print("[ X ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintError(message, username, *argv):
    print("[ X ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintStatus(message, *argv):
    print("[ * ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintBanner():
    banner = """
        _.._
      .' .-'`
     /  /         THT Instagram Spam Script'i
     |  |         ---------------------------
     \  '.___.;      Yapımcı: Hichigo THT
      '._  _.'
         ``
    """
    print(banner)
    pass

def LoadUsers(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                user = line.split(" ")[0]
                password = line.split(" ")[1]
                ret.append({
                    "user": user,
                    "password": password
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'kullanicilar.txt' Dosyası bulunamadı!")
        exit(0)
    pass

def LoadProxies(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                ip = line.split(":")[0]
                port = line.split(":")[1]
                ret.append({
                    "ip": ip,
                    "port": port
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'proxyler.txt' Dosyası bulunamadı!")
        exit(0)
    pass