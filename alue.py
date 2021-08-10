from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import timeit as t
import pandas as pd


# Простоянные переменные
driver = webdriver.Firefox()
app_login = 'kaznu@oqylyq.kz'
app_password = 'yhxTQRBc2n'
delay = 9

driver.get('https://app.oqylyq.kz/')
sleep(1.7)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div[1]/div/input').send_keys(app_login)
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys(app_password)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[4]/div/button/div[2]').click()
sleep(3)
driver.get('https://app.oqylyq.kz/t/assignments/38651')
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]/div[2]/div/div/div[2]/div[1]').click()
#/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]/div[2]/div/div/div[2]/div[1]
#/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[9]/div/div[1]/div[2]/div/div/div[2]/div[1]
sleep(3)
driver.find_element_by_xpath("//*[contains(text(), '100 студентов')]").click()
sleep(3)
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[9]/div/div[3]/div/ul/li[3]/a').click()
#sleep(3)
#/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[9]/div/div[1]/div[2]/div/div[2]
student_number = 1
for i in range(120):
    while True:
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/a[{student_number}]/div[2]/div').click()
            break
        except:
            continue
    while True:
        try:
            driver.find_element_by_class_name('quiz-result-item').click()
            break
        except:
            continue

    question3 = ""
    question1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]').text
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/div[2]/div').click()
    question2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]').text
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]').click()
    #/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/span[1]/div
    try:
        driver.find_element_by_xpath(
           '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/div[3]/div').click()
        question3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]').text
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]').click()
    except:
        print('2 bl')
    name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/a[{student_number}]/div[2]/div').text
    file = open(f'{name}.txt', "w", encoding='utf-8')
    questions = (question1 + '\n' + question2 + '\n' + question3)
    file.write(questions)
    file.close()
    driver.find_element_by_xpath(
        f'/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[2]/div/a[{student_number}]/div[2]/div').click()
    if student_number == 100:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[10]/div/div[3]/div/ul/li[3]/a').click()
        student_number = 1
    student_number += 1
#/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]