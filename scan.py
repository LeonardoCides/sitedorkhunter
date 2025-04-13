from main import dork
def analisar():
    if dork in "id=" or dork in ".php=":
        print("esses sites possivelmente tem falha de SQLI")