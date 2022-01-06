import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
CREDENTIAL_DIR = os.path.join(PARENT_DIR,'check')
GET_FILE = os.path.join(CREDENTIAL_DIR,'pwd.txt')

with open(GET_FILE,'r') as f:
	pwd = f.read()


username = 'fakeCodeTry@gmail.com'
password = pwd

