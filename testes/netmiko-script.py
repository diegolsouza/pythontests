#!/usr/bin/env python
#from __future__ import absolute_import, division, print_function
from getpass import getpass
from sys import exit, argv
import paramiko
import netmiko
import json

if len(argv) < 3:
    print("Faltam argumentos.\nUtilizar: cmdrunner.py <arquivo TXT com comandos> <arquivo JSON com devices>")
    exit()

# Abre o arquivo contendo os comandos
with open(argv[1]) as cmd_file:
    commands = cmd_file.readlines()

# Abre o arquivo contendo os IPs dos devices
with open(argv[2]) as dev_file:
    devices = json.load(dev_file)

# Função para pedir senha
def get_password():
    password = None
    while not password:
        password = getpass(prompt="Senha: ")
        password_verify = getpass(prompt="Digite a senha novamente: ")
        if password != password_verify:
            print("Senha não confere. Tente novamente.")
            password = None
    return password

# Requisição de credenciais
username = input("Usuário: ")
password = get_password()

# Tratamento de erros
#netmiko_exceptions = (netmiko.ssh_exception.netmikoTimeoutException,
#                        netmiko.ssh_exception.netmikoAuthenticationException)

# Abre conexão e executa os comandos, depois fecha conexão
for device in devices:
    device['username'] = username
    device['password'] = password
    device['device_type'] = "cisco_ios"
    try:
        print("-"*79)
        print("Conectando no", device['ip'],"\n")
        connection = netmiko.ConnectHandler(**device)
        for command in commands:
            # Executa os comandos cisco_ios
            print(connection.send_command(command))
        # Fecha a conexão e aguarda input pra fechar programa
        connection.disconnect()

    # Tratamento de erros
    except netmiko_exceptions as e:
        print("Falhou para", device['ip'], e)

    except KeyboardInterrupt:
        print("Você pressionou Ctrl+C")
        sys.exit()

# Aguarda para fechar
print("-"*79)
input("\nPressione Enter para finalizar.")
