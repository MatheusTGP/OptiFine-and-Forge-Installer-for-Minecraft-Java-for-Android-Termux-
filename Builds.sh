# Script Produced by: MatheusTGamerPro
# Shell: Bash (Termux)
# Thank you to everyone who uses it!
# GitHub: https://github.com/MatheusTGamerPro

 clear

 sleep 3

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;32mOptiFine & Forge Installer with Java"
 echo -e "\033[01;33m ==================="

 sleep 1

 echo -e "\033[01;33m Produced by: MatheusTGamerPro"
 echo -e "\033[01;33m Script Version: v1.0.0 [Beta]"
 echo -e "\033[01;33m Read the Wiki to find out how the Script works through my GitHub Site!\033[00;00m"

 sleep 2

 clear

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Starting Setup, Updating Packages..."
 echo -e "\033[01;33m ====================\033[00;00m"

 sleep 1

 apt update && apt upgrade

 sleep 1

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Updating X11 Repository..."
 echo -e "\033[01;33m ====================\033[00;00m"

 sleep 1

 pkg install -y x11-repo

 sleep 2

 clear

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Downloading TigerVNC..."
 echo -e "\033[01;33m ====================\033[00;00m"

 sleep 1

 pkg install -y tigervnc

 sleep 1

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Downloading Thunar Manager..."
 echo -e "\033[01;33m ====================\033[00;00m"

 sleep 1

 pkg install -y thunar

 sleep 2

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Downloading OpenJDK 17"
 echo -e "\033[01;33m ====================\033[00;00m"

 sleep 1

 pkg install -y openjdk-17

 sleep 3

 clear

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Installation Complete!"
 echo -e "\033[01;33m ==================="

 sleep 1

 echo -e "\033[01;32m Collecting Configuration File..."

 sleep 1

 cd ~/.vnc

 rm xstartup

 cd $HOME

 sleep 1

 mv xstartup ~/.vnc

 sleep 2

 clear

 echo -e "\033[01;33m ==================="
 echo -e "\033[01;36m Installation Completed Successfully!"
 echo -e "\033[01;33m ==================="

 echo -e "\033[01;32m [*] Clearing Cache...\033[00;00m"

 clear-cache pkg

 sleep 3

 clear

 echo -e "\033[01;38m To start the Server use the command: \033[01;33mvncserver\033[00;00m"

 echo -e "\033[01;38m To Stop Server execution use: \033[01;31mvncserver -kill :1\033[00;00m"

 echo -e "\033[01;36m Enjoy!"
