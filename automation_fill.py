from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

id = '311221790'
yearborne = '1993'




driver = webdriver.Chrome(ChromeDriverManager().install())
wait = ui.WebDriverWait(driver, 10)
driver.get('https://e-services.clalit.co.il/onlinewebquick/nvgq/tamuz/he-il')

idbox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userId"]')
idbox.send_keys(id)

yearbornebox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_userYearOfBirth"]')
yearbornebox.send_keys(yearborne)

moveonbutten = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphBody_bodyContent_ucQuickLogin_btnLogin_lblInnerText"]').click()


#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
#driver.get('https://e-services.clalit.co.il/OnlineWebQuick/QuickServices/Tamuz/TamuzTransfer.aspx')
#time.sleep(8)
#wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="ProfessionVisitButton"]'))
#driver.execute_script("window.scrollTo(0, 1800)")
time.sleep(5)
ProfessionVisitButton = driver.find_element_by_xpath('//*[@id="ProfessionVisitButton"]').click()



