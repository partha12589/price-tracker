from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib
from email.message import EmailMessage
import time
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("EMAIL_USER1")
sender_password = os.getenv("EMAIL_PASS")
receiver_email = os.getenv("EMAIL_USER2")

def send_email_notification_price_drop(product_title, price):
    msg = EmailMessage()
    msg["Subject"] = "💰 Price Drop Alert!"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"The price of '{product_title}' has dropped to {price}!\nCheck it here:\nhttps://www.lenovo.com/in/en/p/laptops/legion-laptops/legion-5-series/lenovo-legion-5i-gen-9-16-inch-intel/83dg00lfin")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def send_email_notification_no_drop(product_title, price):
    msg = EmailMessage()
    msg["Subject"] = "Price Update for your laptop"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"The price of '{product_title}' is currently {price}!\nCheck it here:\nhttps://www.lenovo.com/in/en/p/laptops/legion-laptops/legion-5-series/lenovo-legion-5i-gen-9-16-inch-intel/83dg00lfin")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


max=99999999
while True:
    try:
        service = Service("C:/Users/parth/Downloads/chromedriver-win64/chromedriver.exe")

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")       

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.lenovo.com/in/en/p/laptops/legion-laptops/legion-5-series/lenovo-legion-5i-gen-9-16-inch-intel/83dg00lfin")

        time.sleep(3)  

        title = driver.find_element(By.CLASS_NAME, "product_summary").text
        price= driver.find_element(By.CLASS_NAME,"price-title").text
        
        cp=int(price[1:].replace(',',""))
        if(cp<max):
            max=cp
            send_email_notification_price_drop(title,price)
        else:
            send_email_notification_no_drop(title,price) 
        
        driver.quit()
    except Exception as e:
        print("Something went wrong:", e)

    time.sleep(4 * 60 * 60)
