from selenium import webdriver
from selenium.webdriver.common.by import By
#selenium import_

import time
from pynput.keyboard import Key, Controller
#common_

keyboard = Controller()

#Desabilitando popus de notificação
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

#Inicia o driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

#Acessando a página de login
driver.get('https://www.espiaoclouddfe.com/')

#Tempo para carregamento
time.sleep(5)


#Enter :)
def Enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
#}

def login():

    #Encontrando o campo de input e inserindo o E-mail
    driver.find_element(By.ID, 'email_p').send_keys('<<E-mail>>')

    #Encontrando o campo de input e inserindo a senha
    driver.find_element(By.ID, 'senha_p').send_keys('<<Senha>>')

    #Click click
    driver.find_element(By.ID, 'login-btn').click()

    #_
    time.sleep(2)

    #Selecionando acesso
    driver.find_element(By.ID, 'sl_empresas_chosen').click()
    
    #(0) se houver apenas um acesso, se não (x)
    for downner in range(0) : keyboard.press(Key.down)
    keyboard.release(Key.down)
    Enter()

    #_
    driver.find_element(By.ID, 'btn_varias').click()
    
    #_
    time.sleep(9)
    
    #Fechando o ModalContent
    try:driver.find_element(By.XPATH, '//*[@id="modalmonitor"]/div/div/div[1]/button').click()
    except:pass

    while True:
        pass
login()