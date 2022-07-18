#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request
import urllib
import urllib.error
try: 
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site nao esta acessivel no momento')
else:
    print('O site esta acessivel no momento!')