import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

def sendMail(fromAddr:str, toAddr:str, password:str, subject:str, msg:str, smtpServer:str, stmpPort=465):
    """
    send email
    :param fromAddr: sender mail address
    :param toAddr: mail receiver address
    :param password: authorization code
    :param subject: mail subject
    :param msg: mail message
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
        logging.info("{} sent to {} success".format(message.as_string(), toAddr))
    except(smtplib.SMTPException) as e:
        logging.error("sending mail error, message: {}".format(e.message))
    finally:
        smtp.quit()
