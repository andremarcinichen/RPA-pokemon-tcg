import requests, os
from dotenv import load_dotenv



class Telegram:

    def iniciar(self):
        load_dotenv('.env')    

    def enviar_msg(self, msg:str=''):
        token_telegram = os.getenv('token_telegram')
        url = f'https://api.telegram.org/bot{token_telegram}/sendMessage'
        grupo_condado_erro = os.getenv('grupo_condado_erro')
        payload = {
            'chat_id': grupo_condado_erro,
            'text': msg
        }
        retorno = requests.post(url,payload)
        if retorno.status_code!=200:
            raise ValueError('Status code inesperado:' +str(retorno.status_code))


if __name__ == '__main__':
    Telegram().enviar_msg('qualquer msg')