import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

sender_email = "<your_email@gmail.com>"
sender_password = "<your_password>"
receiver_email = "<receiver_email@gmail.com>"

def send_mail():
  message = MIMEMultipart("alternative")
  message["Subject"] = "<SUBJECT>"
  message["From"] = sender_email
  message["To"] = receiver_email

  html_content = """\
  <html>
    <body>
      <h1>Hello World</h1>
      <p>What are you doing?</p>
    </body>
  </html>
  """

  image = '<path_to_image>'
  with open(image, 'rb') as f:
    img_data = f.read()

  image_name = (image.split('.'))[0]

  # Turn these into plain/html MIMEText objects
  html_mime = MIMEText(html_content, "html")
  image_mime = MIMEImage(img_data, name=os.path.basename(image_name))

  message.attach(html_mime)
  message.attach(image_mime)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

send_mail()