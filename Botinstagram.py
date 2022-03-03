from time import sleep
from random import randint
import os
try:

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    seleniun = False
    from selenium_stealth import stealth
    stealt = False
except:
    print('\033[91mFalta você instalar algumas bibliotecas\033[m')
    print('\033[93muse os comandos\033[m')
    if seleniun:
        print('\033[97m pip install selenium\033[m')
    if stealt:
        print('\033[97m pip install selenium-stealth\033[m')

class Botinstagram:
    def __init__(self, segurança):
        stealt = True
        seleniun = True



        self.options = Options()
        if segurança:
            self.options = Options()
            self.options.add_experimental_option('excludeSwitches', ["enable-automation"])
            self.options.add_experimental_option('useAutomationExtension', False)
            self.options.add_argument('--incognito')
            self.options.add_argument('--window-size=400,750')
            self.navegador = webdriver.Chrome(options=self.options)
            stealth(
                self.navegador,
                languages=['pt-BR', 'pt'],
                Permissions='prompt',
                vendedor='Google Inc',
                platform='Win64',
                webgl_vendor='Intel Inc',
                renderer='Intel Iris OpenGL Engine',
                fix_hairline=True)
        else:
            self.navegador = webdriver.Chrome(options=self.options)
        self.açao = ActionChains(self.navegador)
        self.navegador.get('https://www.instagram.com/')

        self.user = input('\033[94m>>>>digite o nome do perfil:\033[m ')
        self.senha = input('\033[94m>>>>digite a senha do perfil:\033[m ')
        self.path_fotos = input('\033[92m>>>>digite o nome da pasta:\033[m ')
        self.quantidade_defotos = 4  # int(input('\033[94m>>>>quantas fotos devem ser postadas? '))
        self.sms = False

    def login(self):
        while True:
            cookies = []
            for _, _, item in os.walk(fr'C:\Users\MTZ\PycharmProjects\montador de perfil\cookies'):
                N = True  # isso é feito para obter uma lista com nomes dos objetos dentro da pasta
            # ------------------------------------ gambiarra para logar com cookies -----------------------------------
            if f'{self.user}.txt' in item:
                arquivo = open(fr'C:\Users\MTZ\PycharmProjects\montador de perfil\cookies\{self.user}.txt', 'r')
                arquivo = arquivo.readlines()
                for cookie in arquivo:
                    cookies.append(cookie.split())
                for i in cookies:
                    cookie = ({'name': i[0], 'value': i[1], 'domain': i[2]})
                    self.navegador.add_cookie(cookie)
                self.navegador.refresh()
                sleep(5)
                # ------------------------------------------------------------------------------------------------------------

                # -------------------------------- teste se o login foi concluido com sucesso -------------------------------
                while True:
                    try:
                        erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/p')
                        print('erro ao carregar a pagina')
                        print(erro.text)
                        self.navegador.refresh()
                        sleep(5)
                    except:
                        break
                try:
                    self.navegador.find_element(By.NAME, 'username')
                    print('\033[91mos cookies estão quebrados\033[m')
                    print('\033[93mre-logando...\033[m')
                    self.navegador.find_element(By.NAME, 'username').send_keys(self.user)
                    self.navegador.find_element(By.NAME, 'password').send_keys(self.senha, '\n')
                    sleep(5)
                    try:
                        erro = self.navegador.find_element(By.ID, 'slfErrorAlert')
                        print(f'\033[91m{erro.text}\033[m')
                        self.navegador.close()
                        sleep(3)
                        self.navegador = webdriver.Chrome(options=self.options)
                        self.navegador.get('https://www.instagram.com/')
                        sleep(3)
                    except:
                        print('\033[92mnenhum erro foi encotrado\033[m')
                        arquivo = open(fr'C:\Users\MTZ\PycharmProjects\montador de perfil\cookies\{self.user}.txt',
                                       'w+', )
                        for i in self.navegador.get_cookies():
                            nome = i['name']
                            value = i['value']
                            domain = i['domain']
                            arquivo.write(f'''{nome} {value} {domain}
''')
                            print('\033[92mcookies salvos\033[m')
                        try:
                            bloque_foto = self.navegador.find_element(By.XPATH,
                                                                      '//*[@id="react-root"]/section/main/div[2]/div/div/div[1]/div[2]/h2')
                            print(f'\033[91m{bloque_foto.text}\033[m')
                            sleep(1)
                            b_ok = self.navegador.find_element(By.XPATH,
                                                               '//*[@id="react-root"]/section/main/div[2]/div/div/div[2]/div/div/button').click()
                            sleep(2)
                            self.navegador.get(f'https://www.instagram.com/{self.user}/')
                        except:
                            n = 0
                        break
                except:
                    try:
                        bloque_foto = self.navegador.find_element(By.XPATH,
                                                                  '//*[@id="react-root"]/section/main/div[2]/div/div/div[1]/div[2]/h2')
                        print(f'\033[91m{bloque_foto.text}\033[m')
                        sleep(1)
                        b_ok = self.navegador.find_element(By.XPATH,
                                                           '//*[@id="react-root"]/section/main/div[2]/div/div/div[2]/div/div/button').click()
                        sleep(2)
                        self.navegador.get(f'https://www.instagram.com/{self.user}/')
                    except:
                        try:
                            sms = self.navegador.find_element(By.XPATH,
                                                              '//*[@id="react-root"]/section/main/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/span')
                            if sms.text == 'Confirme que é você para entrar':
                                print('\033[31ma conta sofreu SMS\033[m')
                                self.sms = True
                                break
                        except:
                            break
                    break
            # -------------------------------------------------------------------------------------------------------------------

            # ---------------------------- logando com user e senha caso nao houver cookies salvos ---------------------------
            else:
                print('cookie nao existe')
                while True:
                    try:
                        sleep(3)
                        self.navegador.find_element(By.NAME, 'username').send_keys(self.user)
                        self.navegador.find_element(By.NAME, 'password').send_keys(self.senha, '\n')
                        sleep(5)
                        break
                    except:
                        self.navegador.refresh()
                        sleep(2)

                try:
                    erro = self.navegador.find_element(By.ID, 'slfErrorAlert')
                    print(f'\033[91m{erro.text}\033[m')
                    self.navegador.close()
                    sleep(3)
                    self.navegador = webdriver.Chrome(options=self.options)
                    self.navegador.get('https://www.instagram.com/')
                    sleep(3)
                except:
                    try:
                        sms = self.navegador.find_element(By.XPATH,
                                                          '//*[@id="react-root"]/section/main/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/span')
                        print('1', sms.text, '2', sms.get_attribute('text'), '3', sms.get_attribute('title'))
                        if sms.text == 'Confirme que é você para entrar':
                            print('\033[31ma conta sofreu SMS\033[m')
                            self.sms = True
                            break
                    except:
                        n = 0
                    print('\033[92mnenhum erro foi encotrado\033[m')
                    arquivo = open(fr'C:\Users\MTZ\PycharmProjects\montador de perfil\cookies\{self.user}.txt', 'w+')
                    print('\033[92mCookies salvos.\033[m')
                    for i in self.navegador.get_cookies():
                        nome = i['name']
                        value = i['value']
                        domain = i['domain']
                        arquivo.write(f'''{nome} {value} {domain}
''')
                    try:
                        bloque_foto = self.navegador.find_element(By.XPATH,
                                                                  '//*[@id="react-root"]/section/main/div[2]/div/div/div[1]/div[2]/h2')
                        print(f'\033[91m{bloque_foto.text}\033[m')
                        sleep(1)
                        b_ok = self.navegador.find_element(By.XPATH,
                                                           '//*[@id="react-root"]/section/main/div[2]/div/div/div[2]/div/div/button').click()
                        sleep(2)
                        self.navegador.get(f'https://www.instagram.com/{self.user}/')
                    except:
                        break
                    break
        if self.sms:
            n = 0
        else:
            açao = ActionChains(self.navegador)
            try:
                popup = self.navegador.find_element(By.CSS_SELECTOR, 'div._1XyCr')
                print('pop encontrado')
                sleep(0.5)
                açao.send_keys(Keys.TAB).perform()
                sleep(0.5)
                açao.send_keys(Keys.TAB).perform()
                sleep(0.5)
                açao.send_keys(Keys.ENTER).perform()
            except:
                print('pop não encontrado')
        # -------------------------------------------------------------------------------------------------------------------

    def foto_perfil(self):
        if self.sms:
            n = 0
        else:
            count = 0
            self.navegador.get(f'https://www.instagram.com/{self.user}/')
            while True:
                try:
                    erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/p')
                    print('erro ao carregar a pagina')
                    print(erro.text)
                    self.navegador.refresh()
                    sleep(5)
                except:
                    break
            sleep(5)
            b_foto_perfil = self.navegador.find_element(By.XPATH,
                                                        '//*[@id="react-root"]/section/main/div/header/div/div/div/button')
            while b_foto_perfil.get_attribute('title') == 'Adicionar uma foto do perfil':
                for _, _, i in os.walk(fr'C:\Users\MTZ\Desktop\Salvar\todas as fotos\{self.path_fotos}\foto perfil'):
                    for foto in i:
                        if foto[-3:] == 'jpg' or foto[-4:] == 'jpeg':
                            add_foto = self.navegador.find_element(By.XPATH,
                                                                   '//*[@id="react-root"]/section/main/div/header/div/div/div/div/form/input')
                            add_foto.send_keys(
                                fr'C:\Users\MTZ\Desktop\Salvar\todas as fotos\{self.path_fotos}\foto perfil\{foto}')
                            sleep(3)
                b_foto_perfil = self.navegador.find_element(By.XPATH,
                                                            '//*[@id="react-root"]/section/main/div/header/div/div/div/button')
                try:
                    print('quantidade de fotos perfil', len(i))
                except:
                    count += 1
                    if count == 1:
                        print('\033[91mNão conseguimos encotrar a pasta com a foto de perfil\033[m')
                        print('''\033[97m(Não precisa fechar o Bot apenas 
                        adicione uma pasta com nome foto perfil entre as fotos)\033[m''')

    def postar_foto(self):
        if self.sms:
            n = 0
        else:
            fotos_ja_postada = 0
            # try:
            while True:
                if fotos_ja_postada == self.quantidade_defotos:
                    print('\033[92mTodas as fotos foram postadas com sucesso.\033[m')
                    break
                try:
                    publicações = self.navegador.find_element(By.CSS_SELECTOR, 'span.g47SY')
                    break
                except:
                    try:
                        erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/p')
                        print(erro.text)
                    except:
                        sleep(2)
            for _, _, i in os.walk(fr'C:\Users\MTZ\Desktop\Salvar\todas as fotos\{self.path_fotos}'):
                for nome_foto in i:
                    if nome_foto[-3:] == 'jpg' or nome_foto[-4:] == 'jpeg':
                        while True:
                            try:
                                publicações = self.navegador.find_element(By.CSS_SELECTOR, 'span.g47SY')
                                break
                            except:
                                sleep(2)
                        if fotos_ja_postada == int(publicações.text) < self.quantidade_defotos:
                            self.navegador.find_element(By.CSS_SELECTOR, 'div.vZuFV').click()
                            print('\033[92mbotao enviar apertado com sucesso.\033[m')
                            sleep(2)
                            mandar_ft = self.navegador.find_element(By.XPATH,
                                                                    '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input')
                            mandar_ft.send_keys(
                                fr'C:\Users\MTZ\Desktop\Salvar\todas as fotos\{self.path_fotos}\{nome_foto}')
                            print('\033[92mfoto enviada\033[m')
                            while True:
                                try:
                                    sleep(2)
                                    status_element = self.navegador.find_element(By.XPATH, '/html/body/div[6]/div[2]')
                                    status = status_element.get_attribute('aria-label')
                                except:
                                    try:
                                        status_element = self.navegador.find_element(By.XPATH,
                                                                                     '/html/body/div[8]/div[2]/div/div/div/div[1]/div/div/h1')
                                        print('\033[91mA foto esta fora do padrão\033[m')
                                        status = status_element.get_attribute('aria-label')
                                        print(status)
                                        sleep(randint(1, 40) / 20)
                                        self.açao.send_keys(Keys.ESCAPE).perform()
                                        sleep(0.2)
                                        self.açao.send_keys(Keys.ESCAPE).perform()
                                        sleep(3)
                                        break
                                    except:
                                        print('\033[92mFoto aceita\033[m')
                                print(f'\033[97m{status}\033[m')
                                sleep(randint(0, 40) / 20)
                                if status == 'Cortar' or status == 'Editar' or status == 'Criar nova publicação':
                                    sleep(1)
                                    print('\033[92mOk\033[m')
                                    try:
                                        self.navegador.find_element(By.XPATH,
                                                                    '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()
                                    except:
                                        print('\033[91mO click no para enviar botão falhou\033[m')
                                elif status == 'Compartilhando':
                                    sleep(randint(40, 100) / 20)
                                elif status[0] == 'P':
                                    sleep(1.5)
                                    print('\033[92mPublicação finalizada.\033[m')
                                    self.açao.send_keys(Keys.ESCAPE).perform()
                                    self.navegador.refresh()
                                    while True:
                                        try:
                                            erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/p')
                                            print(erro.text)
                                            self.navegador.refresh()
                                            sleep(2)
                                        except:
                                            break
                                    sleep(2)
                                    sleep(randint(200, 400) / 20)
                                    break
                        else:
                            if fotos_ja_postada == self.quantidade_defotos:
                                break
                            fotos_ja_postada += 1
                            print(f'\033[92m{fotos_ja_postada}• Foto postada\033[m')
                    else:
                        print(f'\033[92m>>>>arquivo {nome_foto} foi removido\033[m')
                        os.remove(fr'C:\Users\MTZ\Desktop\Salvar\todas as fotos\{self.path_fotos}\{nome_foto}')

            # except:
            #     print('\033[91mo envio falhou\033[m')
            #     self.açao.send_keys(Keys.ESCAPE).perform()
            #     self.açao.send_keys(Keys.ESCAPE).perform()
            #     self.açao.send_keys(Keys.ESCAPE).perform()

    def navegar_pagina_inicial(self):
        parada = randint(250, 330)
        time = 0
        var = 1
        while True:
            tempo = randint(30, 80) / 10
            aleatorio = randint(1, 100)
            time += tempo
            print('{}.{}'.format(int(time / 60), int(time % 60)), ':', f'{int(parada / 60)}.{int(parada % 60)}')
            try:
                b_element_like = self.navegador.find_element(By.XPATH,
                                                        f'//*[@id="react-root"]/section/main/section/div/div[2]/div/article[{var}]')
                self.açao.move_to_element(b_element_like).perform()
                if var < 8:
                    var += 1
                erro = False
            except:
                print(f'elemento {var} nao foi encotrado')
                var -= 1
                erro = True
            if erro == False:
                sleep(tempo)
            if aleatorio < 5:
                print('like dado')
                self.açao.double_click(b_element_like).perform()
            if time >= parada:
                break

    def navegar_historys(self):
        time = count = quantidade_de_lives = 0
        parada = randint(250, 330)
        lives = self.navegador.find_elements(By.CSS_SELECTOR, 'span._1iHbP')
        for i in lives:
            quantidade_de_lives += 1
        history = self.navegador.find_element(By.XPATH,
                                              f'//*[@id="react-root"]/section/main/section/div/div[1]/div[2]/div/div/div/ul/li[{3 + quantidade_de_lives}]/div/button')
        self.açao.click(history).perform()
        while True:
            tempo = randint(1000, 10000) / 750
            aleatorio = randint(1, 100)
            if aleatorio <= 20:
                self.açao.send_keys(Keys.ARROW_RIGHT).perform()
            if 20 > aleatorio <= 30:
                self.açao.send_keys(Keys.ARROW_DOWN).perform()
            time += tempo
            a = self.navegador.find_elements(By.CSS_SELECTOR, 'div._5udpW')
            print(f'tempo:{tempo:.2f}')
            sleep(tempo)
            if len(a) == 0:
                count += 1
                if count >= 3:
                    break
            print('{}.{}'.format(int(time / 60), int(time % 60)), ':', f'{int(parada / 60)}.{int(parada % 60)}')
            if time >= parada:
                self.açao.send_keys(Keys.ESCAPE).perform()
                break

    def navegar_explorar(self):
        self.navegador.get('https://www.instagram.com/explore/')
        sleep(5)
    # ------------------------- Teste para ver se a pagina carregou certo ----------------------------------
        while True:
            try:
                conteudo = self.navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/div')
                if ' padding-bottom' in conteudo.get_attribute('style'):
                    break
            except:
                self.navegador.refresh()
                sleep(5)
    # ---------------------------------------------------------------------------------------------------------

        parada = randint(250, 330)
        time = 0
        var = 1
        while True:
            tempo = randint(30, 80) / 10
            aleatorio = randint(1, 100)
            time += tempo
            print('{}.{}'.format(int(time / 60), int(time % 60)), ':', f'{int(parada / 60)}.{int(parada % 60)}')
            try:
                conj_posts = self.navegador.find_element(By.XPATH, # conjutos de posts
                                                             f'//*[@id="react-root"]/section/main/div/div[1]/div/div[{var}]')
                self.açao.move_to_element(conj_posts).perform()
                if var < 12:
                    var += 1
                erro = False
            except:
                print(f'elemento {var} nao foi encotrado')
                var -= 1
                erro = True
            if not erro:
                print(f'sem erro {var}')
                sleep(tempo)
            else:
                print(f'erro {var}')
            if time >= parada:
                break

    def limpar_atividade(self):
        self.navegador.get('https://www.instagram.com/session/login_activity/')
        while True:
            try:
                teste = self.navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/h2')
                print(teste.text)
                if teste.text == 'Atividade de login':
                    break
                else:
                    self.navegador.get('https://www.instagram.com/session/login_activity/')
                    sleep(5)
            except:
                self.navegador.refresh()
                sleep(3)
        while True:
            try:
                elemento = self.navegador.find_element(By.CSS_SELECTOR, 'button._8A5w5')
                if elemento.text == 'Fui eu':
                    elemento.click()
                    sleep(0.5)
                    self.navegador.find_element(By.CSS_SELECTOR,'button.bIiDR').click()
                    sleep(0.6)
                    self.navegador.refresh()
                    sleep(3)
            except:
                try:
                    erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/h1/span')
                    print(erro.text)
                    if erro.text == 'Esta página não está funcionando':
                        self.navegador.refresh()
                        sleep(2)
                except:
                    try:
                        self.navegador.find_element(By.CSS_SELECTOR, 'button.HcJZg')
                    except:
                        break
        count = parar = 0
        while True:
            xpath_b_mais = f'/html/body/div[1]/section/main/div/article/div/div[2]/div/div[{count}]/div/div/div[3]/button'
            xpath_dados = f'/html/body/div[1]/section/main/div/article/div/div[2]/div/div[{count}]/div/div/div[2]/div[2]/div/div/span[1]/div/time'
            try:
                self.navegador.find_element(By.XPATH, xpath_dados)
                self.navegador.find_element(By.XPATH, xpath_b_mais).click()
                sleep(0.6)
                self.navegador.find_element(By.CSS_SELECTOR, 'button._8A5w5').click()
                sleep(0.5)
                self.navegador.find_element(By.CSS_SELECTOR, 'button.HoLwm').click()
                sleep(randint(10, 50) / 10)
                self.navegador.refresh()
                sleep(2)
                parar = 0
            except:
                try:
                    erro = self.navegador.find_element(By.XPATH, '//*[@id="main-message"]/h1/span')
                    print(erro.text)
                    if erro.text == 'Esta página não está funcionando':
                        self.navegador.refresh()
                        sleep(2)
                except:
                    try:
                        erro = self.navegador.find_element(By.XPATH, '/html/body/pre')
                        print(erro.text)
                        if 'tentar' in erro.text:
                            self.navegador.refresh()
                            sleep(2)
                    except:
                        parar += 1
                        if parar == 8:
                            break
                        print(f'{count}- nao encontrado')
                        count += 1
        print('saiu acabou')
        self.navegador.find_element(By.CSS_SELECTOR, 'button.wpO6b').click()
        sleep(randint(5, 20)/10)
        self.navegador.find_element(By.CSS_SELECTOR, 'button._8A5w5').click()
        sleep(randint(5, 20) / 10)


