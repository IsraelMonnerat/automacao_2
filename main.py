from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

navegator = webdriver.Chrome(ChromeDriverManager().install())

navegator.get('https://stamonline.com.br/curriculos/index.php')

print('Executando...')

# CSS selector
login_cpf = '#login'
password_cpf = '#senha'
button_path = '#form > div.form-group.text-center > button > strong'

# identifica e retorna os elementos CSS
login_element = navegator.find_element_by_css_selector(login_cpf)
password_element = navegator.find_element_by_css_selector(password_cpf)
button_element = navegator.find_element_by_css_selector(button_path)

# informações de login
login_element.send_keys('Login')
password_element.send_keys('Password')

# clicando no botão de login
button_element.click()

# clicando no botão salvar na página seguinte


button_path2 = '#subform'
button2_element = navegator.find_element_by_css_selector(button_path2)

for i in range(900000000000000000000000000):
    try:
        # wait 10 seconds before looking for element
        element = WebDriverWait(navegator, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#subform'))).click()
    finally:
        sleep(4)
        navegator.refresh()

input()
