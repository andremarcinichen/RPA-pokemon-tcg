
from time import sleep

def escrita_lenta(texto):
    print('')
    for letra in texto:
        print (letra, end='')
        sleep(0.1)