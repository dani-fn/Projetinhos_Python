import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31m O site do pudim não está acessível no momento. \033[m')
else:
    print('\033[32m Consegui acessar o site do pudim com sucesso! \033[m')
    print(site.read())
