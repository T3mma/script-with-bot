import os
import requests

# Lista de módulos a descargar
mdls = [
    "addhost", "delhost", "alterarsenha", "criarusuario", "expcleaner", "mudardata",
    "remover", "criarteste", "verifbot", "droplimiter", "alterarlimite", "ajuda",
    "sshmonitor", "badvpn", "userbackup", "instsqd", "blockt", "otimizar", "menu",
    "speedtest", "banner", "senharoot", "reiniciarservicos", "reiniciarsistema",
    "attscript", "conexao", "delscript", "detalhes", "botssh", "infousers", "verifatt",
    "limiter", "uexpired", "cabecalho", "bot", "open.py", "proxy.py", "wsproxy.py",
    "trojan-go", "onlineapp", "swapmemory"
]

# Directorio donde se guardarán los archivos
dir1 = "C:/Users/Tiago/Desktop/ScriptConBot/modulos"

# URL base
base_url = "https://raw.githubusercontent.com/vpsvip7/SSHPLUS/main/Modulos/"

# Descarga de los archivos
for arq in mdls:
    file_path = os.path.join(dir1, arq)
    
    # Si el archivo existe, lo eliminamos
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Descargar el archivo
    url = f"{base_url}{arq}"
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        # Hacer ejecutable el archivo (en Windows, esto no aplica, pero se deja como comentario)
        # os.chmod(file_path, 0o755)
        print(f"Descargado: {arq}")
    else:
        print(f"Error al descargar: {arq}")

print("Proceso de descarga finalizado.")
