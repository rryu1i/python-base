"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

VOGAIS = "aeiouãõâôêéáíó" 

words = []
while True:
    word = input('Digite uma palavra (ou enter para sair):').strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        if letter.lower() in VOGAIS:
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep="\n")  # o * desempacota a lista


