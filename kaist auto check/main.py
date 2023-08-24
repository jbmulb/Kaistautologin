import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# make chrome tab not close
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


url_path = "https://talented.kaist.ac.kr:8443"

driver = webdriver.Chrome(options=options) # 웹 드라이버 생성
driver.implicitly_wait(1) # wait time
driver.get(url_path) # url로 이동
driver.maximize_window() # 화면 최대화

driver.implicitly_wait(5)


# driver.find_element(By.CSS_SELECTOR, 'body > main > div:nth-child(1) > div > div > div:nth-child(1) > button').click()

driver.find_element(By.CSS_SELECTOR, '#userId').send_keys('14ip2212')
driver.find_element(By.CSS_SELECTOR, '#userPw').send_keys('lego0625@@')

driver.find_element(By.CLASS_NAME, 'login-btn').click()
driver.implicitly_wait(2)