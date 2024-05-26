
from time import sleep

def escrita_lenta(texto):
    print('')
    for letra in texto:
        print (letra, end='')
        sleep(0.08)


def escrita_rapida(texto):
    print('')
    for letra in texto:
        print (letra, end='')
        sleep(0.01)

def aguarda_input(texto):
    print('')
    return input(texto)