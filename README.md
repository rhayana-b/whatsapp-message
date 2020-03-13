# Instalação

```
sudo apt-get install python3

sudo apt install python3-pip

sudo pip3 install selenium
```

entrar em [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases) e fazer download da versão 32 ou 64 pra Linux

Navegue até a pasta onde realizou o download do arquivo e descompacte-o com o seguinte comando:

```
sudo tar -xvf geckodriver 
```

apertar o tab pra completar o nome do arquivo

Agora precisamos apenas movê-lo para a pasta `/usr/local/bin` e para isso vamos executar o comando:

```
sudo mv geckodriver /usr/local/bin/
```
