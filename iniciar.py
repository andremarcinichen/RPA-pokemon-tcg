##python -m PyInstaller iniciar.py
from .funcoes.escrita import escrita_lenta


class Inicializacao:

    def iniciar(self):
        texto = 'Bem vindo!!'
        escrita_lenta(texto)

        while True:
            pass



if __name__ == '__main__':
    Inicializacao().iniciar()