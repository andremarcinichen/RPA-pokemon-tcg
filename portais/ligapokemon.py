# from chromedriver.chromedriver import Chromedriver
import requests

class LigaPokemon:
    ulr_base = 'https://www.ligapokemon.com.br/'

    def iniciar(self):
        self.get_html()
        pass



    def get_html (self):
        ### captcha cloud flare vou precisar quebrar isso
        headers = {
        'Cookie': '_ga_DQMPEZ847L=GS1.1.1718155905.12.1.1718157105.50.0.0; _ga=GA1.1.304036500.1698877975; _ga_RN47SGMMGJ=GS1.1.1700435250.2.1.1700435353.0.0.0; _ga_8QZH1QED7F=GS1.1.1718155905.12.1.1718157105.50.0.0; PHPSESSID=5f1i5rpqncmu9tdtcbqf3sbtm0; APPprC12=prC1224; _gcl_au=1.1.864915840.1718155906; cf_clearance=E9y0fnman1wQBOk3w1VQxlcLOiIbb5HbxEv4Yshfe2Q-1718155906-1.0.1.1-YH4I0KbAAzglUy7Jv5.ffHgq9m9iYfTqdM56H3VnmAWPsJJjDJzJVKForYkNJT1axBjpN8XFL5kjIlV0J6NTLA; mpLastAba=1; mpLastAba=1'
        }
        busca = 'Shiftry (003/054)'
        url = self.ulr_base + '?view=cards/search&card=' + busca
        resposta = requests.get(url)
        if resposta.status_code==404:
            raise ValueError('Erro 404 na ligapokemon')
        html = resposta.text
        pass


if __name__ == '__main__':
    LigaPokemon().iniciar()