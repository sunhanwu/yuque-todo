import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendMail(fromAddr:str, toAddr:str, password:str, subject:str, msg:str, smtpServer:str, stmpPort=465):
    """
    send email
    :param fromAddr:
    :param toAddr:
    :param password:
    :param subject:
    :param msg:
    :return:
    """
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(fromAddr, 'utf-8')
    message['To'] = Header(toAddr, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP_SSL(smtpServer, stmpPort)
    try:
        smtp.connect(smtpServer)
        smtp.login(fromAddr, password)
        smtp.sendmail(fromAddr, [toAddr], message.as_string())
        print("{}发送到{}邮件成功".format(fromAddr, toAddr))
    except(smtplib.SMTPException) as e:
        print(e.message)
    finally:
        smtp.quit()
