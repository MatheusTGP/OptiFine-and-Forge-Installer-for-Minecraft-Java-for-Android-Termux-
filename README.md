# ⚠️ | OptiFine e Forge Installer para Minecraft Java no Android [Termux-GUI]
**Você já pensou em Instalar o OptiFine pelo próprio celular?** Você pode agora instalar este script para que o próprio programa executa o Java 17 juntamente com o OptFine ou Forge que você desejar pelo Android! Lembre-se, você também poderá executar um Minecraft-Launcher para gerenciar as Versões, você pode utilizar os lançadores MCinaBox ou PojavLaucher.

# 📱 | Como funciona o Script?
**Função**: O script fará o trabalho automaticamente para o usuário, ele
Irá configurar o a GUI (VNC) juntamente com o Gerenciador de Arquivos [Thunar],
E o instalador Java [OpenJDK17], ele você poderá escolher o arquivo que deseja executar com o Java
Fazendo com que o Java abra a janela Main do OptFine ou Forge, logo depois você poderá inserir onde o OptiFine
Será instalado, por exemplo: MCinaBox/gamedir/ **'aqui'**, ou.., games/PojavLaucher/.minecraft/ **'aqui'**, ele necessitará que você
Tenha a versão do OptFine ou Forge já instalada, nesse script você poderá executar o Minecraft-Launcher juntamente para se necessitar
Instalar alguma versão do Minecraft.

# 📥 | Instalação
**Tutorial**: Primeiramente, você deve executar o código em Python - Termux-Installer,
Ele fará a instalação do APK do Termux mais Atualizado (Não use o Termux da PlayStore está desatualizado),
Executando o Termux Installer ele coletara o APK e enviará para o diretório; **/sdcard/Termux-Apk/Termux.apk**,
Agora que você fez a instalação do Termux, você precisará instalar o script **"Builds.sh"**, ele fará a instalação completa!
Más antes lembre-se de instalar o VNC Viewer, pressione aqui para Instalar › [VNCViewer](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android&hl=pt&gl=US)
Após isso, vocês pode iniciar o script, para isso, no terminal do Termux você deve passar somente o comando abaixo, caso você deseja cancelar a instalação aperte CTRL + C ou Z

    cd $HOME && pkg install git && sleep 1 && git clone https://github.com/MatheusTGamerPro/OptiFine-and-Forge-Installer-for-Minecraft-Java-for-Android-Termux- && mv OptiFine-and-Forge-Installer-for-Minecraft-Java-for-Android-Termux- Repository && cd Repository && cp xstartup $HOME && cp Builds.sh $HOME && cd $HOME && chmod u+rwx xstartup && cd $HOME && sleep 3 && bash Builds.sh


Após executar esse comando, automaticamente o script atualiza e instala o Java e outros Pacotes para o usuário,
Depois disso precisamos configurar o servidor VNC, para isso.. após fazer a instalação completa, abra o VNC Viewer,
Pressione no botão "+" e na entrada de "Adress" ou "Endereço" adicione: ```localhost:1```, esse IP é o endereço onde você visualizará
A janela do Gerenciador de arquivos, más antes você não deve já iniciar, salve junto com o Endereço e o nome do Computer, após isso volte ao Termux
E inicie com o comando:

    vncserver -geometry 1280x720

Este comando iniciara o servidor no "localhost:1" igual colocamos no VNC,
Após isso irá aparecer a mensagem que o servidor está aberto na porta :1, caso você queira parar o servidor
Passe o seguinte comando no Termux:

    vncserver -kill :1

Por Favor, sempre feche o servidor ao parar de utilizar o script, qualquer erro na execução,
Me informe no Issues!

# ❗ | Como Utilizar o Script
Primeiramente, faça o procedimento de instalação, logo depois que estivermos dentro da interface, automaticamente será aberto
Uma janela que é o Famoso Gerenciador de arquivos "Thunar", ele você poderá ver as pastas que contém no SDcard, más antes você deve permitir
Acesso ao armazenamento para o Termux (faça isso nas informações do aplicativo), agora que temos o Gerenciador, precisamos procurar o diretório "sdcard"
E irmos até a pasta onde está localizado o nosso arquivo '.jar' OptiFine, Forge, Launcher.. após encontrarmos o arquivo, você não poderá dar dois toques e iniciar
O OptFine ou algo do tipo, antes devemos fazer o seguinte passo, pressione com o botão direito no Arquivo (no VNC Viewer pressione a tela com os dois dedos), logo depois
Selecione para abrir o Arquivo em 'Other Application', irá abrir uma aba de seleção de aplicativos disponíveis, más, você irá em "Comando Personalizado", onde iremos passar
O parâmetro (comando) necessário para executar o 'jar', ao pressionar digite o seguinte comando: ```java -jar```, após isso pressione para abrir com esse comando,
Fazendo isso, automaticamente abrirá uma janela do Java, ou melhor, do instalador do OptiFine, Forge, ou Launcher após isso você poderá selecionar onde instalará o OptiFine
E fazer a instalação. Para executar um Launcher e rodar o Minecraft Java (difícil) necessitara de instalar uma versão do OpenGL, más isso trago mais pra frente.

**Nota**: Você não precisará mais fazer este procedimento, qualquer programa em 'jar' iniciará automaticamente com o Java!😆

