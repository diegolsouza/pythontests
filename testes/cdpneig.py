#!/usr/bin/env python3
#from __future__ import absolute_import, division, print_function
from getpass import getpass
from sys import exit, argv
#import paramiko
import netmiko
import pprint
import json
import signal

signal.signal(signal.SIGPIPE.signal.SIG_DFL)
signal.signal(signal.SIGINT.signal.SIG_DFL)


# Controle de argumentos
if len(argv) < 2:
    print("Faltam argumentos.\nUtilizar: cmdrunner.py <arquivo TXT com comandos> <arquivo JSON com devices>")
    exit()

# Abre o arquivo contendo os IPs
with open(argv[1]) as cmd_file:
    commands = cmd_file.readlines()

# Função para pedir senha
def get_password():
    password = None
    while not password:
        password = getpass(prompt="Senha: ")
        password_verify = getpass(prompt="Digite a senha novamente: ")
        if password != password_verify:
            print("Senha nao confere. Tente novamente.")
            password = None
    return password

# Funcao para pegar as configs via cdp
def get_cfg_cdp(input_string):
    lines = input_string.splitlines()[5:]
    hostname = None
    config = []
    for line in lines:
        words = line.split()
        if len(words) == 1:
            hostname = words[0].split(".")[0]
        else
            if hostname is None:
                hostname = words.pop(0).split(".")[0]
            local = "".join(words[0:2])
            remote = "".join(words[-2:])
            description = "_".join((hostname, remote))
            config.append("interface " + local)
            config.append(" description " + description)
            config.append("!")
            hostname = None


# Requisição de credenciais
username = input("Usuario: ")
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
        output = connection.send_command("show cdp neighbors")
        lines = output.splitlines()[5:]
        hostname = None
        config = []
        for line in lines:
            words = line.split()
            if len(words) == 1:
                hostname = words[0].split(".")[0]
            elif hostname is None:
                hostname = words[0].split(".")[0]
                local = "".join(words[1:3])
                remote = "".join(words[-2:])
                description = "_".join((hostname, remote))
                config.append("interface " + local)
                config.append(" description " + description)
                config.append("!")
                hostname = None
            else
                local = "".join(words[0:2])
                remote = "".join(words[-2:])
                description = "_".join((hostname, remote))
                config.append("interface " + local)
                config.append(" description " + description)
                config.append("!")
                hostname = None
        print("\n".join(config))

        connection.disconnect()

    # Tratamento de erros
    except netmiko_exceptions as e:
        print("Falhou para", device['ip'], e)

    except KeyboardInterrupt:
        print("Voce pressionou Ctrl+C")
        sys.exit()

# Aguarda para fechar
print("-"*79)
input("\nPressione Enter para finalizar.")
