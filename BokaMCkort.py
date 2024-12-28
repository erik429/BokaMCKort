from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import smtplib
import sys
import json
import time
import requests
PATH = "C:\Program Files (x86)\chromedriver.exe" #ANGE PATH TILL CHROMEDRIVER.EXE
driver = webdriver.Chrome(PATH)
driver.get("https://fp.trafikverket.se/Boka/#/")
print("Laddar sidan..")
driver.maximize_window()
try:
    element = WebDriverWait(driver, 30). until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='Boka prov']"))
    )
    element.click()
except:
    driver.quit()
    driver.close()
try:
    element = WebDriverWait(driver, 30). until(
        EC.presence_of_element_located((By.ID, "social-security-number-input"))
    )
    element.click()
    print("Skriver in personnummer")
    driver.find_element(By.ID, "social-security-number-input").send_keys("DITT 12 PERSONNUMMER: ååååmmddxxxx")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='Fortsätt']"))
    )
    element.click()
    print("Vänligen logga in via Bank-ID")
except:
    driver.quit()
    driver.close()
try:
    element = WebDriverWait(driver, 100). until(
        EC.presence_of_element_located((By.LINK_TEXT, "Logga ut"))
    )
    #element.click()
    print("Du är inloggad")
except:
    driver.quit()
    driver.close()



try:
    element = WebDriverWait(driver, 30). until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-group-item"))
    )
    #element.click()
    #print("list-group-item ready...")
except:
    driver.quit()
    driver.close()

search = driver.find_element(By.XPATH, "//a[@title='A']")
print("Väljer Motorcykel: A")
search.click()




try:
    element = WebDriverWait(driver, 30). until(
        EC.presence_of_element_located((By.ID, "examination-type-select"))
    )
    #element.click()
    #print("examination-type-select element ready...")
except:
    driver.quit()
    driver.close()
select = Select(driver.find_element(By.ID,'examination-type-select'))
select.select_by_value('10')
print("väljer körprov")
print("rensar sökfältet")
try:
    element = WebDriverWait(driver, 300). until(
        EC.presence_of_element_located((By.ID, "id-control-searchText-1-1"))
    )
    driver.find_element(By.ID, "id-control-searchText-1-1").clear()
except:
    driver.quit()
time.sleep(2)

listofplaces = ["Västerås", "Örebro", "Gillinge trafikövningsplats", "Gillinge Trafikövningsplats 2", "Tullinge", "Tullinge 2", "Eskilstuna", "Köping", "Nyköping", "Norrköping", "Katrineholm", "Uppsala", "Falun", "Malung", "Eksjö", "Vimmerby", "Jönköping", "Oskarshamn", "Halmstad", "Västerås", "Gävle", "Bollnäs", "Karlstad"]
while True:
    for x in listofplaces:
        print(x)
        time.sleep(2)
        def retrieve_messages(channelid):
            headers = {
                'authorization': 'YOUR_DISCORD_TOKEN'
            }
            r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
            jsonn = json.loads(r.text)
            for value in jsonn:
                discordmsg = (value['content'], '\n')
                if "stop" in discordmsg: #Om man skriver 'stop' i discordkanal-chatten stoppar botten, du kan då logga in och boka tiden själv.
                    print("stop exist!")
                    driver.close()
                    sys.exit()


        retrieve_messages('DITT DISCORD KANAL ID')
        driver.find_element(By.ID, "id-control-searchText-1-1").clear()
        time.sleep(1)
        driver.find_element(By.ID, "id-control-searchText-1-1").send_keys(x + Keys.ENTER)
        try:
            element = WebDriverWait(driver, 3). until(
            EC.presence_of_element_located((By.CLASS_NAME, "col-xs-6"))
            )
            print("LOOKING FOR: " + x)
            stad = x #Dessa tider letar botten efter!
            datum = ['2022-06-17', '2022-06-18', '2022-06-19', '2022-06-20', '2022-06-21', '2022-06-22', '2022-06-23', '2022-06-24', '2022-06-25', '2022-06-26']
            for b in datum:
                src = driver.page_source
                if b in src:
                    print("Finns tid: " + b + " i " + stad)
                    payload = {
                        'content': "Finns tid: " + b + " i " + stad
                    }
                    header = {
                            'authorization': 'YOUR_DISCORD_TOKEN'
                    }
                    r = requests.post("URL_TO_YOUR_DISCORD_CHANNEL",
                                      data=payload, headers=header)
        except Exception as e:
            print(e)
            driver.close()

