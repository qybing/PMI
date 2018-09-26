from selenium import webdriver

driver_path = r'E:\ch\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://hotels.ctrip.com/hotel/428365.html')
html = driver.page_source
print(html)