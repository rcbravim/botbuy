# External Libs
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

# Internal Libs
from methods import send_email, shutdown
import product as p

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# BUGS LIST
    # TRATAMENTO DE ERROS
    # 
# FEATURES LIST
    # INFORMAÇÃO DE EXECUÇÃO NA TELA (TEMPOS)
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#      #      #      #      #      #      #      #      #      #      
# #    # #    # #    # #    # #    # #    # #    # #    # #    # #    
# # #  # # #  # # #  # # #  # # #  # # #  # # #  # # #  # # #  # # #  
# #    # #    # #    # #    # #    # #    # #    # #    # #    # #    
#      #      #      #      #      #      #      #      #      #      

# Init Config
watcher = True
dir_path = os.path.abspath(__file__).replace('app.py','')
team = [
    'raphael.bravim@gmail.com',
    'ricalves1131@gmail.com',
    'arthur_marintl@icloud.com',
    'henribarres@gmail.com',
    'raphael.bravim@gmail.com'
]
webdriver_path = rf'{dir_path}chromedriver.exe'
service=Service(webdriver_path)

# Disable Errors / WatcherOnOff
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
if not watcher:
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

# Get Starting... / Sign-In...
print('>>> INICIANDO BOT v0.2...')
print('>>> ABRINDO PÁGINA DE LOGIN...')
print('>>> FAVOR ENTRAR COM USUÁRIO/SENHA...')
driver = webdriver.Chrome(service=service, options=options)
driver.get(p.SIGNING_PAGE)

while True:
    try:
        hello = driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').get_attribute("textContent")
        if hello == 'Hello, Sign in':
            print('>>> ERRO DURANTE, LOGIN...')
            print('>>> FAVOR TENTAR NOVAMENTE...')
            driver.get(p.SIGNING_PAGE)
        else:
            print('>>> LOGADO COM SUCESSO!')
            break
    except:
        pass

# Looking for Product...
print('>>> ABRINDO PAGINA DO PRODUTO...')
driver.get(p.PRODUCT).minimize_window()
driver.implicitly_wait(1)

# The Loop...
print('>>> AGUARDANDO PRODUTO FICAR DISPONÍVEL!')
print('>>> PRESSIONE CTRL+C PARA ENCERRAR...')

while True:
    try:
        buy_buttton = driver.find_element(By.XPATH, p.XPATH_BTN)
        avaliable_at = datetime.now()
        print(f'>>> PRODUTO DISPONÍVEL!')
        print(f'>>> DATA/HORA: {avaliable_at.strftime("%d/%m/%Y %H:%M")}')
        break
    except:
        driver.refresh()
        if shutdown():
            print(">>> ENCERRANDO...")
            quit()
        pass

# Printscreen Manager
print(f'>>> PRINTANDO TELA...')
image_file = avaliable_at.strftime("%d%m%Y%H%M")
image_name = f'{dir_path}\{image_file}'
driver.save_screenshot(f'{image_name}.png')

# Checking Price...
print(f'>>> COMPARANDO PREÇO...')
_price = driver.find_element(By.CSS_SELECTOR, p.PATH_PRICE)
price = str(_price.text)
price = float(price.replace('$','').replace(',',''))

if price > p.PRICE_BASE:
    print('>>> PREÇO ACIMA DO DEFINIDO!')
    print(f'>>> (${price:.2f} > ${p.PRICE_BASE:.2f})')
    print('>>> ENVIANDO RELATÓRIO POR EMAIL...')
    print('>>> BOT ENCERRADO!')
    input('>>> PRESSIONE ENTER PARA SAIR...')

    raw_message = []
    raw_message.append(f'>>> Produto ficou disponível na data/hora: {avaliable_at.strftime("%d/%m/%Y %H:%M")}')
    raw_message.append(f'>>> Preço definido para compra: ${p.PRICE_BASE}')
    raw_message.append(f'>>> Preço no site: ${price}')
    raw_message.append(f'>>> Bot encerrado...')

    fine_message = ''
    for line in raw_message:
        fine_message += line + '<br>'

    send_email(team, 'Produto Acima do Preço Definido!', fine_message)
    print('>>> BOT ENCERRADO!')
    input('>>> PRESSIONE ENTER PARA SAIR...')
    quit()

# Keeping Purchase...
print(f'>>> PREÇO DE {_price.text} APROVADO!')
print(f'>>> EXECUTANDO COMPRA...')
buy_buttton.click()

print(f'>>> SELECIONANDO CARTÃO DE CRÉDITO...')
driver.implicitly_wait(1)
contiune_button = driver.find_element(By.CLASS_NAME, p.CONTINUE_BUY)
contiune_button.click()

print(f'>>> SELECIONANDO ENDEREÇO DE ENTREGA...')
driver.implicitly_wait(1)
use_this_address = driver.find_element(By.XPATH, p.DEFAULT_ADDRESS)
use_this_address.click()

print(f'>>> EXECUTANDO ÚLTIMA ETAPA...')
driver.implicitly_wait(1)
place_order = driver.find_element(By.XPATH, p.PLACE_ORDER)
#place_order.click()

driver.implicitly_wait(1)
driver.save_screenshot(f'{image_name}_order.png')
print(f'>>> COMPRA REALIZADA COM SUCESSO!!!')
print(f'>>> ENVIANDO RELATÓRIO POR E-MAIL!!!')

raw_message = []
raw_message.append(f'>>> Produto ficou disponível na data/hora: {avaliable_at.strftime("%d/%m/%Y %H:%M")}')
raw_message.append(f'>>> Preço definido para compra: ${p.PRICE_BASE}')
raw_message.append(f'>>> Preço no site: ${price}')
raw_message.append(f'>>> Compra executada com sucesso!')

fine_message = ''
for line in raw_message:
    fine_message += line + '<br>'

send_email(team, 'Produto Adquirido Com Sucesso!', fine_message)
input('>>> PRESSIONE ENTER PARA SAIR...')