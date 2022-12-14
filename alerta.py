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
from typing import Dict

log = logging.Logger("Alerta")


def is_completely_filled(dict_of_inputs: Dict) -> bool:
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs.values())
    filled_size = len([value for value in dict_of_inputs.values() if value is not None])
    return info_size == filled_size
    
def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error(f"{key} Invalida")
            break

info = {
    "temperatura": None,
    "umidade": None
}

# PROGRAMA PRINCIPAL

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temperatura, umidade = info.values()

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