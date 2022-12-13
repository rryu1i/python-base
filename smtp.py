#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "roger@issonaga.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este e o meu e-mail enviado pelo Python
<b>Ola Mundo</b>
"""


message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=25) as server:
    server.sendmail(FROM, TO, message)