from selenium import webdriver
import time
 
browser = webdriver.Firefox()
browser.fullscreen_window()
 
browser.get("https://twitter.com/explore")
 
time.sleep(6)
 
giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[1]/a/div/span/span")
 
giris_yap.click()
 
time.sleep(5)
 
username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
 

username.send_keys("username)
password.send_keys("şifre")
 
time.sleep(5)
login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span")
login.click()
 
time.sleep(5)
searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("#yazılımayolver")
searchArea.send_keys(u'\ue007')

time.sleep(5)


lenOfPage=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):   
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)


elements = browser.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr")


for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("Bir sorun oluştu...")



