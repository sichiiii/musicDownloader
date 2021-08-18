from selenium import webdriver
from time import sleep
import json, wget

url = 'https://bananastreet.ru/86012-papa-tin-bananaday-114'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
driver = webdriver.Chrome('/home/jabka/Downloads/chromedriver', chrome_options=options)

def auth():
    driver.get('https://bananastreet.ru/')
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div').click()
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
    #source = '\u0026'
    print(source['downloadUrl'])
    wget.download(source['downloadUrl'])

auth()
getMusic(url)