import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from send import Template

user_name = '<Display Name>'
username = '<your_email@gmail.com>'
password = '<password>'

class Emailer():
	subject = ""
	content_name = ""
	to_emails = []
	from_email = username
	template_name_text = None  
	template_name_html = None
	has_html = False
	user_name = ""

	def __init__(self, subject="", content_name="", to_emails=[], from_email='<Display Name> <'+username+'>', template_name_text=None, template_name_html=None, has_html=False, user_name=""):
		if template_name_html == None and template_name_text == None:
			raise Exception("You must set a template")
		assert isinstance(to_emails, list)

		self.to_emails = to_emails
		self.subject = subject
		
		if template_name_html != None:
			self.has_html = True
			self.template_name_html = template_name_html
		
		self.template_name_text = template_name_text
		self.content_name = content_name
		self.user_name = user_name

	def format_message(self):
		msg = MIMEMultipart('alternative')
		msg['From'] = self.from_email
		msg['To'] = ','.join(self.to_emails)
		msg['Subject'] = self.subject

		if self.template_name_text != None:
			template_obj = Template(
				template_content_name = self.template_name_text, 
				context_name = self.content_name, 
				user_name = self.user_name
			)
			text_part = MIMEText(template_obj.render_name_in_template(), 'plain')
			msg.attach(text_part)
		
		if self.template_name_html != None:
			template_obj = Template(
				template_content_name = self.template_name_text, 
				context_name = self.content_name
			)
			html_part = MIMEText(template_obj.render_name_in_template(context_name = self.context_name), 'html')
			msg.attach(html_part)

		return msg.as_string()

	def send(self):
		msg_str = self.format_message()
		did_send = False
		# Login to the server
		server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		try:
			server.sendmail(self.from_email, self.to_emails, msg_str)
			did_send = True
		except:
			did_send = False
		server.quit()
		return did_send

send_mail_obj = Emailer(
	subject = "<Enter the Subject>", 
	content_name = "<Receiver Name>", 
	to_emails = ['<email1@gmail.com>', '<email2@gmail.com>'], 
	template_name_text = 'content.txt', 
	user_name = user_name
)
send_mail = send_mail_obj.send()

if send_mail:
	print("Message sent successfully")
else:
	print("Unable to send message") 


