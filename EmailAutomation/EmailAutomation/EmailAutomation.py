import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('Senders_Email','Senders_Password')
server.sendmail('Senders_Email', 'Receivers_Email','Text_mail')
server.quit()