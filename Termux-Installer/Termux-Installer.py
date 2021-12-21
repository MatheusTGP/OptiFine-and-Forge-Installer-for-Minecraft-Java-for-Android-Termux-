from os import system as Shell
from os import mkdir as CreateDiretory
from shutil import rmtree as remove
from time import sleep
try:
	from wget import download as Get
except ModuleNotFoundError:
	Shell('pip install wget')

# Termux Installer For Android

def Termux_Installer ():
	Choice = input("\033[01;35mDeseja Baixar o Apk do Termux [y/n]: \033[01;33m")
	if Choice == "y":
		print("\033[01;38mPesquisando Site de Download...")
		
		sleep(2)

		URL_Get = 'https://cdn.down-apk.com/com.termux/Termux_0.117_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExNy8xMTcuNDkxZjIwN2UyODlhYzA1YmNiMzljYTQzNmI1MjE4ZjZhZTgwMWRiZC5hcGs=&iat=1640053074&sig=a5441081fd3e6ccf05dfa039e852f177&size=85749239&from=cf&version=latest'
		
		try:
			CreateDiretory('/sdcard/Termux-Apk')
		except FileExistsError:
			remove('/sdcard/Termux-Apk')
			CreateDirectory('/sdcard/Termux-Apk')
		Local = '/sdcard/Termux-Apk/'
		
		sleep(1)
	
		print("\n \033[01;32mIniciando Download do APK...")
	
		Get(URL_Get, Local)
	
		print(f"\nAPK do Termux Baixado com sucesso, vá até: {Local}")
	else:
		print("\033[01;31mInstalaçao Cancelada.")

Termux_Installer()
