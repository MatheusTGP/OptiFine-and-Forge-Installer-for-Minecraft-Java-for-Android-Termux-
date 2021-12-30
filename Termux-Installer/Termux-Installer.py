from os import system as Shell
from os import mkdir as CreateDiretory
from shutil import rmtree as remove
from time import sleep
try:
	from wget import download as Get
except ModuleNotFoundError:
	Shell('pip install wget')

# Termux Installer For Android
# Colors for Terminal (Theme)

R = '\033[01;31m'
G = '\033[01;32m'
Y = '\033[01;33m'
B = '\033[01;34m'
M = '\033[01;35m'
C = '\033[01;36m'
W = '\033[01;37m'

def Termux_Installer ():
	Choice = input("\033[01;35mDeseja Baixar o Apk do Termux [y/n]: \033[01;33m")
	if Choice == "y":
		print(W,"Pesquisando Site de Download...")
		
		sleep(2)

		URL_Get = 'https://cdn.down-apk.com/com.termux/Termux_0.117_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExNy8xMTcuNDkxZjIwN2UyODlhYzA1YmNiMzljYTQzNmI1MjE4ZjZhZTgwMWRiZC5hcGs=&iat=1640837450&sig=207f6223508fa8e1ac1cfb4957c9ded1&size=85749239&from=cf&version=latest'
		
		try:
			CreateDiretory('/sdcard/Termux-Apk')
		except FileExistsError:
			remove('/sdcard/Termux-Apk')
			CreateDirectory('/sdcard/Termux-Apk')
		Local = '/sdcard/Termux-Apk/'
		
		sleep(1)
	
		print(G,"\nIniciando Download do APK...",W)
	
		Get(URL_Get, Local)
	
		print(f"\nAPK do Termux Baixado com sucesso, vá até: {Local}")
	else:
		print(R,"Instalaçao Cancelada.",W)

Termux_Installer()
