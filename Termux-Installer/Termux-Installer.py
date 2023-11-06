from os import system as console
from time import sleep as wait
try:
	from wget import download
except ModuleNotFoundError:
	print("Tentando instalar wget.")
	console('pip install wget')

# Função principal
def install_termux ():
	termux_version = get_termux_version()
	if input("Iniciar download? [y/n]: ") == "y" or "Y":
		save_folder = "/storage/emulated/0/Download/"
		repository = f"https://f-droid.org/repo/com.termux_{termux_version}.apk"
		
		try:
			print(f"\nBaixando Termux v{termux_version}")
			download(repository, save_folder)
		except KeyboardInterruptException:
			print("Download interrompido.")
		
		wait(1)
		print(f"\nDownload concluido, salvo em '{save_folder}'")
	else:
		print("Download cancelado")
	
# Liste e colete versões disponiveis do Termux
def get_termux_version():
	versions = ["118", "117", "116"]
	count = 0
	print("Selecione qual versão deseja baixar.\n")
	for version in versions:
		count += 1
		if (version == "118"):
			print(f"({count}) Termux v{version} [Recomendado]")
		else:
			print(f"({count}) Termux v{version}")
	
	option = int(input("\nopção: "))
	if (option in versions):
		return versions[option]
	else:
		return versions[0] # Pegue a versão mais recente
		
install_termux()
