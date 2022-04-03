from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\wekis\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clicar_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as error:
            print('Erro ao clicar em Sign in:', error)
    
    def acessar(self, site):
        self.chrome.get(site)
    
    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('WekisleySouza')
            input_password.send_keys('azul123')
            sleep(3)
            btn_login.click()

        except Exception as error:
            print("Erro ao tentar login!", error)

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://github.com/')

    chrome.clicar_sign_in()
    chrome.faz_login()

    sleep(2)
    chrome.sair()