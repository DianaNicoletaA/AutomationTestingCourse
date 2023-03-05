import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/"

driver.get(LINK)
time.sleep(1)

driver.maximize_window()
time.sleep(1)

link_web_form = driver.find_element(By.LINK_TEXT, "Complete Web Form")
print("")
link_web_form.click()
time.sleep(3)

lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f'Avem {len(lista_inputuri)} elemente cu tag-ul HTML <input>')

for element in lista_inputuri:
    element.click()
    time.sleep(1)


link_partial_web_form = driver.find_element(By.PARTIAL_LINK_TEXT, "Web Form")
link_partial_web_form.click()
time.sleep(3)

