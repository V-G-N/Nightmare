#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Instagram: vangogh.nithz

from os import execl, path, system
from sys import executable, argv


try:
    from requests import get
except:
    system('python3 -m pip install --upgrade pip && pip3 install requests TerminalButtons')
    execl(executable, executable, *argv)
try:
    exec(
        get('https://raw.githubusercontent.com/V-G-N/Nightmare/blob/main/data/layout.py').text
    )
except:
    print('Ops. Existe um erro de conexão, Verifique se esta conectado a uma rede')

