import smtplib
from email.mime.text import MIMEText


def get_read_info(fname):
    with open('meteo.txt', 'r') as f:
        m = f.read()
        f.close()
    return m
    
def get_readline(fname):
    with open(fname, 'r') as f:
        m = f.readline()
        f.close()
    return m

def get_title(title):
    title = title.split(' - ')
    return title
    
# sender = 'stepanyanlilt@gmail.com'
# password = 'ldtbywcwkouztyea'
# server = smtplib.SMTP('smtp.gmail.com', 587)

def get_send(message, title_list):
    msg = MIMEText(message)
    msg["Subject"] = f'Meteo for {title_list[1]} in {title_list[0].title()}'

    sender = 'lil-lid@mail.ru'
    # to = 'tigran.barsegyan@gmail.com'
    password = 'X89UzgG4EYMgnuKP6kFj'
    server = smtplib.SMTP('smtp.mail.ru', 587)

    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, sender, msg.as_string())

    server.sendmail(sender, to, msg.as_string())
    return

def main():
    fname = 'meteo.txt'
    message = get_read_info(fname)
    title = get_readline(fname)
    title_list = get_title(title)
    # inp_period = title_list[0]
    # country = title_list[1]
    get_send(message, title_list)
    print(message)
print(main())










