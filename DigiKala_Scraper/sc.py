import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    url = 'https://www.digikala.com/product/dkp-1560848/%D9%85%DB%8C%DA%A9%D8%B1%D9%88%D9%81%D9%88%D9%86-%D8%B1%DB%8C%D8%A8%D9%88%D9%86-%D8%A8%DB%8C%D8%B1%D8%AF%D8%A7%DB%8C%D9%86%D8%A7%D9%85%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-tg-v90#/tab-desc'
    headers = {'User-Agent': 'YOUR_USER_AGENT'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # title = soup.find('div', {'class': 'c-product__headline'}).get_text()
    price = soup.find('div', {'class': 'c-product__seller-price-raw js-price-value'}).get_text()
    price = price.strip()

    table = {
            44: 46,    # .
            1776: 48,  # 0 
            1777: 49,  # 1
            1778: 50,  # 2
            1779: 51,  # 3
            1780: 52,  # 4
            1781: 53,  # 5
            1782: 54,  # 6
            1783: 55,  # 7
            1784: 56,  # 8
            1785: 57}  # 9

    price = price.translate(table)
    price = price[0:5]
    price = float(price)

    if price <= 4.0:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR_USER', 'YOUR_PASSWORD')

    subject = 'Digikala Price'
    body = 'agha bodo ke arzoon shod!! -> https://www.digikala.com/product/dkp-1560848/%D9%85%DB%8C%DA%A9%D8%B1%D9%88%D9%81%D9%88%D9%86-%D8%B1%DB%8C%D8%A8%D9%88%D9%86-%D8%A8%DB%8C%D8%B1%D8%AF%D8%A7%DB%8C%D9%86%D8%A7%D9%85%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-tg-v90#/tab-desc'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'FROM_EMAIL@EXAMPLE.COM',
        'TO_EMAIL@EXAMPLE.COM',
        msg
    )
    print('email sent!!')
    server.quit()

while(True):
    check_price()
    time.sleep(3600 * 12)
