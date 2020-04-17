from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 

#Inserir nomes ou números dos contatos

contact_list = [

"Contato 1", "Contato 2", "Contato 3","etc"

]

# Automático) Abre o WhatsApp Web

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
assert "WhatsApp" in driver.title

# (Automático) 15 segundos para ler o QR code no Whatsapp Web com o aparelho que possui os contatos salvos na agenda

time.sleep(15)


# (Automático) Pesquisa dos contatos no campo de busca

contact = driver.find_element_by_css_selector("._3F6QL._3xlwb > ._2S1VP")

for phone in contact_list:
    contact.send_keys(phone)
    time.sleep(2)

    try:
        result = driver.find_element_by_css_selector("._2wP_Y[style*='z-index: 0'] span.matched-text._3FXB1")         
    except NoSuchElementException:
        print("{} não encontrado, verifique se o nome ou número do contato está correto".format(phone))
        contact.clear()
        continue
    else:
        result.click()
    

# Inserir mensagem aqui na string

    message = driver.find_element_by_css_selector("._3F6QL._2WovP > ._2S1VP[contenteditable=true]")
    message.send_keys("#ping")

# Envia mensagem
    message.send_keys(Keys.RETURN)
    time.sleep(2)

driver.close()
