from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text


def get_period_info_click(inp_period, period_list):
    if inp_period in period_list:
        if ' ' in inp_period:
            inp_period = inp_period.replace(' ', '\u00a0')
        period_info = browser.find_element(By.XPATH, f'//a[text()="{inp_period}"]')
        period_info.click()
    else:
        return "No result"
    return


def get_date(date):
    d = []
    for el in date:
        if el.text == '' or el.text in d:
            continue
        d.append(el.text)
    return d


def get_time(date_time):
    d = []
    for el in date_time:
        if el.text == '' or not el.text.isalpha():
            continue
        d.append(el.text)
    return d


def get_temp(date_temp):
    d = []
    for el in date_temp:
        if el.text == '':
            continue
        d.append(el.text)
    return d

def get_date_value(d_date, d_time, d_temp):
    d_value = []
    for i in range(len(d_date)):
        d = {}
        for j in range(i*4,i*4+4):
            d[d_time[j]] = d_temp[j]
        i+=4
        d_value.append(d)
    return d_value

def get_data(d_date, date_value):
    data = {}
    for i in range(len(d_date)):
        data[d_date[i]] = date_value[i]  
    return data
    
def get_today_time(today_time):
    ml = []
    for el in today_time:
        h = el.text[:-2] + ':' + el.text[-2:]
        if h in ml:
            continue
        ml.append(h)
    return ml

def get_today_temp(today_temp):
    ml = []
    for i in range(0, len(today_temp), 2):
        ml.append(today_temp[i].text)
    return ml 



def get_write_info(data_result):
    with open('meteo.txt', 'w') as f:
        f.write(f'{country.title()} - {inp_period}\n')
        f.write(str(data_result))
        f.close()



def main():
    period_list = ["now", "today", "tomorrow", "3 days", "10 days", "2 weeks", "month", "7 days"]
    country = input('Select a country: ')
    inp_period = input(f'Select a period from the list: {period_list}: ')
    # country = 'gyumri'
    # inp_period = '3 days'
    
    link = 'https://www.gismeteo.com/'
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    search_info = browser.find_element(By.CSS_SELECTOR, '.input.js-input')
    search_info.send_keys(country)

    search_btn = browser.find_element(By.CLASS_NAME, 'search-item')
    search_btn.click()

    if inp_period.lower() == '3 days':
        get_period_info_click(inp_period, period_list)
        date = browser.find_elements(By.CSS_SELECTOR, '.widget-date-wrap>.item')
        date_time = browser.find_elements(By.CSS_SELECTOR, '.widget-row>.row-item>span')
        date_temp = browser.find_elements(By.CSS_SELECTOR, '.chart>.values>.value')
        d_date = get_date(date)
        d_time = get_time(date_time)
        d_temp = get_temp(date_temp)
        date_value = get_date_value(d_date, d_time, d_temp)
        data_result = get_data(d_date, date_value)
        print(data_result)
        get_write_info(data_result)
    elif inp_period == 'today':
        today_time = browser.find_elements(By.CSS_SELECTOR, '.widget-items>.widget-row-time>.row-item>span')
        today_temp = browser.find_elements(By.CSS_SELECTOR, '.widget-row-chart>.chart>.values>.value>span')
        today_time_house = get_today_time(today_time)
        t_temp = get_today_temp(today_temp)
        print(t_temp)
    browser.close()
print(main())



    



