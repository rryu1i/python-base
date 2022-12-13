#!/user/bin/env python3
"""Imprime a mensagem de um e-mail"""

__version__ = "0.1.1"

import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe o arquivo com os emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)  # emails.txt
templatepath = os.path.join(path, templatename)  # email_tmpl.txt

with smtplib.SMTP(host="localhost", port=8025) as server:


    for line in open(filepath):
        nome, email = line.split(",")
        text = (
            open(templatepath).read()
            % {
                "nome": nome,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "https://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5
            }
        )
        from_ = "roger@kek.com"
        to = ", ".join([email])
        message = MIMEText(text, "html")
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())