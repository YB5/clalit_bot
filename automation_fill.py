from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def run_web(id,year):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://e-services.clalit.co.il/onlinewebquick/nvgq/tamuz/he-il')

    idbox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userId"]')
    idbox.send_keys(id)

    yearbornebox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userYearOfBirth"]')
    yearbornebox.send_keys(year)

    moveonbutten = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_btnLogin_lblInnerText"]')
    moveonbutten.click()

    time.sleep(5)
    ProfessionVisitButton = driver.find_element_by_link_text("לרופאים יועצים").click()

#run_web("311221790","1993")


