from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json, wget, sys

#example: https://bananastreet.ru/86012-papa-tin-bananaday-114

s=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options, service=s)

def auth():
    driver.get('https://bananastreet.ru/')
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div/div').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[1]').click()
    login = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div/div[2]/div[1]/div[2]/input')
    password = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div/div[2]/div[2]/div[2]/input')
    login.send_keys('testformusicapi@gmail.com')
    password.send_keys('karonespidor')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div/div[2]/button').click()
    sleep(3)

def getMusic(url):
    downloadUrl = url[:29]
    id = downloadUrl[-5:]
    downloadLink = 'https://bananastreet.ru/api/releases/' + id + '/limited_download'
    driver.get(downloadLink)
    content = driver.find_element_by_tag_name('pre').text
    source = content.replace("\\u0026", "&")
    source = json.loads(source)
    wget.download(source['downloadUrl'])
    
try:
    print("Authentication... ")
    auth()
    url = input("Please enter url: ")
    print('Downloading... ')
    getMusic(url)
    print('\nSuccess! ')
except Exception as ex:
    print(str(ex))
