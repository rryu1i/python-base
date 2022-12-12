#!/usr/bin/env python3
"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das
condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
    "ALERTA!!! 🥵 Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:
python3 alerta.py
temperatura: 30
umidade: 90
...
"ALERTA!!! 🥵♒ Perigo de calor úmido"
"""
import logging
import sys
log = logging.Logger("Alerta")

"""
try:
    temperatura = float(input("Qual a temperatura? ").strip())
except ValueError:
    log.error("Temperatura Invalida")
    sys.exit(1)

try:
    umidade = float(input("Qual a umidade do ar? ").strip())
except ValueError:
    log.error("Umidade Invalida")
    sys.exit(1)
"""

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()


for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key} Invalida")
        sys.exit(1)

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temperatura > 30 and temperatura*3 >= umidade:
    print("ALERTA!!! 🥵 Perigo de calor úmido")
elif temperatura >= 10 and temperatura <= 30:
    print("😀 Normal")
elif temperatura >= 0 and temperatura <= 10:
    print("🥶 Frio")
elif temperatura < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")