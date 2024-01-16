import subprocess

def check_and_install(package):
    try:
        # Tenta importar a biblioteca
        __import__(package)
        print(f'{package} já está instalado.')
    except ImportError:
        # Se a biblioteca não estiver instalada, instala-a
        subprocess.check_call(['pip', 'install', package])
        print(f'{package} instalado com sucesso.')

# Lê as bibliotecas do arquivo requirements.txt
with open('requirements.txt') as f:
    required_packages = [line.strip() for line in f]

# Verifica e instala as bibliotecas
for package in required_packages:
    check_and_install(package)
