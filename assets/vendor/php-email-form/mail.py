from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["From"]="weltrestaurante@yopmail.com"
mensaje["To"]= "mateogariboglio@gmail.com"
mensaje["Subject"] ="Oremos"
adjunto = MIMEBase("application","octect-stream")
mensaje.attach(adjunto)
smtp = SMTP("smtp.yopmail.com")
#smtp.gmail.com for google accounts
#smtp.yahoo.com for yahoo accounts
smtp.starttls()
smtp.login("weltrestaurante@yopmail.com")
smtp.sendmail("weltrestaurante@yopmail.com","targetMail",mensaje.as_string())
smtp.quit()