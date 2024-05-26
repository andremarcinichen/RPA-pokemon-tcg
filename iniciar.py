##python -m PyInstaller iniciar.py
from funcoes.escrita import escrita_lenta,escrita_rapida,aguarda_input
from funcoes.geral import gera_print
from telegram.telegram import Telegram
import pandas as pd

class Inicializacao:

    def iniciar(self):
        try:
            self.abertura()
        except Exception:
            try:
                print_path = gera_print()
                Telegram().iniciar(print_path)
            except Exception:
                print_path = gera_print()
                aguarda_input('Favor notificar o autor do erro inesperado. Digite enter para finalizar.')

    def abertura(self):
        texto = 'Bem vindo!!, desculpe interface no futuro será uma melhor!'
        escrita_lenta(texto)
        texto = 'Durante o processo será criado uma pasta nos downloads com excel que deve ser preenchido, caso tenha duvidas entre em contato com autor do projeto.'
        escrita_rapida(texto)
        texto = 'Vamos começar preenchendo alguns dados para facilitar o processo!'
        escrita_rapida(texto)
        dado =aguarda_input('pq xu nao ama?')
        while True:
            pass

    def valida_pasta_excel():
        pass






if __name__ == '__main__':
    Inicializacao().iniciar()