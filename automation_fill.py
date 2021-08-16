from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def run_web(id, year, specialty):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://e-services.clalit.co.il/onlinewebquick/nvgq/tamuz/he-il')

    idbox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userId"]')
    idbox.send_keys(id)

    yearbornebox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userYearOfBirth"]')
    yearbornebox.send_keys(year)

    moveonbutten = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_btnLogin_lblInnerText"]')
    moveonbutten.click()

    time.sleep(1)
    driver.get('https://e-services.clalit.co.il/OnlineWebQuick/QuickServices/Tamuz/TamuzTransferContentByService.aspx')
    driver.find_element_by_id("ProfessionVisitButton").click()
    select = Select(driver.find_element_by_name('SelectedSpecializationCode'))
    switcher = {
        "orthopedics": "58",
        "otolaryngology": "62",
        "breast surgeon": "501",
        "women": "63",
        "skin": "31",
        "eyes": "61"
    }
    specialty_number = switcher.get(specialty, "0")
    select.select_by_value(f'{specialty_number}')
    driver.find_element_by_xpath('//*[@id="professionSection"]/div[2]/div[1]/table/tbody/tr[4]/td[3]/input').click()
    # html_list = driver.find_element_by_id("diariesList")
    # items = html_list.find_elements_by_tag_name("li")[0]
    # print(item.text)
    # f = driver.find_element_by_xpath('//*[@id="diariesList"]/li[1]/div[1]/div[1]/a')
    # print(f.text)
    time.sleep(20)


run_web("311221790", "1993", "skin")


