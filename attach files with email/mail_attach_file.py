import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = "<your_email@gmail.com>"
user_pwd = "<your_password>"
to_address = "<receiver_email@gmail.com>"

def send_email():
	msg = MIMEMultipart('alternative')
	msg['Subject'] = '<SUBJECT>'
	msg['From'] = from_address
	msg['To'] = to_address

	body_content = 'This email includes file ppt'
	msg_body = MIMEText(body_content, 'plain')

	msg.attach(msg_body)

	filename = '<filename>'
	with open(filename, 'rb') as f:
		attachment = f.read()

	file_mime = MIMEBase('application', 'octet-stream')
	file_mime.set_payload((attachment))
	encoders.encode_base64(file_mime)
	file_mime.add_header('Content-Disposition', f'attachment;filename={filename}')
	msg.attach(file_mime)

	msg_str = msg.as_string()

	server = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
	server.ehlo()
	server.starttls()
	server.login(from_address,user_pwd)
	server.sendmail(from_address,to_address,msg_str)
	server.quit()

send_email()
