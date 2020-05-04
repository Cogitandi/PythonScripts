import webbrowser, re, io, time, random, logging, os
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='C:\\Users\\TiMan\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\geckodriver.exe')
logging.basicConfig(format='%(asctime)s %(message)s')

def captcha(main_window):
  downloadCaptcha()
  # open new tab
  browser.execute_script("window.open(''),'_blannk'")
  # change focus to new tab
  browser.switch_to.window(browser.window_handles[1])
  # get content
  browser.get("https://ocr.space")
  # get upload button
  uploadClick = browser.find_element_by_xpath('//*[@id="imageFile"]')
  # upload captcha image
  uploadClick.send_keys('C:\\Users\\TiMan\\Desktop\\captcha1.png')
  # get start button
  startButton = browser.find_element_by_css_selector('#btnStartOCR > a:nth-child(1)')
  # click start button
  startButton.click()
  # wait 3 seconds
  time.sleep(3)
  # get textarea with encode captcha
  resultText = browser.find_element_by_css_selector('#txtAreaParsedResult')
  # get captcha code
  text = resultText.get_attribute("value")
  regex = re.compile(r'\n\*\*\*\*\*\* Result for Image/Page 1 \*\*\*\*\*\*\n(.+)\n')
  code = regex.findall(text)
  if len(code) == 0:
    logging.warning("Nie odczytano kodu")
    os.rename("captcha1.png","captcha"+str( random.randint(0,1000))+".png" ) 
    browser.close()
    browser.switch_to.window(main_window)
    time.sleep(1)
    return False
  code = code[0]
  code = code.replace(" ","")
  code = code.replace("*","x")
  browser.close()
  browser.switch_to.window(main_window)
  return code

def downloadCaptcha():
  time.sleep(2)
  captchaIMG = browser.find_element_by_css_selector('#content_ajax > article > form > table:nth-child(1) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(9) > td:nth-child(2) > img')
  image = captchaIMG.screenshot_as_png
  imageStream = io.BytesIO(image)
  im = Image.open(imageStream)
  im.save("captcha1.png")

def checkCreate():
  try:
    captchaError = browser.find_element_by_css_selector('#content_ajax > article > div > div > div.ErrorMessage > li')
    logging.warning("Zle odczytano kod")
  except NoSuchElementException:
    logging.warning("Zalozono konto")
def program():
  browser.get("https://www.prostoriaots.pl/?subtopic=createaccount")
  main_window= browser.current_window_handle
  accInput = browser.find_element_by_css_selector('#account_name')
  emailInput = browser.find_element_by_css_selector('#email')
  passInput = browser.find_element_by_css_selector('#passor')
  pass2Input = browser.find_element_by_css_selector('#passor2')
  codeInput = browser.find_element_by_css_selector('#verify')
  agree = browser.find_element_by_css_selector('#rules')
  submit = browser.find_element_by_css_selector('#content_ajax > article > form > table:nth-child(3) > tbody > tr > td:nth-child(2) > input[type=image]')

  code = captcha(main_window)
  if code == False:
    return

  accName = random.randint(000000000,999999999)
  email = "essajdu@sp.pl"
  password = random.randint(000000000,999999999)
  
  accInput.send_keys(accName)
  emailInput.send_keys(email)
  passInput.send_keys(password)
  pass2Input.send_keys(password)
  codeInput.send_keys(code)
  agree.click()
  submit.click()


  
while 1>0:
  program()
  time.sleep(3)
  

