print("hi world")
from selenium import webdriver

url = 'https://nusmods.com/modules/PL3249/memory'

driver_path = './chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

another_url = driver.find_element_by_xpath('//*[@id="prerequisites"]/div/ul/li/ul/li/ul/li[1]/div/a')
print(another_url)

print("Done")