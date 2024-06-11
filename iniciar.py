##python -m PyInstaller  -F --add-binary "c:\Windows\System32\python11.dll" iniciar.py
texto = 'Bem vindo!!, desculpe interface no futuro será uma melhor! Carregando aguarde...'
print(texto)
from funcoes.escrita import escrita_rapida,aguarda_input,escrita_rapida_sem_print
from funcoes.geral import gera_print
from chromedriver.chromedriver import Chromedriver
from telegram.telegram import Telegram
from time import sleep
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
        texto = 'Durante o processo será criado uma pasta nos downloads com excel que deve ser preenchido,\n caso tenha duvidas entre em contato com autor do projeto.'
        escrita_rapida_sem_print(texto)
        texto = 'Vamos começar preenchendo alguns dados para facilitar o processo!'
        escrita_rapida(texto)
        dado =aguarda_input('teste?')

        print('ah entao é assim... vou fechar programa')
        sleep(20)

    def valida_pasta_excel():
        pass


    def inicia_portal():
        pass



if __name__ == '__main__':
    Inicializacao().iniciar()