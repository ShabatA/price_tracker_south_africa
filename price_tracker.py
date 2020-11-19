import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib, ssl
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# list to store the links and the current price
items = []
driver = webdriver.Chrome()


def sendMail(title, URL, original, new):
    '''
    This function send an email to a partcular email

    args:
    title: the product title 
    URL: Webpage link
    original: the product original price
    new: the new price
    '''
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        subject = f"Price dropped for {title}"
        body = f"Old Price: {original}\nNew Price: {new}\nDifference: {original - new}\n{URL}\n Designed by: Dr. Abuobayda Shabat"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient, msg)
        print("Sent email")


def takealot_data(url):
    '''
    This function extract the data from Takealot website
    args:
    url: Webpage link
    '''
    driver.get(url)
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "product-title")))
    except TimeoutException:
        driver.quit()
    
    page_source = driver.page_source
    
    soup = BeautifulSoup(page_source, 'lxml')
    
    price = soup.find('span', class_='currency plus currency-module_currency_29IIm').get_text()
    title = soup.find('div', class_='product-title').get_text().strip()

    price = float(price[1:].strip())
    return price, title


def makro_data(url):
    '''
    This function extract the data from Makro website
    args:
    url: Webpage link
    '''
    driver.get(url)
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "price")))
    except TimeoutException:
        driver.quit()
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    price = soup.find('p', class_='price').get_text()
    title = soup.find('b', class_='code mak-typo__large mak-typo__h1-md').get_text().strip()
    price = price.strip().strip('00').replace(',','')
    price = float(price[1:].strip())
    
    return price, title


def game_data(url):
    '''
    This function extract the data from Makro website
    args:
    url: Webpage link
    '''
    driver.get(url)
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "pdp_price")))
        
    except TimeoutException:
        driver.quit()
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    
    price = soup.find('span', class_='pdp_price').get_text()
    # title = soup.find('div', class_='product-title').get_text()
    title = soup.find('div', class_='name').get_text().strip()
    price = price.strip().strip('.00').replace(',','')
    price = float(price[1:].strip())
    return price, title