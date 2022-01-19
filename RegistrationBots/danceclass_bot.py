import time

import json
import chromedriver_binary
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

f = open('data.json')

data = json.load(f)

f.close()

print(data)

wd = wd.Chrome()

wd.maximize_window()

# wd.implicitly_wait(10)

wd.get('http://silvercatstudio.pl/?fbclid=IwAR2vEhSOD7fIBBQznV4nT9diJvjuj5K26558dkK5i_Yjg8EtlIjZ95F3fvs')

wd.implicitly_wait(10)
book_dat_button = wd.find_element(By.XPATH, '//*[@id="section-2"]/div[1]/div/div/div/div/div[2]/a')

book_dat_button.click()
wait = WebDriverWait(wd, 1)
while True:
    try:
        wd.switch_to.window(wd.window_handles[1])
        break
    except:
        time.sleep(1)

while True:
    try:
        sign_in_button = wd.find_element(By.XPATH, '//*[@id="sign-in"]')

        sign_in_button.click()

        # if you have an account
        sign_in_button2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dialogContent_0"]/div/div[1]/button')))

        # if you don't have an account
        # sign_in_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dialogContent_0"]/div/div[2]/button')))

        sign_in_button2.click()
        wd.switch_to.window(wd.window_handles[2])
        break
    except:
        time.sleep(1)

login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_0"]')))
login.send_keys(data['login'])
password = wd.find_element(By.XPATH, '//*[@id="input_1"]').send_keys(data['password'])

loginBtn = wd.find_element(By.XPATH, '//*[@id="login-button"]/button').click()

wd.implicitly_wait(10)

activities_name = "//*[contains(text(), '" + data['activities'] + "')]"

day_id = "md-1-month-" + str(data['year']) + "-" + str(data['month']) + "-" + str(data['day'])
print(day_id)

wait2 = WebDriverWait(wd, 0.1)
# while True:
while True:
    try:
        dateDiv = wait2.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="my-training-datepicker"]/div/input')))
        dateDiv.click()
        time.sleep(0.1)
        day = wait2.until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(@aria-label, 'Wednesday January 26 2022')]")))
            # EC.presence_of_element_located((By.XPATH, "//td[contains(@aria-label, 'Tuesday January 4 2022')]")))
        # time.sleep(1)
        day.click()

        time.sleep(0.5)


        #
        button = wd.find_element(By.XPATH, '//*[@id="tab-content-2"]/div/table/tbody/tr[5]/td[5]/button')
        # for i in range(1):
        #     parent = choose_activities_btn.find_element(By.XPATH, "./parent::*")
        #
        # button = button_parent.find_element(By.TAG_NAME, 'button')

        # buttons = parent.find_elements(By.TAG_NAME, 'button')
        #
        # # button = wd.find_element(By.XPATH, '//*[@id="tab-content-2"]/div/table/tbody/tr[6]/td[5]/button')
        # disabled = wd.execute_script("return arguments[0].hasAttribute(\"ng-disabled\");", button)
        # button.click()
        # print(button.get_property('disabled'))
        if not button.get_property('disabled'):
            while True:
                try:
                    time.sleep(0.05)
                    button.click()
                    break
                except:
                    button = wd.find_element(By.XPATH, '//*[@id="tab-content-2"]/div/table/tbody/tr[5]/td[5]/button')
                    time.sleep(0.01)
            time.sleep(0.05)
            while True:
                try:
                    button2 = wd.find_element(By.XPATH,
                                              '//*[@id="tab-content-2"]/div/table/tbody/tr[5]/td[5]/div[1]/button')
                    button2.click()
                    break
                except:
                    time.sleep(0.01)

            print('clicked')
            break
        else:
            # time.sleep(0.1)
            wd.refresh()
    except:
        time.sleep(0.1)
        # wd.refresh()
# break


time.sleep(15)
wd.close()