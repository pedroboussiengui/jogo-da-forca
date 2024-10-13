import random
from database import *

def mascacar(palavra):
    segreddo = ['*'] * len(palavra)
    for i, letra in enumerate(palavra):
        if letra == '-':
            segredo[i] = '-'
    return segreddo

def mostrar_mascara(palavra):
    for i in palavra:
        print(i, end=' ')
    print('\n')

def verificar_se_palavra_foi_descoberta(palavra):
    if '*' not in palavra:
        return True
    return False


As = ['Ã', 'Á', 'À', 'Â']
Es = ['É', 'È', 'Ê', 'Ẽ']
Is = ['Ĩ', 'Î', 'Ì', 'Í']
Os = ['Ô', 'Õ', 'Ó', 'Ò']
Us = ['Û', 'Ũ', 'Ú', 'Ù']
Cs = ['Ç']
def letra_basica(letra):
    if letra in As:
        return 'A'
    elif letra in Es:
        return 'E'
    elif letra in Is:
        return 'I'
    elif letra in Os:
        return 'O'
    elif letra in Us:
        return 'U'
    elif letra in Cs:
        return 'C'
    else:
        return letra

def retornar_conjunto(args):
    db = []
    if 'animais' in args:
        db = db + animais
    if 'frutas' in args:
        db = db + frutas
    if 'paises' in args:
        db = db + paises
    random.shuffle(db)
    return db

def escolher_palavra_do_database(args):
   escolha = random.choice(retornar_conjunto(args))
   return escolha['nome'], escolha['dicas']