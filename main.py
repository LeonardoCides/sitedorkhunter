from googlesearch import search
from scan import *
from banner import banner
from os import system
system('clear')
print(banner)
dork = input("Defina a Dork para pesquisar: ")
num_results = int(input("Quantidade de Sites: "))
def encontrar_site_com_dork(dork, num_results):
    try:
        print(f"Buscando sites com a dork: {dork}...")
        resultados = search(dork, num_results=num_results)
        for i, url in enumerate(resultados, 1):
            print(f'{i}. {url}')
            analisar()
    except Exception as e:
        print(f'ERRO')

encontrar_site_com_dork(dork, num_results)
