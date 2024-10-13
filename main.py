import os
import sys
import random
from estados import estados
from util import *

indice_estado = 0
estado_atual = estados[indice_estado]
sorteio = escolher_palavra_do_database(sys.argv[1:])
palavra = sorteio[0]
resultado = False
letras_usadas = []
segredo = mascacar(palavra)
exibir_messagem_letra_usada = False
exibir_messagem_tamanho_da_palavra = False
finalizado = False
exibir_dicas = False
max_dicas_atingidas = False
dicas = []

# print(palavra)

while True:
    print("JOGO DA FORCA")
    print("Adivinhe a palavra")

    if exibir_dicas and max_dicas_atingidas == False:
        dica = random.choice(sorteio[1])
        dicas.append(dica)
        sorteio[1].remove(dica)
        exibir_dicas = False
    
    if len(dicas) == 3:
        max_dicas_atingidas = True
    
    for dica in dicas:
        print(dica)
    
    if max_dicas_atingidas:
        print('Todas as dicas já foram utilizas')

    tentativa = False

    print(estado_atual)

    mostrar_mascara(segredo)

    print('Palavras usadas:', letras_usadas)

    if exibir_messagem_letra_usada:
        print('Letra já usada, tente outra!')

    if exibir_messagem_tamanho_da_palavra:
        print('Só é possível entrar com uma letra, tente outra vez!')

    if finalizado:
        break

    letra_digitada = input('Digite uma letra: ').upper()

    if len(letra_digitada) > 1 and letra_digitada != 'DICA':
        exibir_messagem_tamanho_da_palavra = True
        os.system('clear')
        continue
    else:
        exibir_messagem_tamanho_da_palavra = False

    if letra_digitada == 'DICA':
        exibir_dicas = True
        os.system('clear')
        continue

    if letra_digitada in letras_usadas:
        exibir_messagem_letra_usada = True
        os.system('clear')
        continue
    else:
        exibir_messagem_letra_usada = False

    for i, letra in enumerate(palavra):
        if letra_digitada == letra_basica(letra):
            segredo[i] = letra
            tentativa = True

    if tentativa == False:
        letras_usadas.append(letra_digitada)
        indice_estado = indice_estado + 1
        estado_atual = estados[indice_estado]
        if indice_estado == 6:
            resultado = False
            finalizado = True
            os.system('clear')
            continue
    else:
        if verificar_se_palavra_foi_descoberta(segredo):
            resultado = True
            finalizado = True
            os.system('clear')
            continue
    os.system('clear')

if resultado:
    print('Vitória!')
else:
    print(f'Derrota!! a palavra era {palavra}.')