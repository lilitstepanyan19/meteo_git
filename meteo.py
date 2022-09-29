from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text

import smtplib
from email.mime.text import MIMEText

link = 'https://www.gismeteo.com/'

period_list = ["now", "today", "tomorrow", "3 days", "10 days", "2 weeks", "month", "7 days"]
country = input('Select a country: ')
inp = input(f'Select a period from the list: {period_list}: ')
# country = 'gyumri'
# inp = '3 days'

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)




search_info = browser.find_element(By.CSS_SELECTOR, '.input.js-input')
search_info.send_keys(country)

search_btn = browser.find_element(By.CLASS_NAME, 'search-item')
search_btn.click()


if inp in period_list:
    if ' ' in inp:
        inp = inp.replace(' ', '\u00a0')
    period_info = browser.find_element(By.XPATH, f'//a[text()="{inp}"]')
    period_info.click()
else:
    print("No result")


date = browser.find_elements(By.CSS_SELECTOR, '.widget-date-wrap>.item')
d_date = []
for el in date:
    if el.text == '' or el.text in d_date:
        continue
    d_date.append(el.text)

date_time = browser.find_elements(By.CSS_SELECTOR, '.widget-row>.row-item>span')
d_time = []
for el in date_time:
    if el.text == '' or not el.text.isalpha():
        continue
    d_time.append(el.text)

date_temp = browser.find_elements(By.CSS_SELECTOR, '.chart>.values>.value')
d_temp = []
for el in date_temp:
    if el.text == '':
        continue
    d_temp.append(el.text)


date_value = []
for i in range(len(d_date)):
    d = {}
    for j in range(i*4,i*4+4):
        d[d_time[j]] = d_temp[j]
    i+=4
    date_value.append(d)
    

data = {}

for i in range(len(d_date)):
    data[d_date[i]] = date_value[i]  
    
print(data)    
    
with open('meteo.txt', 'w') as f:
    f.write(str(data))
    f.close()
browser.close()

with open('meteo.txt', 'r') as f:
    m = f.read()
    f.close()


# print(m)

# sender = 'stepanyanlilt@gmail.com'
# password = 'ldtbywcwkouztyea'
# server = smtplib.SMTP('smtp.gmail.com', 587)

msg = MIMEText(m)
msg["Subject"] = f'Meteo for {inp} in {country.title()}'

sender = 'lil-lid@mail.ru'
to = 'tigran.barsegyan@gmail.com'
password = 'X89UzgG4EYMgnuKP6kFj'
server = smtplib.SMTP('smtp.mail.ru', 587)

server.starttls()

server.login(sender, password)
server.sendmail(sender, sender, msg.as_string())

server.sendmail(sender, to, msg.as_string())



