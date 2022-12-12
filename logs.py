#!/usr/bin/env python3

import os
import logging

# BOILERPLATE
# TODO: usar funcao
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, logging.DEBUG)
ch = logging.StreamHandler()  # Console/terminal/stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s " "l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")  # a partir do warning que comeca a msotrar
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("---------")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("[ERRO] Deu erro %s", str(e))