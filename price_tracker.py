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
