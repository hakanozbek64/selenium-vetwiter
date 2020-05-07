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
 

username.send_keys("username")
password.send_keys("şifre")
 
time.sleep(5)
login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span")
login.click()
 
time.sleep(5)
searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("Altera Cyclone IV FPGA")
searchArea.send_keys(u'\ue007')

time.sleep(5)


lenOfPage=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):   
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
time.sleep(5)
tweets = []

elements = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")

for element in elements:
        tweets.append(element.text)
        
tweetCount = 1


with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("*************************\n")
        tweetCount +=1



